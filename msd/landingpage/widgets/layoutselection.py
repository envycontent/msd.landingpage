from Products.Archetypes import public as atapi 

from msd.landingpage.layout import Layout

class LayoutSelectionWidget(atapi.SelectionWidget):
    """
    """
        
    _properties = atapi.SelectionWidget._properties.copy()
    
    _properties.update({
        # Skin file used for this widget
        'macro' : "layoutselectionwidget",
        })
        
        
    def getLayoutImageSource(self, context, item):
        layout = Layout.getLayoutByViewName(context, context.REQUEST, item)
        if layout.icon:
            return context.portal_url() + "/" + layout.icon 
        else:
            return None
    