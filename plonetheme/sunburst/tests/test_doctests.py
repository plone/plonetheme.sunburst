import unittest
import doctest

from plone.app.testing.bbb import PTC_FUNCTIONAL_TESTING
from plone.testing import layered

optionflags = (doctest.NORMALIZE_WHITESPACE|
               doctest.ELLIPSIS|
               doctest.REPORT_NDIFF)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(layered(
        doctest.DocFileSuite('README.rst', package='plonetheme.sunburst',
                             optionflags=optionflags),
        layer=PTC_FUNCTIONAL_TESTING))
    return suite
