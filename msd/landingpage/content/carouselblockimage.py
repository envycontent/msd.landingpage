"""Definition of the CarouselBlockImage content type
"""

from zope.interface import implements

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
    
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.ATContentTypes.configuration import zconf
from Products.validation import V_REQUIRED

from Products.Carousel.content.carouselbanner import CarouselBanner, CarouselBannerSchema

from Products.Carousel import CarouselMessageFactory as _
# -*- Message Factory Imported Here -*-

from msd.landingpage.interfaces import ICarouselBlockImage
from msd.landingpage.config import PROJECTNAME

CarouselBlockImageSchema = CarouselBannerSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.ImageField('image',
        required = False,
        storage = atapi.AnnotationStorage(),
        languageIndependent = True,
        max_size = zconf.ATNewsItem.max_image_dimension,
        original_size=(964,2000),
        sizes={
                'image-2': (103, 2000),
                'image-3': (103, 2000),
                'image-4': (144, 2000),
                'image-5': (185, 2000),
                'image-6': (226, 2000),
                'image-7': (267, 2000),
                'image-8' : (308, 2000),
                'image-9' : (349, 2000),
                'image-10': (390, 2000),
                'image-11': (431, 2000),
                'image-12' : (472, 2000),
                'image-13' : (513, 2000),
                'image-14' : (554, 2000),
                'image-15' : (595, 2000),
                'image-16' : (636, 2000),
                'image-17' : (677, 2000),
                'image-18' : (718, 2000),
                'image-19' : (759, 2000),
                'image-20' : (800, 2000),
                'image-21' : (841, 2000),
                'image-22' : (882, 2000),
                'image-23' : (923, 2000),
                'image-24' : (964, 2000)
              },
        validators = (('isNonEmptyFile', V_REQUIRED),
          ('checkNewsImageMaxSize', V_REQUIRED)),
        widget = atapi.ImageWidget(
            description = _(u'This image will be shown when this banner is active.'),
            label= _(u'Image'),
            show_content_type = False)
        ),
        

))

schemata.finalizeATCTSchema(CarouselBlockImageSchema, moveDiscussion=False)


class CarouselBlockImage(CarouselBanner):
    """Banner image used in the CarouselBlock"""
    implements(ICarouselBlockImage)

    meta_type = "CarouselBlockImage"
    schema = CarouselBlockImageSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getSpanSize(self, width):
        """ returns correct span size using image fields sizes based on the given width in pixels 
            @width: Width in pixels
            @return: one of the image sizes defined in the schema as int (image-8 returns 8 and so on). If not found returns 
            size that is biggest possible but smaller than wanted size
        """
        sizes = self.schema["image"].sizes
        
        aboutSize = 0
        
        for size in sizes.iteritems():
            if size[1][0] == width:
                return int(size[0].strip("image-"))
            elif size[1][0] < width:
                s = int(size[0].strip("image-"))
                if s > aboutSize:
                    aboutSize = s

        return aboutSize

atapi.registerType(CarouselBlockImage, PROJECTNAME)
