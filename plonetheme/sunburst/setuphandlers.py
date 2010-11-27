from Products.CMFCore.utils import getToolByName

def importVarious(context):
    # Make sure this import step only runs for the sunburst profile.
    if context.readDataFile('sunburst.txt') is None:
        return
    
    # Copy the plone_setup action to the user category
    atool = getToolByName(context.getSite(), 'portal_actions')
    cp = atool.site_actions.manage_copyObjects(['plone_setup'])
    atool.user.manage_pasteObjects(cp)
    
    position = atool.user.getObjectPosition('preferences') + 1
    atool.user.moveObjectToPosition('plone_setup', position)

    atool.user.plone_setup.visible = True