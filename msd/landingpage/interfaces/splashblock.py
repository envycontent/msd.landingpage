from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from msd.landingpage import landingpageMessageFactory as _

class ISplashBlock(Interface):
    """A Splash Box"""
    
    # -*- schema definition goes here -*-
