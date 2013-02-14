## Script (Python) "testForWidth"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=sl, sr
##title=
##



#Landing page specific check if it does not allow portlets use span-24
if hasattr(context, "show_portlets"):
    if context.portal_type == "LandingPage":
        if not context.show_portlets():
            return "layoutcolumn span-24"

if sl and sr:
    return "layoutcolumn span-12"
if sl:
    return "last layoutcolumn  span-18"
if sr:
    return "layoutcolumn span-18"
return "layoutcolumn span-24"