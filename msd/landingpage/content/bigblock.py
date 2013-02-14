"""Definition of the BigBlock content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import IBigBlock
from msd.landingpage.config import PROJECTNAME

BigBlockSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

schemata.finalizeATCTSchema(
    BigBlockSchema,
    folderish=True,
    moveDiscussion=False
)

BigBlockSchema["description"].widget.visible = { "view" : "invisible", "edit" : "invisible"}

class BigBlock(folder.ATFolder):
    """Block containing little blocks"""
    implements(IBigBlock)

    meta_type = "BigBlock"
    schema = BigBlockSchema
    # -*- Your ATSchema to Python Property Bridges Here ... -*-


    def getLayoutOptions(self):
        """
        @return: AT vocabulary to use with the widget.
        """
        
        
atapi.registerType(BigBlock, PROJECTNAME)
