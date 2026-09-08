# Elements

In the Elements panel, we can inspect the code that creates the DOM tree. The bottom part also contains more information about the selected element.

The code is made up of HTML, CSS, and JavaScript.

## Style pane

This pane shows the CSS rules affecting the selected element.

For example:

:root.light-theme {
    --bard-color-neutral-90: #e3e3e3;
    --bard-color-neutral-95: #f2f2f2;
}

These:

--bard-color-neutral-90
--bard-color-neutral-95

are CSS custom properties, often called CSS variables.

For example:

--main-color: #ffffff;

can later be used as:

color: var(--main-color);

## Computed

In Computed, we can see the final CSS values after Chrome has resolved everything.

For example, many CSS rules might affect:
    font-size

But Computed shows:
    font-size: 16px
This is the actual final value being rendered.

## Layout

This helps inspect:
 - Flexbox
 - Grid
 - Layout overlays

Useful when you want to understand why elements are positioned in a particular way

## Event Listeners

This shows JavaScript events attached to the selected element.

For example:

- click
- mouse over
- keydown
- submit

If a button does something when you click it, there may be a click event listener attached.

## DOM Breakpoints

This is a more advanced feature.
It lets you pause JavaScript when something changes in the DOM.

For example:

Pause when this element is removed.

Useful for debugging.

## Properties

This shows the JavaScript object properties associated with the DOM element

Remember:

HTML element
      ↓
represented as
      ↓
JavaScript DOM object

## Accessibility

This lets you inspect how assistive technology sees the selected element.

For example:

Role
Name
ARIA attributes
Accessibility tree

## Important Things

What we see on the screen is the current DOM, which is not necessarily exactly the HTML that originally came from the server.

For example, the server may send:

<div id="app"></div>

Then JavaScript runs and creates:

<div id="app">
    <button>Login</button>
    <p>Hello</p>
</div>

DevTools Elements will show the current DOM after JavaScript modifications.

That is why:

View Page Source

and:

F12 → Elements

can sometimes show different things.

That is a very useful concept to remember.
