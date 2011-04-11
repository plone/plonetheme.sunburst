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
