Changelog
=========


1.4.8 (2017-08-14)
------------------

New features:

- Add data-base-url attribute in body tag.
  Closes `issue 2051 <https://github.com/plone/Products.CMFPlone/issues/2051>`_
  [rodfersou]


1.4.7 (2014-09-07)
------------------

- Add some missing WYSIWIG/editor styles to the Static Text Portlet.
  [rpatterson]


1.4.6 (2014-02-19)
------------------

- Update README.rst to point to correct file for updating portal_css.
  [aclark]

- Use nocall when referencing site_properties for a mini optimization.
  [tomgross]

- Clarify documentation about registration of the skins layer.
  [thet]


1.4.5 (2013-08-14)
------------------

- Fix tests to pass on Plone 4.4 (which currently has a Calendar
  portlet on the right by default) and keep them running on 4.3 too.
  [maurits]

- Make portal messages display correctly (colors).
  https://dev.plone.org/ticket/13658
  [gbastien]


1.4.4 (2013-06-13)
------------------

- fix green line showing under current select for green bar items in Firefox,
  Checked in Firefox, Chrome and IE8.
  [gbastien, vangheem]


1.4.3 (2013-05-30)
------------------

- Revert dashboard permission change from 1.4.2. The dashboard works best when
  editable - linking to an uneditable dashboard should not be default.
  [danjacka]


1.4.2 (2013-05-23)
------------------

- Remove font-weight bold for monthdays and font-weight normal for table header
  in portlet calendar. Set div.portletCalendar with to auto instead of
  unnecessary 100% + margin.
  [thet]

- Users only require dashboard view - not edit - permission to get a 'Dashboard'
  link in the actions menu.
  [danjacka]


1.4.1 (2013-03-05)
------------------

- fix navigation items having more height than bar in chrome
  [vangheem]

- fix green line showing under current select for green bar items in chrome
  [vangheem]

- change line height of listing table class to only apply to folder contents
  listing where it's affected instead of it applying to styles globally.
  fixes #13420
  [vangheem]

- More cleanup. Move following remaining portlet styles out of public.css:
  - Dashboard styles to member.css,
  - Portlet management styles to controlpanel.css,
  - Other portlet styles to portlet.css.
  [thet]


1.4 (2013-01-17)
----------------

- Move documentation from .txt to .rst files for ReST syntax highlighting.
  [thet]

- Move workflow color definition for state "published" to public.css. The
  "published" color definition is propably something to be excluded with
  public.css in custom designs to avoid coloring of all normally visible links.
  [thet]

- Seperate css rules based on @group hints to dedicated, already existing files
  and leave only Sunburst design-specific styles in public.css. This way, your
  own theme can depend on Sunburst but exclude the public.css file, which leads
  to way less style overrides while still having a Plone-like user interface
  (edit-bars, tables, forms, etc). Fixes pull-requests #1 and #2. Upgrade step
  included (upgrade_step_2_3).
  [thet, TH-code]


1.3.1 (2013-01-01)
------------------

- Apply .portalMessage styling to reST admonitions
  https://github.com/plone/plonetheme.sunburst/pull/4
  [rpatterson]

- style reset on th for table.plain and IE9, fixes #11589
  [maartenkling]

- more specific Sunburst CSS on content-core dd, fixes #11840
  [maartenkling]


1.3.0 (2012-10-16)
------------------

- Style #ajax-spinner rather than inserting #kss-spinner in main_template.
  [davisagli]

- Style fixes for new style of portlet manager buttons.
  [vangheem]


1.2.7 (2012-08-11)
------------------
- fixes: Display menu falls under footer (see Events page) (IE7)
  [maartenkling]

- fixes: Live search appears under content action menu (IE7)
  [maartenkling]

- style ol/li in statictext portlet having omit border true
  [maartenkling]

- Fixes: in overlays, and especially in reference browser,
  label in an anchor link has a cursor pointer.
  Improves navigation experience in reference browser widget.
  [thomasdesvenain]

- Fixes: compare previous link margin with history records
  is smaller.
  [thomasdesvenain]

- Fixes and improvements on history popup with diff.
  [thomasdesvenain]

