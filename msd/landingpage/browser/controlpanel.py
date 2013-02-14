from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
    
from msd.landingpage.interfaces import ILandingpageSettings
from plone.z3cform import layout
    
class LandingpageControlPanelForm(RegistryEditForm):
	schema = ILandingpageSettings
    
LandingpageControlPanelView = layout.wrap_form(LandingpageControlPanelForm, ControlPanelFormWrapper)

