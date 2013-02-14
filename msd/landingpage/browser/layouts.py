"""

    Available default layout view renderers.

"""

from zope.interface import implements, Interface

from Products.CMFCore.utils import getToolByName

from five import grok

from msd.landingpage import landingpageMessageFactory as _

# Import BlocksView
from msd.landingpage.browser.blocksview import LayoutView, ILayoutView
from msd.landingpage.layout import Block

from msd.landingpage.interfaces import ILandingPage

# All layout views are available for landing page content only
grok.context(ILandingPage)

grok.templatedir("layout_templates")

# Layout views must inherit from LayoutView
class Layout1(LayoutView):
    """
    SampleLayout browser view
    """
    icon = "layout1.png"
    title = _(u"Three horizontal")
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                (24, 18, 12), 
                                css_classes=["layoutcolumn span-24 last",
                                             "layoutcolumn span-18 last",
                                            "layoutcolumn span-12 last"],
                                ), 
                          Block(
                                Block.HORIZONTAL, 
                                (24, 18, 12), 
                                css_classes=["layoutcolumn span-24 last",
                                             "layoutcolumn span-18 last"],), 
                          Block(Block.HORIZONTAL, 
                                (24, 18, 12), 
                                css_classes=["layoutcolumn span-24 last",
                                             "layoutcolumn span-18 last"],) ]
    
class Layout2(LayoutView):
    """
    SampleLayout browser view
    """
    icon = "layout2.png"
    title = _(u"Three vertical")
    
    
    block_definitions = [ Block(Block.VERTICAL, [8,6], css_classes=["layoutcolumn span-8",
                                                                    "layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, [8,6], css_classes=["layoutcolumn span-8",
                                                                    "layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, [8,6], css_classes=["layoutcolumn span-8 last",
                                                                    "layoutcolumn span-6 last"],) ]
    
        
class Layout3(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Mixed 1")
    icon = "layout3.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [18], 
                                css_classes=["layoutcolumn span-18"],
                                ), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["layoutcolumn span-6"],),
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],),
                        ]
            
    show_portlets = False
    
class Layout4(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Squares")
    icon = "layout4.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [12], 
                                css_classes=["layoutcolumn span-12"],
                                ), 
                          Block(Block.VERTICAL, 
                                [12], 
                                css_classes=["last layoutcolumn span-12"],), 
                          Block(Block.VERTICAL, 
                                [12], 
                                css_classes=["layoutcolumn span-12"],),
                          Block(Block.VERTICAL, 
                                [12], 
                                css_classes=["last layoutcolumn span-12"],), 
                          Block(Block.VERTICAL, 
                                [12], 
                                css_classes=["last layoutcolumn span-12"],),
                        ]
            
    show_portlets = False

class Layout5(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Mixed 2")
    icon = "layout5.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [18], 
                                css_classes=["last layoutcolumn span-18"],
                                ), 
                          Block(Block.VERTICAL, 
                                [18], 
                                css_classes=["last layoutcolumn span-18"],), 
                          Block(Block.VERTICAL, 
                                [18], 
                                css_classes=["last layoutcolumn span-18"],),
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],),
                        ]
            
    show_portlets = False

class Layout6(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Mixed 3")
    icon = "layout6.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [12], 
                                css_classes=["layoutcolumn span-12"],
                                ), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],),
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],), 
                          Block(Block.VERTICAL, 
                                [6], 
                                css_classes=["last layoutcolumn span-6"],),
                        ]
            
    show_portlets = False

class Layout7(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Mixed 4")
    icon = "layout7.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [16], 
                                css_classes=["layoutcolumn span-16"],
                                ), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["layoutcolumn span-8"],), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["last layoutcolumn span-8"],),
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["last layoutcolumn span-8"],), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["last layoutcolumn span-8"],),
                        ]
            
    show_portlets = False

class Layout8(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Mixed 5")
    icon = "layout8.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.HORIZONTAL, 
                                [24], 
                                css_classes=["layoutcolumn span-24"],
                                ), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["layoutcolumn span-8"],), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["layoutcolumn span-8"],),
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["last layoutcolumn span-8"],), 
                          Block(Block.VERTICAL, 
                                [8], 
                                css_classes=["last layoutcolumn span-8"],),
                        ]
            
    show_portlets = False

class Layout9(LayoutView):
    """
    SampleLayout browser view
    """
    title = _(u"Flat")
    icon = None#"layout8.png"
    
    # blocks are defined by Block objects
    # parameters are: direction, (width without portlets, width with one portlet column, width with two portlet columns)
    block_definitions = [ Block(Block.VERTICAL, 
                                [24], 
                                css_classes=["layoutcolumn"],
                                ), 
                        ]
            
    show_portlets = False
