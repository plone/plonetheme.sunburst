from Testing.ZopeTestCase import Sandboxed

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase.PloneTestCase import installPackage
from Products.Five.testbrowser import Browser
from Products.PloneTestCase import PloneTestCase as ptc

from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer

class Layer(BasePTCLayer):
    """ set up basic testing layer """

    def afterSetUp(self):
        # load zcml for this package and its dependencies
        fiveconfigure.debug_mode = True
        from plonetheme import sunburst
        zcml.load_config('configure.zcml', package=sunburst)
        fiveconfigure.debug_mode = False
        # after which the required packages can be initialized
        installPackage('plonetheme.sunburst', quiet=True)
        # finally load the testing profile
        self.addProfile('plonetheme.sunburst:default')

layer = Layer(bases=[ptc_layer])

ptc.setupPloneSite()

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

class SunburstTestCase(Sandboxed, ptc.PloneTestCase):
    """ Base class used for test cases """

    layer = layer

class FunctionalTestCase(ptc.FunctionalTestCase):

    layer = layer

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            user = ptc.default_user
            pwd = ptc.default_password
            browser.addHeader('Authorization', 'Basic %s:%s' % (user, pwd))
        return browser
