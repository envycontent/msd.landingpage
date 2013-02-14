from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from msd.landingpage import landingpageMessageFactory as _

class ICarouselBanner(Interface):
    """A Banner for the Carousel"""
    
    # -*- schema definition goes here -*-
