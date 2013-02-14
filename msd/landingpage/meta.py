from zope.interface import Interface
from zope.app.publisher.browser.viewmeta import _handle_menu
from zope.configuration.fields import GlobalInterface, Path, MessageID
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import TextLine
from Products.Five.browser.metaconfigure import page
from msd.landingpage.interfaces import ICarouselBlock

from Products.Carousel.interfaces import ICarousel


def banner(_context, name, template, title, layer=IDefaultBrowserLayer):
    """
    Registers a banner template for use with CarouselBlock.
    """
    page(_context, name, 'zope.Public', ICarousel, layer=layer,
        template=template)
    menu = _context.resolve('zope.app.menus.carouselblock_bannertemplates')
    _handle_menu(_context, menu, title, 
        [ICarousel], name, 'zope.Public', layer)