from zope.component import queryMultiAdapter
        
def getViewForLittleBlock(request, block):
    """
    
    @param block: Archetypes block content object
    """

    # TextBox -> textbox
    block_name = block.portal_type.lower()
    
    view = queryMultiAdapter((block, request), name=block_name)  
    if view == None:
        raise RuntimeError("No block view for " + str(block) + " view name:" + str(block_name))
    
    return view