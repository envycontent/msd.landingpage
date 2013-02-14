"""Definition of the SplashBlock content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ISplashBlock
from msd.landingpage.config import PROJECTNAME

from msd.landingpage.content import littleblock

SplashBlockSchema = littleblock.LittleBlockSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
        atapi.TextField(
            "body",
            allowable_content_types=('text/html',),
            default_output_type='text/html',
            widget=atapi.RichWidget(
                    label=_("Body text"),
                    allow_buttons=(
                        'bg-basicmarkup',
                        'bold-button',
                        'italic-button',
                        'bg-drawers',
                        'linklibdrawer-button',
                        'linkdrawer-button',
                        'bg-list',
                        'list-ul-addbutton',
                        ),
                    )
            ),

        atapi.StringField(
            'colour',
            widget=atapi.SelectionWidget(
                label=_(u"Colour"),
                description=_(u"Styling colour for the box"),
                format='select',
            ),
            vocabulary="getColoursVocabulary",
        ),

        atapi.StringField(
            'link',
            widget=atapi.StringWidget(
                label=_(u"Link"),
                description=_(u"Link for image and title. http://www.google.com"),
            ),

        ),
        atapi.ImageField(
            'image',
            widget=atapi.ImageWidget(
                label=_(u"Image"),
                description=_(u"Image for the block"),
            ),
            validators=('isNonEmptyFile'),
            required=False,
            original_size=(964,2000),
            sizes={
                    'image-6': (226,2000),
                    'image-8' : (308,2000),
                    'image-9' : (349,2000),
                    'image-12' : (472,2000),
                    'image-16' : (636,2000),
                    'image-18' : (718,2000),
                    'image-24' : (964,2000)
                  }

        ),
    ))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.


schemata.finalizeATCTSchema(SplashBlockSchema, moveDiscussion=False)

class SplashBlock(littleblock.LittleBlock):
    """A Splash Box"""
    implements(ISplashBlock)

    meta_type = "SplashBlock"
    schema = SplashBlockSchema

    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(SplashBlock, PROJECTNAME)