- Move new CSS class generation into new function called ``getColumnClasses``
  to let the old and deprecated one return column content CSS class only. This
  is important to keep all previously customized main_templates working.
  [saily]


1.2.6 (2012-06-29)
------------------

- Use sunburst_view to generate portal-column-one and portal-column-two
  classes as it is already done for portal-column-content.
  Fixes: https://dev.plone.org/ticket/12995
  [saily]


1.2.5 (2012-05-25)
------------------
- For event view template, changed headerless table to headings and divs for better accessibility. See bug #13181
  [hmharter]

- define class .breadcrumbSeparator, which is referred to in plone.app.layout
  and plone.app.search, but wasn't in Sunburst. Set a color on it, because
  the separator character was changed (see https://dev.plone.org/ticket/12904)
  The color chosen is WCAG2.0 compliant in contrast.
  [polyester]

- Set "display: block; font-weight:normal" on .formHelp in forms.css.dtml to
  assure that field help displays well even if it is formatted as a span
  inside the label for accessibility.
  [smcmahon]

- Change form tab style selectors from '#content' to '#content-core' so form
  tabs work in both content and overlays.
  [davidjb]

- Fix vertical alignment of listing table cells when content type icons are
  enabled.
  [esteele]


1.2.4 (2012-05-07)
------------------

- Add selector for AT required field icon
  [tom_gross]

- Use CSS :content selector to inject required icon instead of image
  [tom_gross]

1.2.3 (2012-04-15)
------------------

- Move .row and .cell styles from footer.pt to Sunburst main_template.
  Fixes https://dev.plone.org/ticket/12156
  [agnogueira]

- fix 'device-width;" for key "width" not recognized in chrome' in javascript console
  [eleddy]

- Fix view windw error in chrome
  [plone konferenz coding dojo]


1.2.2 (2012-02-07)
------------------

- Fix the styling of the standalone @@historyview view used when
  overlays are turned off.
  [rossp]


1.2.1 (2011-08-25)
------------------

- Put #search-results-bar on a lower CSS layer to not overlap the livesearch
  [spliter]

1.2 - 2011-07-19
----------------

- Switch to HTML5 doctype. References http://dev.plone.org/plone/ticket/11300
  [spliter]

- Deprecated iefixes.js and IEFixes.css after we have introduced Modernizr.
  References http://dev.plone.org/plone/ticket/11300
  [spliter]

- Merge PLIP 9352.
  [esteele]

- Applied styles for search filter on search results page.
  References http://dev.plone.org/plone/ticket/9352
  [spliter]

1.1.5 - 2011-07-04
------------------

- Fixed IE8 issue where a ghost top-margin would appear above the
  headline in the folder summary listing.
  [malthe]

- Add shadow and border for iframe overlays to match images and ajax overlays.
  [smcmahon]

- Fixed: portal footer is in a 'row' div.
  [thomasdesvenain]

- Clean up HTML comments in main_template.
  [davisagli]

- Add ids on content core viewlet managers.
  [thomasdesvenain]

- Fixed: siteactions background-color was applied to whole page.
  Add a clear: left.
  [thomasdesvenain]

- Add IEFixes.css to CSS registry in case plonetheme.classic is not installed.
  [elro]

- Removed comment in IEFixes.css concerning the now removed IE8.js.
  [elro]

- Fixed: spinner is back in main_template.
  [thomasdesvenain]

1.1.4 - 2011-05-13
------------------

- Add styling for dragdropreorder.js.
  [elro]

1.1.3 - 2011-05-12
------------------

- Add styling for z3cform multi-widget.
  [elro]

- Optimize images and icon file sizes.
  [hannosch]

- Updated base_properties values with new sunburst theme CSS values.
  [thomasdesvenain]

- Removed `clear:both` on `.image-left` and `.image-right` rules.
  [vincentfretin]

- Add MANIFEST.in.
  [WouterVH]


1.1.2 - 2011-03-02
------------------

- Make text input fields have a default width of 20em when no size is set.
  [elro]

- Hide plone.app.discussion comment viewlet from print.
  [timo]


1.1.1 - 2011-02-10
------------------

- Renamed options box in IEFixes for keyword multiple select enhancement PLIP.
  Refs http://dev.plone.org/plone/ticket/11017.
  [rmattb]


1.1 - 2011-02-04
----------------

- Merge PLIP 11017: Tags MultiSelectionWidget w/scrollbar & checkboxes.
  [esteele]


1.0.6 - 2011-01-18
------------------

- Adjust the new setuphandler introduced in 1.0.5 to avoid using copy/paste,
  which introduced unwanted additional security checks.
  [hannosch]

- Tightened selector for error fields to avoid z3cform inner div.error.
  [elro]

- Added styling for z3cform title and description fields.
  [elro]


1.0.5 - 2011-01-04
------------------

- Added iframe to style reset.
  [elro]

- Added ajax_include_head request parameter for use with cross domain iframe.
  [elro]

- Copy the plone_setup action to the user action category via a custom
  setuphandler rather than in actions.xml, so that we don't have to hardcode
  the various action settings here.  This provides forward compatibility with
  Plone 4.1, where the URL and permission change.
  [davisagli]

- Fixed content views list shift under ie6.
  This fixes http://dev.plone.org/plone/ticket/11280.
  [thomasdesvenain]


1.0.4 - 2010-11-15
------------------

- Restore more of the table.listing (Fancy listing) CSS. Refs #10331.
  [rossp]


1.0.3 - 2010-09-09
------------------

- Removed padding from navigation portlet header when it is hidden, so we won't
  see a small chunk of it. This fixes http://dev.plone.org/plone/ticket/10800.
  [cwainwright]

- Worked on fixing up styles for IE8:

  * put previous logo settings back (float messes with rtl)
  * put in IE spacing fixes (logo, hiddenStructure)
  * removed float from div.cell, so livesearch and display menu don't fall
    behind other items in IE8.

  Closes http://dev.plone.org/plone/ticket/10872.
  [cwainwright]

- Removed "line-height: 2em;" from "table.listing a" css rule so the vertical
  alignment of linked text and non linked text is the same.
  [vincentfretin]

- Moved icons in drop down "Add new..." menu to right of text for RTL
  scripts. This fixes http://dev.plone.org/plone/ticket/10954.
  [emanlove]

- Moved language selector to the left for RTL scripts. Also reversed margin
  of the actionMenu for RTL scripts. This fixes
  http://dev.plone.org/plone/ticket/10955.
  [emanlove]

- Fixed state position in the state/transitions menu when it is no clickable.
  [vincentfretin]

- Worked on fixing up styles for IE7:

  * removed padding on breadcrumb links, so all breadcrumb text
    displays on one level
  * put in hack to make links with content icons 'display: block' in IE.
    This fixes the Add New dropdown display, but breaks icon display on
    .navTreeCurrentItem, so I added zoom to the links.
    (fyi - the hack was the only way I could find to make this work to
    override the inline-block, did not work in IEFixes.css)
  * adjusted styles on logo so IE displays it in the correct place

  Refs http://dev.plone.org/plone/ticket/10872.
  [cwainwright]


1.0.2 - 2010-07-18
------------------

- Fixed problems with content menus sticking out of the edit bar under various
  font sizes. This closes http://dev.plone.org/plone/ticket/10736.
  [hannosch]

- Fixed anonymous personal bar spacing with multiple entries. This closes
  http://dev.plone.org/plone/ticket/10743.
  [hannosch]

- Fixed bulleted / numbered lists out of text area in right to left. This
  closes http://dev.plone.org/plone/ticket/9658.
  [emanlove, hannosch]

- Added back styles for grid listings. This refs
  http://dev.plone.org/plone/ticket/10331.
  [hannosch]

- Add globe icon to external links when "Mark External Links" is checked.
  [cwainwright]

- Update license to GPL version 2 only.
  [hannosch]


1.0.1 - 2010-07-07
------------------

- Removed remaining references to empty ``sunburst_js`` folder.
  [hannosch]


1.0 - 2010-07-07
----------------

- Removed IE9.js from Sunburst for now.
  [spliter]

- Cleaned up the Dashboard CSS. This fixes
  http://dev.plone.org/plone/ticket/10516.
  [limi]

- Adding max-width for the language selector, so it works even with
  a ridiculous amount of languages.
  This fixes http://dev.plone.org/plone/ticket/10452.
  [limi]

- Improved default rendering for Python code listings when using the
  syntax coloring, and improved the overall typography for code.
  This fixes http://dev.plone.org/plone/ticket/10692.
  [limi]

- Adding eventDetails styling and vertical table styles, this fixes
  http://dev.plone.org/plone/ticket/10540.
  [limi]

- Lining up the edges of the main layout elements, this fixes
  http://dev.plone.org/plone/ticket/10465.
  [limi]

- Increased space between icons in the sprite to 200px to make collisions
  unlikely. This fixes http://dev.plone.org/plone/ticket/10633.
  [limi]

- Only add content type icons when they are enabled.
  Fixes http://dev.plone.org/plone/ticket/10541
  [davisagli]

- Remove the sprited icons for the file and image content types, to avoid
  double icons. Fixes http://dev.plone.org/plone/ticket/10501.
  [davisagli]

- Improved printing: hide some UI, better document and listing views
  [tdesvenain]

- Restore some of the headline/description styling that was lost when
  Denys' branch was merged.
  [limi]

- Adding a border to the dialog boxes, so it doesn't appear borderless on
  browsers that don't support box-shadow, like Internet Explorer.
  Fixes http://dev.plone.org/plone/ticket/10630.
  [limi]


1.0b7 - 2010-05-31
------------------

- Improved typography and vertical rhythm of the theme to improve UX.
  [spliter]

- Moved overlay close button to upper-left to get it off the vertical
  scrollbar when a an ajax overlay is longer than the viewport.
  [stevem]

- Set overflow-y:auto on ajax overlays to support forms longer than the
  viewport.
  [stevem]


1.0b6 - 2010-05-03
------------------

- Remove styling of path_bar. Breadcrumbs should now behave in a manner
  similar to that of Plone 3.
  [esteele]


1.0b5 - 2010-05-03
------------------

- Show current page in breadcrumbs, give the surrounding div the same height
  as our portal-headers for consistency.
  [esteele]

- Dtml vars removed.
  Fixes: http://dev.plone.org/plone/ticket/10492
  [pelle]

- Improved :focus which is an accessibility requirement, a level 2 priority
  point/AA. This was removed entirely due to the reset css in use, so
  specifying :hover then remember :focus as well.
  Fixes: http://dev.plone.org/plone/ticket/10472
  [pelle]

- Fix for global navigation colliding with portlets, bread crumb etc.
  http://dev.plone.org/plone/ticket/10491
  [pelle]


1.0b4 - 2010-05-01
------------------

- Always enable breadcrumbs on all levels. ploneCustom contains an example on
  how to disable them on the first levels. This closes
  http://dev.plone.org/plone/ticket/9987 again.
  [elvix, hannosch]

- Added tests for "ajax_load" query string in main_template. When found, skip
  anything expensive that isn't going to show in an ajax overlay.
  The plone.app.jquerytools overlay helper sets the ajax_load query string
  to prevent browser caching.
  [smcmahon]

- Removed fixed vertical position for overlays. This needs to be computed on
  display so that overlays don't display out of the viewport on long pages.
  [smcmahon]

- Remove display:none for navigation portlet header. This is now handled
  through the template.
  [esteele]

- Improved style of blocked portlets.
  [igbun]

- Be carefull with adding ie hacks to IEFixes.css since Sunburst Theme
  uses IE8.js.
  Fixes http://dev.plone.org/plone/ticket/10417.
  [pelle]

- Improved overlay styling e.g. for openid overlay.
  Done when stepping trough #10035 and it's tried to make as general as possible.
  [pelle]


1.0b3 - 2010-04-10
------------------

- Improved mobile styling.
  [limi]

- Less disruptive styling for inline validation, it no longer shifts the form
  around in a significant way.
  [limi]

- Remove unused personalize_form template and unneeded copies of the author
  template and prefs_main_template.
  [davisagli]

- Updated styling for breadcrumbs, tags/keywords, and added styles for the
  currently selected nav tree item.
  [limi]

- Adjusted viewlets so that Sunburst uses the viewlet configuration from
  plone.app.layout.viewlets.
  [davisagli]

- Improved call-out and pull-quote styling.
  [limi]

- Improved general overlay styling.
  [limi]

- Improved history pop-up styling.
  [limi]

- Fix columns in prefs_main_template.
  [davisagli]

- Pass the current view to getColumnsClass.  This is needed if the view is not
  the @@plone view and it has different portlets (such as on the portlet
  management views).  This closes http://dev.plone.org/plone/ticket/10320.
  [davisagli]

- Repositioned the searchbox for RTL scripts.
  Fixes http://dev.plone.org/plone/ticket/10367.
  [emanlove]

- Stop hiding the (now) non-existing sendto action.
  Refs http://dev.plone.org/plone/ticket/8800.
  [dukebody]

- Fixed help_biography message.
  [vincentfretin]


1.0b2 - 2010-03-05
------------------

- Established Sunburst-specific browser view similar to ploneview and moved
  out the logic of applying special width/position CSS class on
  #portal-column-content from main_template.pt to that view.
  Closes http://dev.plone.org/plone/ticket/10292
  [spliter]

- Set up testing environment for the package
  [spliter]

- Inline images should not have borders (makes it hard to insert graphics that
  are part of a sentence, or similar), and we don't have any other round
  elements in the basic design (the edit bar is special, and is round to
  differentiate itself from the "stable elements"), so removed the rounded
  corners for image frames.
  [limi]

- Added some padding to a <fieldset> in order to have better-looking forms.
  References http://dev.plone.org/plone/ticket/9824
  [spliter]

- Moved language selector and personal tools viewlets into plone.portalheader
  viewlet manager and re-positioned them relatively instead of absolute.
  Closes http://dev.plone.org/plone/ticket/10252
  [spliter]

- Hide the "up to groups overview" link and fieldset border in the "add group"
  overlay.
  Closes http://dev.plone.org/plone/ticket/10149
  Closes http://dev.plone.org/plone/ticket/10150
  [stuttle]

- Replaced references to redundant #region-content to #content in stylesheets.
  References http://dev.plone.org/plone/ticket/10231
  [spliter]

- Adding back IE8.js to fix Sunburst for IE6/7, re-enabling mobile device
  support.
  [limi]

- Adding IE8.js v2.1 beta, this should resolve the issues with @media selectors,
  and let us re-enable the mobile support again. Thanks to Dean Edwards for
  fixing this.
  [limi]


1.0b1 - 2010-02-18
------------------

- Added example CSS to ploneCustom.css on how to enable the first levels of
  breadcrumbs. This fixes http://dev.plone.org/plone/ticket/9987.
  [limi]

- Removed #region-content and .documentContent from all templates, as they are
  redundant. See http://dev.plone.org/plone/ticket/10231 for details.
  [limi]

- Updated prefs_main_template.pt and personalize_form.pt to the recent markup
  conventions.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Moved 'content' slot to the same place as it is in CMFPlone's
  main_template.pt. Having the same slot in different places is confusing.
  References http://dev.plone.org/plone/ticket/9981
  [spliter]

- Wrapped .contentViews and .contentActions with <div id="edit-bar"> in
  author.pt.
  [spliter]

- Add html id to personal bar actions.
  [paul_r]

- Align the personal tools drop-down submenu to the left for
  RTL scripts.
  Fixes http://dev.plone.org/plone/ticket/10181.
  [emanlove]

- Updated templates to disable the columns with 'disable_MANAGER_NAME'
  pattern.
  [spliter]

- Removed action drop-down submenu right alignment for RTL scripts.
  Re-fixes http://dev.plone.org/plone/ticket/9651.
  [emanlove]

- Some sunburst for the site actions.
  Refs http://dev.plone.org/plone/ticket/10176
  [pelle]

- Remove common CSS registries.
  Refs http://dev.plone.org/plone/ticket/9988.
  [dukebody]

- Copied updated structure of 'main' slot from classic theme to Sunburst
  [spliter]


1.0a5 - 2010-02-01
------------------

- Move the login overlay form labels slightly down to align vertically
  with their associated fields.
  Refs http://dev.plone.org/plone/ticket/10021.
  [dukebody]

- Align the action drop-down submenu to the right.
  Fixes http://dev.plone.org/plone/ticket/10074.
  [dukebody]

- Remove the ability for anonymous to send author feedback again. A quick
  survey of integrators showed that this wasn't desirable.
  [esteele]

- Avoid the test function in the main_template. It doesn't exist in view page
  template files.
  [hannosch]

- Simplify the bodyClass construction.
  [hannosch]

- Use renderBase from new location.
  [hannosch]

- Remove obsolete charset definition for the global_cache_settings macro.
  [hannosch]

- Follow the getSectionFromURL change in CMFPlone.
  [hannosch]

- Just a markup polishing - <metal> tags don't need explicit "metal" for
  defining slots.
  [spliter]

- Copied preferred structure of 'main' slot from default main_template
  [spliter]

- Moved plone.abovecontent and plone.belowcontent viewlet managers actually
  above and below content respectively for Sunburst.
  References http://dev.plone.org/plone/ticket/10081
  [spliter]

- Support various image alignment classes and image caption.
  Based on the classic theme but with a slight sunburst touch.
  http://dev.plone.org/plone/ticket/10043
  [pelle]

- Don't limit the styling of portal messages etc. to the
  #region-content, portal messages might also appear out side
  that area in an overlay, portlet etc.
  Fixes http://dev.plone.org/plone/ticket/10069
  [pelle]

- Move search results to the left for RTL scripts.
  Fixes http://dev.plone.org/plone/ticket/10015.
  [emanlove]

- Port changes to author.pt from
  http://dev.plone.org/plone/changeset/32858
  [esteele]

- Limit the caption width to 200px.
  Fixes http://dev.plone.org/plone/ticket/9992.
  [dukebody]

- Avoid leading spaces in the class attribute of the body element.
  Fixes http://dev.plone.org/plone/ticket/9489.
  [dukebody]

- Removed underline from "Manage portlets" fallback link
  [spliter]

- Adjust login overlay position and width. Refs
  http://dev.plone.org/plone/ticket/9869
  [dukebody]

- Underline links in warning and error info messages. This closes
  http://dev.plone.org/plone/ticket/9801
  [dukebody]

- Add some spacing between siteaction links. This closes
  http://dev.plone.org/plone/ticket/9830
  [dukebody]

- Style display view menu for items selected as main view for a
  folder. This closes http://dev.plone.org/plone/ticket/9894
  [dukebody, thanks cewing]


1.0a4 - 2009-12-21
------------------

- made descriptions for items in livesearch wrap normally
  [spliter]

- fixed positioning of livesearch to not overflow the screen on the
  right and have horizontal scrollbar.
  [spliter]

- Enabled thumbnails view in Sunburst. Fixes #9870.
  [spliter]

- Do not display the author contact form when the author has no email
  (for example for openid users).  Refs #8707.
  [maurits]

- On author.cpt, only display the "log in to add comments" button if mailhost
  is defined. Only show the mailhost warning if user is authenticated.
  [esteele]


1.0a3 - 2009-12-02
------------------

- Add selectors for openid login form section to login styles.
  [smcmahon]

- Sunburst has it's own table-less prefs_main_template.pt to
  keep validation of control panels for both sunburst and
  plonetheme.classic
  [spliter]

- removed negative margin from #contentActionMenus - it broke
  the rounded corner of #edit-bar
  [spliter]

- moved "Manage portlets" fallback link out of main_template to
  plone.manage_portlets_fallback viewlet
  http://dev.plone.org/plone/ticket/9808
  [spliter]

- Update styles to reflect the move to @@register and @@new-user
  [esteele]


1.0a2 - 2009-11-18
------------------

- Remove non-ascii character in README that prevented distribution.
  [esteele]


1.0a1 - 2009-11-18
------------------

- Initial release
