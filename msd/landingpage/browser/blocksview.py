"""

    Helper functions to expose blocks to layout views in easy-to-render form.

"""


from cStringIO import StringIO

import zope.interface
from zope.interface import implements, Interface
from zope.traversing.interfaces import ITraverser, ITraversable
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces.browser import IBrowserRequest

from zope.security import checkPermission
from zope.component import getMultiAdapter, queryMultiAdapter, getUtility
from Acquisition import aq_inner
from plone.portlets.interfaces import IPortletManager, IPortletManagerRenderer

from five import grok

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from zope.component import getMultiAdapter

from msd.landingpage import HAS_PLONE4

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ILandingPage, IBigBlock, ILayoutView, ILittleBlock
from msd.landingpage.layout import Layout, Block
from msd.landingpage.browser.blocks import BaseBlockView

from msd.landingpage.utilities import getViewForLittleBlock

grok.templatedir("block_templates")

class BigBlock(grok.View):
    """
    """
    
    grok.context(IBigBlock)
    
    def setBlockIndex(self, index):
        """
        Know which block we are.
        """
        self.number = index
        
    def getBlockIndex(self):
        return self.number
    
    @property
    def portal_state(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        
        return portal_state       
    
    def showAddLink(self):
        return checkPermission('cmf.AddPortalContent', self.context)

    
    def total_weight(self):
        """
        @return: Sum all little blocks weight inside this block minus 6 if view has visible portlets 
        """
        weight = 0
        items = self.context.contentItems()
        for id, block in items:
            weight += block.getWeight()
        
        #TODO: get rid of hardcoded weight penalty of 6 if there is portlets
        #if self.layout_has_portlets():
        #    weight -= 6
            
        return weight
    
    def units(self):
        """ How many units this block is wide.
        """
        layout = self.getLayout()
        case = self.getLayoutCase()
        block = self.getBlockDefinition()
        return block.getWidthInCase(case)
    
    def getLayoutCase(self):
        """ Which kind of layout case we are dealing with.
        """
        if not self.getLayout().show_portlets:
            return Block.CASE_NO_PORTLETS
        
        if self.have_portlets("plone.rightcolumn") and self.have_portlets("plone.leftcolumn"):
            return Block.CASE_TWO_PORTLET_COLUMNS
        
        if self.have_portlets("plone.leftcolumn"):
            return Block.CASE_ONE_PORTLET_COLUMN
        
        if self.have_portlets("plone.leftcolumn"):
            return Block.CASE_ONE_PORTLET_COLUMN
        
        return  Block.CASE_NO_PORTLETS
        
    def getCSSClasses(self):
        """
        Generate CSS class string for the big block.
        """
        classes = "big-block big-block-index-%d big-block-total-weight-%d " % (self.number, self.total_weight())
        
        block = self.getBlockDefinition()

        # Block might not be defined 
        # in the layout view class 
        if block:
            case = self.getLayoutCase()
            block_classes = block.getCSSClassInCase(case)
            if block_classes:
                classes += block_classes 
                classes += " "
            
        return classes
        
    def hasBlocks(self):
        """
        @return: True if contains little blocks
        """
        return len(self.getBlocks()) > 0
        
    def getBlockDefinition(self):
        """
        @return: Block object defining the layout properties for this block
        """
        layout = self.getLayout()
        return layout.getBlock(self.getBlockIndex())

    def getDirection(self):
        """ Is this big block vertical or horizontal
        
        @return: Block.DIRECTION_XXX pseudoconstant
        """
        #TODO: Should we default to horizontal or throw error if layout does not have block_direction
        
        block = self.getBlockDefinition()
        if block:
            return block.direction
        else:
            return None
    
    def getBlocks(self):
        """ Return contained blocks.
        """
        return self.context.contentItems()
    
    def little_blocks(self):
        """ Render all little blocks and return them as string.
        """
        buffer = ""
        
        contentItems = self.context.contentItems()

        # For vertical blocks, we have blocks equal widths
        # For horizontal blocks, we calculate the width for each little block
        if self.getDirection() == Block.HORIZONTAL:
            contentItemsLength = len(contentItems)
            i = 0
            for id, little_block in contentItems:
                i += 1
                view = getViewForLittleBlock(self.request, little_block) 
        
                view_units = self.units() * little_block.getWeight() / self.total_weight()
               
                view.setUnitWidth(view_units)
               
                if i == contentItemsLength:
                    view.setIsLast(True)
                else:
                    view.setIsLast(False)
                buffer += view()
        else:
            #little blocks inside vertical big blocks always get the span width of its container
            for id, little_block in contentItems:
                view = getViewForLittleBlock(self.request, little_block)
                view.setUnitWidth(self.units())
                view.setIsLast(False)

                buffer += view()
        
        return buffer
    
    def layout_has_portlets(self):
        """ Returns True if layout allows portlets and there is portlets on either side """
        
        if not self.getLayout().show_portlets:
            return False
        
        if self.have_portlets("plone.rightcolumn"):
            return True
        
        if self.have_portlets("plone.leftcolumn"):
            return True
        
        return False
    
    # Helper methods taken from the Plone-3.3.4-py2.4.egg/Products/CMFPlone/browser/ploneview.py
    def have_portlets(self, manager_name, view=None):
        """Determine whether a column should be shown.
        The left column is called plone.leftcolumn; the right column is called
        plone.rightcolumn. Custom skins may have more portlet managers defined
        (see portlets.xml).
        """

        context = aq_inner(self.context)
        if view is None:
            view = self

        manager = getUtility(IPortletManager, name=manager_name)
        renderer = queryMultiAdapter((context, self.request, view, manager), IPortletManagerRenderer)
        if renderer is None:
            renderer = getMultiAdapter((context, self.request, self, manager), IPortletManagerRenderer)

        return renderer.visible

    def getLayout(self):
        """
        @return : active msd.landingpage.layout.Layout object from the parent landing page.
        """
        
        # HACK HACK HACK
        
        # Iterate to parent objects, until get landingpage content
        # and extract layout from it
        iter = self.context.aq_parent
        while iter:
            
            if ILandingPage.providedBy(iter):
                return iter.getActiveBlockLayout()
            
            if hasattr(self.context, "aq_parent"):
                iter = iter.aq_parent
            else:
                iter = None
    
        return None
    

class BlocksHelper(object):
    """ Exposes rendered blocks to template via Zope traversal. 
    """

    zope.interface.implements(ITraversable)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def traverse(self, name, further_path):
        """
        Allow getting a rendered by.
        
        @param name: Block number as a string. The first block is block number 0.

        @return: Viewlet HTML output

        @raise: RuntimeError if viewlet is not found
        """

        # We care about folder order here only
        big_blocks = self.context.contentItems()
        
        try:
            idx = int(name)
        except:
            raise RuntimeError("Big block id must be 0...N, got " + str(name))
        
        if idx < len(big_blocks):
            id, big_block = big_blocks[idx]
            
            # Create BigBlock renderer view
            # and set up its variables
            # and acquisition context
            view = BigBlock(big_block, self.request)
            view.setBlockIndex(idx)
            
            #Plone 4 views don't have the of attribute because they automatically have a parent pointer.           
            if not HAS_PLONE4:
                view = view.__of__(big_block)
            
            return view
        else:
            # No block which such id,
            # return just dummy filler
            return u""

class LayoutView(grok.View):
    """
    A base class for views which allows you to expose blocks in renderable in TAL.
    
    Cache the rendered result for the anonymous visitors.
    """
    implements(ILayoutView)

    grok.baseclass()

    def getCSSClass(self):
        """
        @return: CSS classes used by layout wrapped, based on layout name.
        """
        layout = self.context.getActiveBlockLayout()
        if layout:
            return "layout-" + layout.id
        else:
            return ""

    @property
    def blocks(self):
        """ 
        @return: traversable object which allows accessing rendered blocks in the template.
        """
        return BlocksHelper(self.context, self.request)
    
    #def blockUnits(self, id):
    #    view = BlocksHelper(self.context, self.request).traverse(id, [])
    #    return view.units()

    #def getBlockBlueprintCSS(self, id):        
    #    return 'layoutcolumn span-'+str(self.blockUnits(id))
    
    
class LittleBlockView(BaseBlockView):
    """
    View used for littleblocks when they are viewed directly
    """
    
    grok.context(ILittleBlock)

    def update(self):
        
        self.rendered_view = getViewForLittleBlock(self.request, self.context)

class BigBlockView(BaseBlockView):
    """
    View used for big block when it is viewed directly
    """
    
    grok.context(IBigBlock)

    def update(self):
        
        self.rendered_view = getViewForBigBlock(self.request, self.context)