from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from msd.melipona.browser.interfaces import IMeliponaLayoutPolicy
from msd.melipona.browser.layout import MeliponaLayoutPolicy

from msd.landingpage import landingpageMessageFactory as _


class LandingpageLayoutPolicy(MeliponaLayoutPolicy):
    """
    LandingpageLayout browser view
    """
    implements(IMeliponaLayoutPolicy)

    def __init__(self, context, request):
        self.context = context
        self.request = request


    def _show_portlets(self):
        if hasattr(self.context, "show_portlets"):
            #This view is only registered to ILandingPage interface so not sure if we need to check portal_type here
            if self.context.portal_type == "LandingPage" and not self.context.show_portlets():
                return False
            
        return True

    def get_content_column_class(self, column_left, column_right):
        """Get the classes for the middle column
           calculating the width from the presence of left or right cols
        """
        
        #default with no portlets
        classes = "layoutcolumn span-24"
                
        if self._show_portlets():
            if column_left and column_right:
                classes = "layoutcolumn span-12"
            elif column_left:
                classes = "last layoutcolumn span-18"
            elif column_right:
                classes = "layoutcolumn span-18"
                
        return classes
        
    def get_column_left_class(self):
        """Return classes for the left column    
        """

        return "layoutcolumn span-6"

    def get_column_right_class(self):
        """Return classes for the right column
        """

        return "last layoutcolumn span-6"
    