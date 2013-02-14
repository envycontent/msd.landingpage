"""

    Layout definitions.

"""

from zope.publisher.interfaces.browser import IBrowserView
from zope.component import queryMultiAdapter, getAdapters

from msd.landingpage.interfaces import ILayoutView


class Block(object):
    """
    Describe one big block in the layout definition.
    """
    
    
    # Pseudo-constants defining block direciton
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    # Different layout cases with portlet combinations
    # This maps to widths and css classes array index
    CASE_NO_PORTLETS = 0
    CASE_ONE_PORTLET_COLUMN = 1
    CASE_TWO_PORTLET_COLUMNS = 2

    def __init__(self, direction, widths=[], css_classes=[],):
        """
        
        @param direction: "vertical" or "horizontal"
        @param widths: Block with under following conditions: (no portlets, one portlet column, two portlet colums)
        @param css_classes: CSS classes applied for the block in different cases
        """
        self.direction = direction
        self.widths = widths
        self.css_classes = css_classes

    def getWidthInCase(self, case):
        """
        @param case: One of PORTLETS pseudoconstants
        """
        if case < len(self.widths):
            return self.widths[case]
        else:
            return 0

    def getCSSClassInCase(self, case):
        """
        @param case: One of PORTLETS pseudoconstants
        """
        if case < len(self.css_classes):
            return self.css_classes[case]
        else:
            return None
        
        
class Layout(object):
    """
    Define a layout properties.
    """
    
    def __init__(self, id, view_name, title, icon, blocks, show_portlets):
        """
        
        @param id:
        @param title: Translatable title
        @param icon: Icon used to symbolize layout, as site root relative image URI
        @param blocks: List of Block instances 
        @param show_portlets: Does this layout allow left and right portlet managers
        """
        self.id = id
        self.view_name = view_name
        self.title = title
        self.icon = icon
        
        self.blocks = blocks        
        self.show_portlets = show_portlets
        
    def getBlock(self, index):
        if index < len(self.blocks):
            return self.blocks[index]
        else:
            return None

    @staticmethod
    def getLayouts(context, request):
        """
        @return: List of Layout objects.
        """
               
        from plone.app.customerize import registration
        from zope.publisher.interfaces.browser import IBrowserView
        from zope.publisher.interfaces.browser import IBrowserRequest
        
        views = registration.getViews(IBrowserRequest)
        views = [ view for view in views if ILayoutView.implementedBy(view.factory) ] 
        
        def constructLayout(view):
            """
            Extract layout definition from class attributes
            """
            icon = getattr(view.factory, "icon", None)
            
            # default title to class name if not present
            title = getattr(view.factory, "title", view.name)
            blocks = getattr(view.factory, "block_definitions", [])
            show_portlets = getattr(view.factory, "show_portlets", True)
            
            return Layout(view.name, 
                          view.name, 
                          title, 
                          icon, 
                          blocks, 
                          show_portlets)
        
        # Do not include abstract base class in the available view list
        return [ constructLayout(view) for view in views ]    
        

    @staticmethod
    def getLayoutByViewName(context, request, name):
        """ Resolve active view to Layout object defining it.
        """
        layouts = Layout.getLayouts(context, request)
        for l in layouts:
            if l.view_name == name:
                return l
        return None
        