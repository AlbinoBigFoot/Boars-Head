---
title: Comm Loss And Value Quality
sidebar_position: 17
description: What operators see when PLC data is not Good (red COMM LOSS, gray dash, No Data) and how to apply the same rule to a new binding in the Designer.
sources:
  - docs/quality-sweep.md
last_verified: 2026-10-24
---

# Comm Loss And Value Quality

## What it does

Permanent rule (2026-10-24): **everything shows comm loss when its data is not Good.** No device may show RUN, OPEN,
a level fill or a state colour from a stale value, and Perspective's black quality overlay (the dot, the dashed box,
the "UNKNOWN" bar) must never appear. When the PLC link drops, tag values become Bad or Uncertain (the last known
value) and the HMI must say so.

## What operators see

| Situation (the source is not Good) | What shows |
|---|---|
| A device symbol (pump, compressor, valve, fan, tank, evaporator, discrete input, sensor, sequence, LTU, safeties, PLC card) | A **red** symbol and a red **COMM LOSS** label. No run or open animation, no level fill, no state colour |
| State text on pages and panels (RUN, OPEN, IDLE, Interlocks OK) | **COMM LOSS** |
| State chips and mode words in faceplates (Auto / Manual, OK / Active) | A gray dash |
| Value text | A gray italic dash; the unit is hidden |
| Colours and fills | Neutral gray |
| Edit pencils (setpoints, timers) | Dimmed and not clickable, so nothing can be written from a stale screen |
| Charts and tables with no data | The text **No Data** |
| A missing tag or empty path | The gray dash (the PLC rack chips say "No Data") |
| A command, mode or toggle button (for example the control group panel's Start / Stop Defrost, mode and cycle-fan buttons) | **Disabled**, with the tooltip **Comm Loss - Command Unavailable**; a mode button falls back to its "not selected" look |

A PLC-wide link loss turns every OPC value Uncertain or Bad, so the whole HMI goes to this state at once. Real
Good values return on their own when the link is back.

## How To Change It

Apply the rule to every new binding that reads a tag.

1. **Test the quality with `isGood()`**, not "not bad". `isBad()` and `isBadOrError()` let the quality
   `Uncertain_LastKnownValue` through, which is exactly what a dropped link produces. Pattern:

   ```
   if(isGood(tag({view.params.tagPath} + "/Val")), tag({view.params.tagPath} + "/Val"), null)
   ```

   Use `coalesce(try(tag(...), null), <default>)` where a default is safe. Leave `params.tagPath` empty in the
   Designer (no placeholder paths).
2. **Pick the fallback by property:** a display string gets the dash (an em dash); a colour or fill gets a neutral
   gray; a state word gets `COMM LOSS`; a custom property gets null.
3. **Comm loss per device:** compute it from the device's key status member, for example
   `custom.values.commLoss = !isGood(tag(<tagPath>/Motor/Val_Sts))`. Expression-based members (for example
   `ModulesFaulted`, or `HmiStatus` when it uses `coalesce`) stay Good while their inputs are stale, so gate them on
   the PLC's `Connected` member or on a key OPC member, not on their own quality.
4. **Opt out of the overlay only after gating.** The client draws its quality overlay on a component when any of its
   `props.*` bindings is Bad, Uncertain or Pending. In the Designer, open the binding (the link icon next to the
   property) and tick **Overlay Opt-Out** (`overlayOptOut` in the JSON). Do this only on a binding that already
   handles a not-Good value; never on an ungated one. `custom.*`, `meta.*` and `position.*` bindings never draw an
   overlay, but they pass their quality on to the props that read them.
5. **Reuse the style classes.** Gray dash text: `value-bad`. Red comm-loss symbol: `device-comm-loss`, which uses the
   theme variable `--deviceFill-commLoss`. Edit them in Designer > Project > Styles > Style Classes (and the
   [Styling](../perspective/styling/index.md) pages), not inline.
6. **Charts and tables:** set the ApexCharts `noData` text to "No Data" and the table's empty message to "No Data".
7. **Beware of params:** quality travels through `view.params`. A tag-derived value inside a path param (for example
   a flag that decides part of a `tagPath`) turns every binding of the embedded view Uncertain.
8. **Command buttons:** disable the button while the member it acts on is not Good, and give it the tooltip
   "Comm Loss - Command Unavailable": in the Designer set `props.enabled` to an expression that includes
   `isGood(tag(<member path>))` and the tooltip text to an expression that returns that sentence when it is not Good.
9. **Dynamic member paths count too.** A binding that builds a path from a view param (for example
   `{view.params.tagPath} + '/Status/Value'`) reads a live PLC member unless that member is one of the memory-only
   members the HMI owns (settings such as `Cfg_*Path`, `Cfg_Has*`, or the device row lists). Gate it like any other
   tag read; do not assume a path ending in `/Value` is a memory tag.
10. **Edit pencils:** the setpoint, timer, string and multi-state input components read a `custom.qualityOk` guard;
   keep it bound when you copy one.

To test it, stop the link (as happens whenever the PLC is unreachable), or point a copy of the view at a tag that does
not exist, and open the view in a session: every state word must read COMM LOSS or the dash and no dashed overlay may
appear.

## Known limitations and parked items

- Binding sources that are only structure (a tag browse feeding a list, a pen list, a selector option list) are
  deliberately not gated because they cannot show a stale live state.
- The check now treats dynamic member paths strictly (the 2026-10-24 sweep found 70 more bindings in 10 views that
  had been skipped, mostly the control group panel); all of them are gated now. With the link up, three CG pages
  showed 0 overlays. The enabled state of the command buttons for a permitted user is still a manual check.
- The earlier sweep (44 pages and the faceplates of the main device types) found 0 overlays with the link down; the
  evaporator, exhaust fan and LTU faceplates are on the manual check list.

Source of truth: `docs/quality-sweep.md`. See also [Value Quality in faceplates](../perspective/faceplates.md#value-quality-gray-italic-dash).
