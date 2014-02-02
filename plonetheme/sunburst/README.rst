Detailed documentation
======================

Set up and log in
-----------------

    >>> from plone.testing import z2
    >>> browser = z2.Browser(layer['app'])
    >>> browser.handleErrors = False
    >>> portal = layer['portal']
    >>> portal_url = portal.absolute_url()
    >>> portal.error_log._ignored_exceptions = ()
    >>> from plone.app.testing import SITE_OWNER_NAME
    >>> z2.login(layer['app']['acl_users'], SITE_OWNER_NAME)

Example portlet
    >>> from zope.component import getUtility
    >>> from plone.portlets.interfaces import IPortletType
    >>> portlet = getUtility(IPortletType, name='portlets.Search')

Sunburst view
-------------

Sunburst ships with a special main view similar to ploneview. It contains
helping methods relevant to the Sunburst theme only so it doesn't make sense
to put these into global ploneview.

First let's check that the view exists

    >>> from plonetheme.sunburst.browser.sunburstview import SunburstView
    >>> view = SunburstView(portal, layer['request'])


getColumnsClass()
*****************

The getColumnsClass() method of SunburstView class returns CSS class based on
existence of the columns. This class is applied to
<div id="portal-column-content">.

No columns
~~~~~~~~~~

Originally on a fresh site we don't have portlets on the top level
(login portlet has been disabled in Plone 4) and thus we should not
have any columns.

    >>> browser.open('http://nohost/plone/front-page')
    >>> 'id="portal-column-one"' not in browser.contents
    True
    >>> 'id="portal-column-two"' not in browser.contents
    True

In this case content column should take the whole width of the site

    >>> '<div id="portal-column-content" class="cell width-full position-0"' in browser.contents
    True

Left column only
~~~~~~~~~~~~~~~~

First we need to add a portlet that would definitely be visible. So let's add
the search portlet via it's addview.

    >>> mapping = portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
    >>> addview = mapping.restrictedTraverse('+/' + portlet.addview)
    >>> result = addview.createAndAdd({})
    >>> bool(result)  # None or empty string
    False
    >>> import transaction
    >>> transaction.commit()
    >>> browser.reload()

In this case we should have the left column.

    >>> 'id="portal-column-one"' in browser.contents
    True
    >>> 'id="portal-column-two"' not in browser.contents
    True

And the class on id="portal-column-content" is changed

    >>> '<div id="portal-column-content" class="cell width-3:4 position-1:4"' in browser.contents
    True

Now we switch from English to an RTL language. Hebrew for example.

    >>> from Products.CMFCore.utils import getToolByName
    >>> tool = getToolByName(portal, "portal_languages")
    >>> tool.getDefaultLanguage()
    'en'
    >>> tool.setDefaultLanguage('he')
    >>> transaction.commit()

Changes aren't pick up immediately. We need to reload

    >>> 'dir="rtl"' in browser.contents
    False
    >>> browser.reload()
    >>> 'dir="rtl"' in browser.contents
    True

And the class on id="portal-column-content" should be changed as well

    >>> '<div id="portal-column-content" class="cell width-3:4 position-0"' in browser.contents
    True

Both columns
~~~~~~~~~~~~

Now lets add a Search portlet to the right column also to have both columns
populated and visible.

    >>> mapping = portal.restrictedTraverse('++contextportlets++plone.rightcolumn')
    >>> addview = mapping.restrictedTraverse('+/' + portlet.addview)
    >>> result = addview.createAndAdd({})
    >>> bool(result)  # None or empty string
    False
    >>> transaction.commit()
    >>> browser.reload()

In this case we should have both columns visible.

    >>> 'id="portal-column-one"' in browser.contents
    True
    >>> 'id="portal-column-two"' in browser.contents
    True

And the class on id="portal-column-content" is changed

    >>> '<div id="portal-column-content" class="cell width-1:2 position-1:4"' in browser.contents
    True

Right column only
~~~~~~~~~~~~~~~~~

Now let's get rid of the left column in order to have only the right column
visible.

    >>> mapping = portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
    >>> del mapping['search']
    >>> transaction.commit()

    >>> browser.reload()
    >>> 'id="portal-column-one"' in browser.contents
    False
    >>> 'id="portal-column-two"' in browser.contents
    True

And now we check id="portal-column-content". Since we are still in 'he'
language...

    >>> tool.getDefaultLanguage()
    'he'

... content column should start not from the left, but rather from
position-1:4 (1:4 on the left is taken by the right column in RTL)

    >>> '<div id="portal-column-content" class="cell width-3:4 position-1:4"' in browser.contents
    True

Now we switch language back to 'en' and our content should start at position-0
when there is no left column

    >>> tool.setDefaultLanguage('en')
    >>> transaction.commit()

Changes aren't pick up immediately. We need to reload

    >>> 'dir="ltr"' in browser.contents
    False
    >>> browser.reload()
    >>> 'dir="ltr"' in browser.contents
    True

And the class on id="portal-column-content" should be changed as well

    >>> '<div id="portal-column-content" class="cell width-3:4 position-0"' in browser.contents
    True
