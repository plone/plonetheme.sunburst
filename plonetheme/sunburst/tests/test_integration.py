# Testing basic integration of the package into Plone

from zope.component import getUtility

from plone.portlets.interfaces import IPortletType

from plonetheme.sunburst.tests.base import SunburstTestCase as TestCase

class SunburstTestCase(TestCase):

    def test_sunburst_layers_available(self):
        self.failUnless('sunburst_images' in self.portal.portal_skins.objectIds())
        self.failUnless('sunburst_js' in self.portal.portal_skins.objectIds())
        self.failUnless('sunburst_styles' in self.portal.portal_skins.objectIds())
        self.failUnless('sunburst_templates' in self.portal.portal_skins.objectIds())                        
        
    def test_sunburst_skin_installed(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        self.failUnless(theme == 'Sunburst Theme', 'Default theme is %s' % theme)

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)