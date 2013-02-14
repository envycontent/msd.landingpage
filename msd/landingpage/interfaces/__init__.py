# -*- extra stuff goes here -*-
from carouselblockimage import ICarouselBlockImage
from carouselbanner import ICarouselBanner

from carouselblock import ICarouselBlock

from splashblock import ISplashBlock

from listingblock import IListingBlock

from highlightblock import IHighlightBlock
from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory(u"msd.landingpage")


class ILayoutView(Interface):
    """
    Marker interface which will make the view appear as the selectable landing page layout.
    
    The view class must have special class attributes describing the layout.
    """


class ILandingpageSettings(Interface):
    #messageOfTheDay = schema.TextLine(title=u"A banner message", default=u"Welcome!")

    colours = schema.List(
                title=_(u"Block Colours"),
                unique=True,
                value_type=schema.TextLine(
                            title=_(u"Colour"))
            )
            
    snippets = schema.List(
                title=_(u"Template Snippet Choice"),
                unique=True,
                value_type=schema.TextLine(
                            title=_(u"Snippet"))
            )


from landingpage import ILandingPage
from littleblock import ILittleBlock
from bigblock import IBigBlock
from highlightblock import IHighlightBlock
from searchblock import ISearchBlock
