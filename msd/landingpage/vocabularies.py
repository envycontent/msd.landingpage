from zope.interface import implements
from zope.app.publisher.interfaces.browser import IBrowserMenu
from zope.component import getUtility
from zope.schema.vocabulary import SimpleVocabulary
from Products.Carousel.vocabularies import getContext, uniqueMenuItems
from Products.Carousel.vocabularies import DummyCarouselFolder
    
def getPageBannerTemplates(context):
    context = getContext(context)
    menu = getUtility(IBrowserMenu, name='carouselblock_bannertemplates')
    items = menu.getMenuItems(DummyCarouselFolder(), context.REQUEST)
    return SimpleVocabulary.fromItems(uniqueMenuItems(items, 'Default'))