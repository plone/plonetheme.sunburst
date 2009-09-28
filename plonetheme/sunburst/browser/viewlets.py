from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase, PersonalBarViewlet

class NewPersonalBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile('templates/personal_bar.pt')
