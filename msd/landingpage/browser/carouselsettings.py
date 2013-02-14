"""
We are doing lots of stuff here so we can have our own settings for the landginpage carousel.
We override banner_template vocabulary so it uses our own menu and just template registered for the carouselblock
and we also hide some of the settings we don't need. 

"""
from Products.Carousel.browser.folder import CarouselSettingsView, CarouselSettingsForm, TransitionGroup
from Products.Carousel.interfaces import ICarouselSettings, ICarousel
from Products.Carousel.browser.folder import CarouselSettings, Carousel
from zope import schema
from z3c.form import interfaces, group, field
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from zope.component import adapts
from zope.interface import implements
from zope.annotation import factory

from msd.landingpage.interfaces import ICarouselBlock
from Products.Carousel import CarouselMessageFactory as _
    
#This classname might be confusing as we have content type with same name?
class CarouselBlock(Carousel):
    implements(ICarousel)
    adapts(ICarouselBlock)

class ILandingPageCarouselSettings(ICarouselSettings):
    """
    override banner template vocabulary
    """
    
    banner_template = schema.Choice(
     title=_(u'Banner Type'),
        description=_(u'The banner is the part of the Carousel that rotates.'
            ' Choose Default for the standard Carousel banner.'),
        vocabulary='msd.landingpage.BannerTemplates',
    )
    
    
class LandingPageCarouselSettings(CarouselSettings):
    implements(ILandingPageCarouselSettings)
    adapts(ICarouselBlock)
    
    pager_template = None
    
LandingPageCarouselSettingsFactory = factory(LandingPageCarouselSettings)

class AppearanceGroup(group.Group):
    """
    Appearance options. Just so we can override banner_template vocabulary and hide some fields
    """

    label = _(u'Appearance')
    fields = field.Fields(ILandingPageCarouselSettings).select(
        'banner_template', 'banner_elements', 'width', 'height',
         'element_id')
    fields['banner_elements'].widgetFactory = CheckBoxFieldWidget
    fields["banner_template"].vocabularyName ='msd.landingpage.BannerTemplates'

class LandingPageCarouselSettingsForm(CarouselSettingsForm):
    """
    """

    groups = (AppearanceGroup, TransitionGroup,)

    def update(self):
        #First call parent's update
        super(LandingPageCarouselSettingsForm, self).update()

        #Previous update has changed groups to instances and we can update the widgets
        self.groups[0].widgets["banner_elements"].mode = interfaces.HIDDEN_MODE
        self.groups[0].widgets["width"].mode = interfaces.HIDDEN_MODE
        self.groups[0].widgets["height"].mode = interfaces.HIDDEN_MODE
        
    def getContent(self):
        return ILandingPageCarouselSettings(self.context)

        
LandingPageCarouselSettingsForm.buttons['apply'].title = u'Save'
           
class LandingPageCarouselSettingsView(CarouselSettingsView):
    """
    View for searching and filtering ATResources.
    """
    
    form = LandingPageCarouselSettingsForm
    
