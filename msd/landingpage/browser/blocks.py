"""

"""

from five import grok

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from zope.component import getMultiAdapter, queryMultiAdapter
from zope.interface import Interface
from zope.security import checkPermission

from msd.landingpage.interfaces import ILittleBlock

from lxml import html as lxml_html
from lxml import etree
import urlparse

grok.templatedir("block_templates")

grok.context(ILittleBlock)

class BaseBlockView(grok.View):
    grok.baseclass()
    
    def __init__(self, *args):
        
        super(BaseBlockView, self).__init__(*args)
        #Set defaults for width and isLast
        self.width = 18
        self.isLast = True
    
    def setUnitWidth(self, width):
        """
        @param: width = 0...24
        """
        self.width = width
    
    def getCSSClasses(self):
        """
        Generate CSS class string for this block.
        """
        return "littleblock little-block-units-" + str(self.width)
    
    def setIsLast(self, isLast):
        """
        @param: isLast = True or False
        """
        
        self.isLast = isLast
        
    @property
    def portal_state(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        
        return portal_state
    
    def showEditLink(self):
        return checkPermission('cmf.ModifyPortalContent', self.context)
    
    def getBlueprintCSSClasses(self):
        """
        Generate Blueprint CSS class string for this block
        """
        
        classes = "layoutcolumn span-" +str(self.width)
        
        if self.isLast:
            classes += " last"
            
        return classes

    def getWeightedImageUrl(self):
        """ Returns url based on the current layout of the block """
        return self.context.getImage().absolute_url()+'_image-'+str(self.width)


    def transformText(self, orig):
        """
        Transforms relative href link attributes from the given html to abslute links.
        
        @param orig String with html. Likely a body field contents from the context.
        @return: String with html where links are transformed. 
        """
        
        if orig == "":
            return orig
        
        context = aq_inner(self.context)


        if not isinstance(orig, unicode):
            # Apply a potentially lossy transformation, and hope we stored
            # utf-8 text. There were bugs in earlier versions of this portlet
            # which stored text directly as sent by the browser, which could
            # be any encoding in the world.
            orig = unicode(orig, 'utf-8', 'ignore')
            #logger.warn("Static portlet at %s has stored non-unicode text. "
            #            "Assuming utf-8 encoding." % context.absolute_url())
       
        try:
            dom = lxml_html.fromstring(orig)
        except Exception, e:
            #Change to logger instead
            print "Encountered bad html" +str(orig)
            return orig
        
        links = dom.iter("a")
        
        for link in links:
            if "href" in link.attrib and not self._is_external_link(link.attrib["href"]):
                href = link.attrib["href"]    
                link.attrib["href"] = urlparse.urljoin(context.absolute_url(), href)
                
        images = dom.iter("img")
        
        for image in images:
            if "src" in image.attrib and not self._is_external_link(image.attrib["src"]):
                src = image.attrib["src"]
                image.attrib["src"] = urlparse.urljoin(context.absolute_url(), src)
                
        transformed = etree.tostring(dom, encoding="UTF-8")
        
        return transformed

    def _is_external_link(self, link):
        """
        Returns true if link is external (has // in it)
        """
        return "//" in link

    
    def transformUIDLinks(self, original):

        """
        Use this instead of transformText if you are using Plone 4 with UID links.
        
        Use the safe_html transform to protect text output. This also
        ensures that resolve UID links are transformed into real links.
        
        Check static.py from plone.portlet.static for original method (transformed in Renderer class)
        """       
        
        context = aq_inner(self.context)
        
        if not isinstance(original, unicode):
            # Apply a potentially lossy transformation, and hope we stored
            # utf-8 text. There were bugs in earlier versions of this portlet
            # which stored text directly as sent by the browser, which could
            # be any encoding in the world.
            original = unicode(original, 'utf-8', 'ignore')
            #logger.warn("Static portlet at %s has stored non-unicode text. "
            #            "Assuming utf-8 encoding." % context.absolute_url())

        # Portal transforms needs encoded strings
        original = original.encode('utf-8')

        transformer = getToolByName(context, 'portal_transforms')
        data = transformer.convertTo("text/x-html-safe", original,
                                     context=context, mimetype='text/html')
        result = data.getData()
        if result:
            return unicode(result, 'utf-8')
        
        #I think we rather send original text than None?
        #return None
        return original
        

class HighlightBlock(BaseBlockView):
    """
    """    
    
    def update(self):
        pass

class SearchBlock(BaseBlockView):
    """
    """    
    
    def update(self):
        context = aq_inner(self.context)
        mode = int(context.getSearch_mode())
        self.config = {'mode': mode}
        
        if mode == 0: # browse mode
            criteria = {}
            catalog = getToolByName(context, 'portal_catalog')
            for crt in context.getBrowse_criteria():
                value = crt['b_value']
                if value in ['True', 'False']:
                    value = eval(value)
                criteria[crt['b_key']] = value
            brains = catalog(**criteria)

            self.config['urls'] = [{
                    'link': brain.getURL(),
                    'title': brain.Title
                    } for brain in brains]

            self.config['label'] = context.getBrowse_label()

        elif mode == 1: #search mode
            field_name = context.getSearch_field_name()
            self.config['criteria'] = context.getSearch_criteria()
            self.config['label'] = context.getSearch_label()
            self.config['field_name'] = field_name
            self.config['unique_id'] = context.getUnique_id()
            self.config['form_name'] = '%s%sForm' % (context.getId(), field_name)
            self.config['form_action'] = context.getSearch_url()
            self.config['form_class'] = context.getForm_class()
            self.config['search_button'] = context.getSearch_button()
            self.config['search_link_class'] = context.getSearch_link_class()
    
class SplashBlock(BaseBlockView):
    """
    """    

    def update(self):
        pass

        
class ListingBlock(BaseBlockView):
    """
    """
    
    def update(self):
        pass
        
    
    def results(self):
        results = self.context.queryCatalog()
#        print results
        return results
        

from Products.Carousel.config import CAROUSEL_ID
from Products.Carousel.interfaces import ICarousel, ICarouselSettings
from Products.Carousel.browser import folder
from Acquisition import aq_base

from zope.annotation import factory
from zope.component import adapts
from zope.interface import implements

#class CarouselBlockAdapter(folder.Carousel):
#    implements(ICarousel)
#    adapts(ILittleBlock)
# 
#class CarouselBlockSettings(folder.CarouselSettings):
#    """
#    Settings for a Carousel instance.
#    """
#    implements(ICarouselSettings)
#    adapts(ILittleBlock)   
#
#CarouselSettingsFactory = factory(CarouselBlockSettings)
   
class CarouselBlock(BaseBlockView):            

    def _template_for_carousel(self, name, carousel):
        """
        Returns a template for rendering the banners or pager.
        
        Copy of Products.Carousel.browser.viewlet code
        """
        
        template = queryMultiAdapter(
            (carousel, self.request),
            Interface,
            default=None,
            name=name.replace('@@', '')
        )
        
        if template:
            return template.__of__(carousel)

        return None
    
    def getCSSClasses(self):
        """ Add template name to the extra classes """
        base = super(CarouselBlock, self).getCSSClasses()
        
        return base+" "+ICarousel(self.context).getSettings().banner_template.strip("@@")
    
    def update(self):
        """
        Set the variables needed by the template.
        
        This is copy of Products.Carousel.browser.viewlet code with some modifications
        """
        
        self.available = False
        
        context_state = self.context.restrictedTraverse('@@plone_context_state')
        if context_state.is_structural_folder() and not context_state.is_default_page():
            folder = self.context
        else:
            folder = context_state.parent()
                
        #No need for these
        #if hasattr(aq_base(folder), CAROUSEL_ID):
        #   carousel = ICarousel(folder[CAROUSEL_ID])
        #else:
        #    return
        
        carousel = ICarousel(folder)
        settings = carousel.getSettings()

        if not settings.enabled:
            return
            
        banners = carousel.getBanners()

        if not banners:
            return

        self.banners = self._template_for_carousel(
            settings.banner_template or u'@@banner-default',
            carousel
        )
        
        self.pager = self._template_for_carousel(
            settings.pager_template or u'pager-none',
            carousel
        )
        #Antti's addition
        # this sets the width to the width of the image
        imagewidth, imageheight = banners[0].getSize(scale='image-'+str(self.blockWidth()))
        
        settings.width = imagewidth
        settings.height = imageheight
        self.height = settings.height or 0
        #self.width = settings.width or 0
        #self.containerwidth = containerwidth or 0
        self.transition = settings.transition_type
        self.speed = int(settings.transition_speed * 1000)
        self.delay = int(settings.transition_delay * 1000)
        self.element_id = settings.element_id
        
        #Template will throw error when scaling image if either one of these is 0
        if settings.width == 0 or settings.height == 0:
            self.available = False
        else:
            self.available = True
            
    def results(self):
        results = self.context.getFolderContents()
        
        return results
        
    def snippet(self):
    
        return 1
        
    def blockWidth(self):
        return self.width
