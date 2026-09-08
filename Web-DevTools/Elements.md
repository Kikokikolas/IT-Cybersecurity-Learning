# Elements

## Elements

In the elements section we can see the code, the one that creates the DOM tree, in the bottom part we can also see more information.

The code is html + css + javascript

## Style pane

This pane shows CSS rules affecting the selected element

For example:

:root.light-theme {
    --bard-color-neutral-90: #e3e3e3;
    --bard-color-neutral-95: #f2f2f2;
}

These:

--bard-color-neutral-90
--bard-color-neutral-95

are CSS custom properties, often called CSS variables.

For exemple:

--main-color: #ffffff;

can later be used as:

color: var(--main-color);

## Computed

In computed we can see the final CSS values after chrome has resolved everything.

For example, many CSS rules might affect:
    font-size

But Computed shows:
    font-size: 16px
Which is the acutal final value being rendered.

## Layout

This helps inspect:
 - Flexbox
 - Grid
 - Layout overlays

Useful when you want to understand why elements are positioned in a particular way

## Event Listeners

This shows javascript events attached to the select ellement

For example:

- click
- mouse over
- keydown
- submit

If a button does something when you click it, there may be a click event listener attached.

