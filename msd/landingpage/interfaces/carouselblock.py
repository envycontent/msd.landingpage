from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from msd.landingpage import landingpageMessageFactory as _

class ICarouselBlock(Interface):
    """A slideshow type block"""
    
    # -*- schema definition goes here -*-
