from plone.app.testing.bbb import PloneTestCaseFixture, PloneTestCase
from Products.Five import zcml
from plone.testing import z2
from plone.app import testing


zcml_string = """\
<configure xmlns="http://namespaces.zope.org/zope"
           xmlns:browser="http://namespaces.zope.org/browser"
           xmlns:plone="http://namespaces.plone.org/plone"
           xmlns:gs="http://namespaces.zope.org/genericsetup"
           package="plonetheme.sunburst"
           i18n_domain="test">

    <gs:registerProfile
        name="testing"
        title="plonetheme.sunburst testing"
        description="Used for testing only"
        directory="tests/profiles/testing"
        for="Products.CMFCore.interfaces.ISiteRoot"
        provides="Products.GenericSetup.interfaces.EXTENSION"
        />

</configure>
"""


class SunburstFixture(PloneTestCaseFixture):

    def setUpZope(self, app, configurationContext):
        super(PloneTestCaseFixture, self).setUpZope(app, configurationContext)
        import plonetheme.sunburst
        self.loadZCML(package=plonetheme.sunburst)
        z2.installProduct(app, 'plonetheme.sunburst')

    def setUpPloneSite(self, portal):
        super(PloneTestCaseFixture, self).setUpPloneSite(portal)
        # install sunburst theme
        testing.applyProfile(portal, 'plonetheme.sunburst:default')

    def tearDownZope(self, app):
        super(PloneTestCaseFixture, self).tearDownZope(app)
        z2.uninstallProduct(app, 'plonetheme.sunburst')



PTC_FIXTURE = SunburstFixture()
PTC_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(PTC_FIXTURE,), name='PloneTestCase:Functional')


class SunburstTestCase(PloneTestCase):
    """ Base class used for test cases """

    layer = PTC_FUNCTIONAL_TESTING

class FunctionalTestCase(PloneTestCase):

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = z2.Browser()
        if loggedIn:
            user = ptc.default_user
            pwd = ptc.default_password
            browser.addHeader('Authorization', 'Basic %s:%s' % (user, pwd))
        return browser
