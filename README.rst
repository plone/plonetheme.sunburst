Sunburst, a theme for Plone 4
=============================

Sunburst is a modern, minimalist, grid-based theme for Plone 4.

.. contents:: Table of contents

Goals
-----

- Keep the theme color-neutral (black, white, grays), so it meshes with any
  company logo and doesn't feel like it requires color adjustment for doing the
  10-minute-show-it-to-the-boss exercise.

- The theme does not use any tables for layout, and is based on the Deco grid
  approach which is currently in use on plone.org. It works perfectly in all
  browsers, including IE6.

- The grid works in both fixed-width and flexible-width modes, there's a
  commented-out section in the top of the CSS file you can enable if you want
  fixed-width layout.

- No substantial markup changes outside of the table removal - class and ID
  names are kept.

- The theme uses some CSS3 features, but degrades gracefully.

- The theme does not use any DTML.

- When viewed on a device with less than 640px width, the portlets neatly tuck
  under the main content area. This means that the site works well with
  CSS-enabled devices like tablets and phones that may have limited resolution.


How to depend on Sunburst for your custom theme
-----------------------------------------------

Since Sunburst 1.4, Plone-UI generic styles are seperated from public.css,
where only Sunburst-design specific styles were left. This reduces the need to
override style definitions to match your custom theme.

Here is a way to only include specific stylesheets in your custom theme. This
example is based on Products.ResourceRegistries with the "bundles" concept,
which is available from version 2.1a1.

In the cssregistry.xml profile, configure bundles for your styles:

.. code-block:: xml

    <?xml version="1.0"?>
    <object name="portal_css">

      <!-- These are the Sunburst-styles which we want to include in our custom
           theme. They are configured to be in the "default" bundle.
           Note: by default, all styles land in the "default" bundle. So this
           configuration isn't strictly necessary. -->
      <stylesheet bundle="default" id="authoring.css"/>
      <stylesheet bundle="default" id="base.css"/>
      <stylesheet bundle="default" id="controlpanel.css"/>
      <stylesheet bundle="default" id="forms.css"/>
      <stylesheet bundle="default" id="IEFixes.css"/>
      <stylesheet bundle="default" id="member.css"/>
      <stylesheet bundle="default" id="reset.css"/>
      <stylesheet bundle="default" id="RTL.css"/>

      <!-- These are Sunburst-design specific styles, which we do not want to
           include in our theme. They are configured to be in the "sunburst"
           bundle. -->
      <stylesheet bundle="sunburst" id="columns.css"/>
      <stylesheet bundle="sunburst" id="deprecated.css"/>
      <stylesheet bundle="sunburst" id="invisibles.css"/>
      <stylesheet bundle="sunburst" id="kupuplone.css"/>
      <stylesheet bundle="sunburst" id="mobile.css"/>
      <stylesheet bundle="sunburst" id="navtree.css"/>
      <stylesheet bundle="sunburst" id="portlets.css"/>
      <stylesheet bundle="sunburst" id="print.css"/>
      <stylesheet bundle="sunburst" id="public.css"/>

      <!-- This is your custom style -->
      <stylesheet bundle="mycustombundle" id="mystyles.css" insert-after="*"
          cacheable="True" compression="safe" cookable="True" enabled="True"
          expression="" media="screen" rel="stylesheet" rendering="link"/>

    </object>


In registry.xml, configure the resource-bundles you want to include in your
custom theme. The "sunburst" bundle isn't inlcuded.

.. code-block:: xml

    <?xml version="1.0"?>
    <registry>
      <record
          name="Products.ResourceRegistries.interfaces.settings.IResourceRegistriesSettings.resourceBundlesForThemes"
          interface="Products.ResourceRegistries.interfaces.settings.IResourceRegistriesSettings"
          field="resourceBundlesForThemes">
        <value purge="false">
          <element key="mycustom_skin">
            <element>jquery</element>
            <element>default</element>
            <element>mycustombundle</element>
          </element>
        </value>
      </record>
    </registry>

Of course, the mycustom_skin needs to be registered in skins.xml too.
