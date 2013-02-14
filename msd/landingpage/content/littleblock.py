"""Definition of the LittleBlock content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ILittleBlock
from msd.landingpage.config import PROJECTNAME

LittleBlockSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.IntegerField("weight",
                       default=1,
                       widget=atapi.IntegerWidget(
                            label=_(u"Weight"),
                            description=_(u"How many units of space are reserved for this block if container is horizontal.")
                            )
            )
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

LittleBlockSchema["description"].widget.visible = { "view" : "invisible", "edit" : "invisible"}


schemata.finalizeATCTSchema(LittleBlockSchema, moveDiscussion=False)


class LittleBlock(base.ATCTContent):
    """ Abstract base class for payload blocks """
    implements(ILittleBlock)

    meta_type = "LittleBlock"
    schema = LittleBlockSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    
    def getSnippets(self):
        """ Returns site specific colours from the landingpage settings to be used as colourfield
            vocabulary """
        registry = getUtility(IRegistry)
        snippets =  registry['msd.landingpage.interfaces.ILandingpageSettings.snippets']
        return snippets
    
    
    def getColours(self):
        """ Returns site specific colours from the landingpage settings to be used as colourfield
            vocabulary """
        registry = getUtility(IRegistry)
        colours =  registry['msd.landingpage.interfaces.ILandingpageSettings.colours']
        return colours
    
    def getColoursVocabulary(self):
        """ Returns just the css class from the name|class colour setting"""
        colours = self.getColours()
        return [c.split("|")[0] for c in colours]
    
    def getColourClass(self):
        """ Returns current colour class name of the block """
        colour = self.getColour()
        
        return colour.split("|")[0]
        
# atapi.registerType(LittleBlock, PROJECTNAME)
