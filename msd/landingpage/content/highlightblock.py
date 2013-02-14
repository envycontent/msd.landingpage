"""Definition of the HighlightBlock content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import IHighlightBlock
from msd.landingpage.config import PROJECTNAME

from msd.landingpage.content import littleblock

HighlightBlockSchema = littleblock.LittleBlockSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.BooleanField(
        'showTitle',
        widget=atapi.BooleanWidget(
            label=_(u"Show block title?"),
            description=_(u"Untick to hide block's title"),
        ),
        default=True,
    ),
    
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
                    'source',
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

    atapi.StringField(
        'footer_link',
        widget=atapi.StringWidget(
            label=_(u"Footer link"),
            description=_(u"Link for the box footer."),
        ),

    ),

    atapi.StringField(
        'footer_title',
        widget=atapi.StringWidget(
            label=_(u"Footer title"),
            description=_(u"Title for the box footer link."),
        ),

    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

schemata.finalizeATCTSchema(HighlightBlockSchema, moveDiscussion=False)


class HighlightBlock(littleblock.LittleBlock):
    """Description of the Example Type"""
    implements(IHighlightBlock)

    meta_type = "HighlightBlock"
    schema = HighlightBlockSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getColoursVocabulary(self):
        """ Returns just the css class from the name|class colour setting"""
        colours = self.getColours()
        return [c.split("|")[2] for c in colours if c.split('|')[0] == 'highlight']


        
    def __bobo_traverse__(self, REQUEST, name):
        """Give transparent access to image scales. This hooks into the
        low-level traversal machinery, checking to see if we are trying to
        traverse to /path/to/object/image_<scalename>, and if so, returns
        the appropriate image content.
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return super(HighlightBlock, self).__bobo_traverse__(REQUEST, name)


atapi.registerType(HighlightBlock, PROJECTNAME)
