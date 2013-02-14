"""Definition of the ListingBlock content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import topic

from zope.component import getUtility
from plone.registry.interfaces import IRegistry


from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import IListingBlock
from msd.landingpage.config import PROJECTNAME

from msd.landingpage.content import littleblock


ListingBlockSchema = topic.ATTopicSchema.copy() + littleblock.LittleBlockSchema.copy () + atapi.Schema((


    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        'link',
        widget=atapi.StringWidget(
            label=_(u"Link"),
            description=_(u"Link for title and read more. http://www.google.com"),
        ),
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
        'snippet',
        widget=atapi.SelectionWidget(
            label=_(u"Template Snippet"),
            description=_(u"Template snippet for the box"),
            format='select',
        ),
        vocabulary="getSnippetsVocabulary",
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.
ListingBlockSchema["text"].widget.visible = { "view" : "invisible", "edit" : "invisible"}
ListingBlockSchema["customView"].widget.visible = { "view" : "invisible", "edit" : "invisible"}
ListingBlockSchema["customViewFields"].widget.visible = { "view" : "invisible", "edit" : "invisible"}


schemata.finalizeATCTSchema(ListingBlockSchema, moveDiscussion=False)

class ListingBlock(topic.ATTopic, littleblock.LittleBlock):
    """A Listing Block - works like a collection"""
    implements(IListingBlock)

    meta_type = "ListingBlock"
    schema = ListingBlockSchema
    
   
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    
    def getSnippetsVocabulary(self):
        """ Returns just the css class from the name|class colour setting"""
        colours = self.getSnippets()
        return [c.split("|")[2] for c in colours if c.split('|')[0] == 'listing']

    def getColoursVocabulary(self):
        """ Returns just the css class from the name|class colour setting"""
        colours = self.getColours()
        return [c.split("|")[2] for c in colours if c.split('|')[0] == 'highlight']
    

atapi.registerType(ListingBlock, PROJECTNAME)
