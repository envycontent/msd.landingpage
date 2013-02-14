"""Definition of the CarouselBlock content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ICarouselBlock
from msd.landingpage.config import PROJECTNAME


from zope.component import getUtility
from plone.registry.interfaces import IRegistry


from msd.landingpage.content import littleblock

CarouselBlockSchema = folder.ATFolderSchema.copy() \
                      + littleblock.LittleBlockSchema.copy() \
                      + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
   

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.


schemata.finalizeATCTSchema(
    CarouselBlockSchema,
    folderish=True,
    moveDiscussion=False
)

from Products.Carousel.interfaces import ICarouselFolder
from Products.Carousel.utils import addPermissionsForRole

class CarouselBlock(folder.ATFolder, littleblock.LittleBlock):
    """A slideshow type block"""
    implements(ICarouselBlock, ICarouselFolder)

    meta_type = "CarouselBlock"
    schema = CarouselBlockSchema
    
    def initializeArchetype(self, **kwargs):
        """
        Set permissions so Carousel Banners can be added to this Block
        """
        folder.ATFolder.initializeArchetype(self, **kwargs)

            # make sure Carousel banners are addable within the new folder
        addPermissionsForRole(self, 'Manager', ('Carousel: Add Carousel Banner',))
        
        # make sure *only* Carousel banners are addable
        self.setConstrainTypesMode(1)
        self.setLocallyAllowedTypes(['CarouselBlockImage'])
        self.setImmediatelyAddableTypes(['CarouselBlockImage'])
           
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(CarouselBlock, PROJECTNAME)
