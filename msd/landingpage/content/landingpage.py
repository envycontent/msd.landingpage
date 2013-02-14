"""Definition of the LandingPage content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ILandingPage
from msd.landingpage.config import PROJECTNAME

from msd.landingpage.layout import Layout
from msd.landingpage.widgets.layoutselection import LayoutSelectionWidget

LandingPageSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        "blockLayout",
        vocabulary="getLayoutOptions",
        widget = LayoutSelectionWidget(
            label = _(u"Layout"),
            description="What kind of layout you wish to use on this landing page"
        )
    ),
    
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

LandingPageSchema['title'].storage = atapi.AnnotationStorage()
LandingPageSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    LandingPageSchema,
    folderish=True,
    moveDiscussion=False
)


class LandingPage(folder.ATFolder):
    """Landing page"""
    implements(ILandingPage)

    meta_type = "LandingPage"
    schema = LandingPageSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def initializeArchetype(self, **kwargs):    
        """
        Prepopulate folder during the creation.
        
        Create five subfolders of "BigBlock" type, with title and id preset.
        """
        folder.ATFolder.initializeArchetype(self, **kwargs)
        
        for i in range(0, 5):
            id = "container" + str(i)
            self.invokeFactory("BigBlock", id, title="Big block " + str(i+1))
            item = self[id]
            
            # Clear creation flag so that edit screen 
            item.markCreationFlag()
            
            
    def show_portlets(self):
        """ Returns False if current layout does not allow portlets. Otherwise True. """
        layout = self.getActiveBlockLayout()
        
        #Layout does not exist at the creation
        if layout:
            return layout.show_portlets
        else:
            return True
        
    def getLayoutOptions(self):
        """
        Populate selection list vocabulary for the edit page.
        """
        layouts = Layout.getLayouts(self, self.REQUEST)
        dl = atapi.DisplayList()
        for l in layouts:
            dl.add(l.view_name, l.title)
            
        return dl
    

    def getActiveBlockLayout(self):
        """
        @return: msd.landingpage.layout.Layout object
        """
        return Layout.getLayoutByViewName(self, self.REQUEST, self.getBlockLayout())
        
    
    def setBlockLayout(self, value):
        """
        Override block layout field mutator to do the change of actual active view also.
        """
        field = self.Schema()["blockLayout"]
        field.set(self, value)
        if value != None and value != "":
            self.setLayout(value)
    
atapi.registerType(LandingPage, PROJECTNAME)
