# Change log ? `feat/groveport-kpi-nav-dashboard`

Accurate file-touch log for staging/commits on this multi-work branch.
**Rule:** every intentional edit lands in a section below before commit. Do not stage `.resources` CAS churn or System/StoreAndForward noise.

| When (local) | Workstream | Paths touched | Notes |
|--------------|------------|---------------|-------|
| 2026-08-20 ~13:47 | bootstrap | `docs/kpi/Utility Tracker_template.xlsx` | Copied from Downloads for KPI reference |
| 2026-08-20 ~13:47 | bootstrap | `docs/handoff/CHANGE-LOG-feat-groveport-kpi-nav.md` | This log |
| 2026-08-20 ~13:50 | gsd | `.planning/MILESTONE-CONTEXT-groveport-kpi.md`, `REQUIREMENTS-groveport-kpi.md`, `ROADMAP-groveport-kpi.md` | Milestone slice for this branch |
| 2026-08-20 ~13:52 | data | `scripts/_inspect_utility_tracker.py` | Stdlib xlsx peek (temp helper; OK to keep or drop later) |
| 2026-08-20 ~13:53 | data | `docs/kpi/README.md` | Workbook sheet/metric notes |
| 2026-08-20 ~13:55 | nav-clock (G1) | `?/00_Docked/Navigation/view.json`, `stylesheet/stylesheet.css` (+ resource.json via repair) | DateTime label under Search; `.psc-nav-clock` |
| 2026-08-20 ~13:58 | home-cards (G2) | `?/02_Widgets/MetricCard/*`, `?/LandingPage/Globe/view.json` (+ resource.json via repair) | Lightspeed-style KPI rail on Globe (static params) |
| 2026-08-20 ~13:58 | data (G3) | `tag-definition/default/KPI/**`, `scripts/_seed_kpi_groveport_tags.py`, `docs/kpi/README.md` | Memory placeholders EPMS/Utility/Production ? Site+8 areas |
| 2026-08-20 ~14:00 | dashboards+nav (G4/G5) | `views/00_Pages/Groveport/**`, `page-config/config.json`, `Navigation/view.json`, `TempNav/view.json`, `_Config/tags.json` (Navigation), `scripts/_build_groveport_kpi_pages.py` | Site Overview + Area Dashboard + Domains; Area?EPMS/Utility/Production leaves |
| 2026-08-20 ~14:05 | nav-clock fix | `?/00_Docked/Navigation/view.json`, `stylesheet/stylesheet.css` (+ resource.json via repair) | 12h+seconds clock (`MMM dd, yyyy h:mm:ss a`); center Search row + DateTime in dock |
| 2026-08-20 ~14:10 | bugfix MetricCard params | `?/02_Widgets/MetricCard/view.json` (+ resource.json), `?/LandingPage/Globe/view.json`, `?/Groveport/Site/Overview/view.json`, `?/Groveport/Area/Dashboard/view.json`, `?/Groveport/Domains/{EPMS,Utility,Production}/view.json` (+ resource.json each) | Designer typed param objects ? BH simple params; card tile sizing (~140px) |
| 2026-08-20 ~14:15 | nav tree icons+collapse | `?/00_Docked/Navigation/view.json`, `?/00_Docked/TempNav/view.json`, `_Config/tags.json` (Navigation), `scripts/_build_groveport_kpi_pages.py` (+ Navigation/TempNav resource.json via repair) | Domain leaves used missing material icons (`bolt`/`water_drop`/`precision_manufacturing`) ? blank glyphs + Tree remount fail on collapse/expand. Switched to proven paths: `show_chart` / `opacity` / `build`. |
| 2026-08-20 ~14:15 | kpi CSS | `stylesheet/stylesheet.css` (+ resource.json via repair) | Lightspeed-ish Groveport KPI classes: `kpi-card`, `kpi-card-header`, `kpi-value`, `kpi-chart`, `kpi-metrics`, `kpi-dashboard-grid`, `kpi-dashboard-page` (compose with `container-card`) |
| 2026-08-20 ~14:25 | KPI widget + dashboards | `?/02_Widgets/KPI/*` (new), `?/Groveport/Domains/{EPMS,Utility,Production}/view.json`, `?/Groveport/Site/Overview/view.json`, `?/Groveport/Area/Dashboard/view.json`, `?/LandingPage/Globe/view.json`, `stylesheet/stylesheet.css` (+ resource.json via repair), `scripts/_build_kpi_widget_and_pages.py`, `scripts/_build_lightspeed_kpi_widget.py` | Lightspeed KPI card (ApexCharts stepline + Min/Max/Avg placeholder sparkline); Groveport MetricCard?KPI (~240?280); Globe: 4 KPI + 2 MetricCard |
| 2026-08-20 ~14:40 | KPI tags re-seed | `tag-definition/default/KPI/**` | Re-ran `_seed_kpi_groveport_tags.py` so memory placeholders exist for live value bindings |
| 2026-08-20 ~14:55 | Site cards + denser Overview | `?/02_Widgets/SiteCard/*` (new), `?/LandingPage/Globe/view.json`, `?/Groveport/Site/Overview/view.json`, `?/Groveport/Domains/*`, `?/Area/Dashboard/view.json`, `stylesheet.css`, `scripts/_build_site_cards_and_overview.py`, `scripts/_seed_kpi_groveport_tags.py`, `tag-definition/default/KPI/{NewCastle,ForrestCity,Petersburg,Holland}/**` | Home rail = Lightspeed-style Site cards (5 plants, gauge+pens, click?page). Groveport Site Overview = EPMS/Utility/Production overview cards (hero + gauge + pens + trend + time range). Domain pages densified. Other plants Site tag stubs. |
| 2026-08-20 ~14:50 | SiteCard gauge fix | `?/02_Widgets/SiteCard/view.json`, `?/Groveport/Site/Overview/view.json`, `scripts/_fix_sitecard_gauge.py` (+ resource.json via repair) | Replaced missing `ia.chart.simple-gauge` with Kyvis ApexCharts `radialBar` (kWh vs 7yr %) |
| 2026-08-20 ~14:55 | SiteCard size | `?/SiteCard/view.json`, `?/LandingPage/Globe/view.json`, `stylesheet.css` | Larger radialBar (~168px), taller site embeds (270px), overflow visible so gauge/pens not clipped |
| 2026-08-20 ~15:15 | SiteCard polish (Playwright) | `?/SiteCard/view.json`, `?/Globe/view.json`, `stylesheet.css`, `scripts/_tighten_sitecard.py` | Full-circle radial (no semi dead space); pen rows value/unit no-shrink (Production overlap fixed); 200px embeds; hide view-parent scrollbars; Outdoor Temp fully visible |
| 2026-08-20 ~15:20 | SiteCard clip + labels | `?/SiteCard/view.json`, `?/Globe/view.json`, `stylesheet.css`, `scripts/_fix_sitecard_polish.py` | Removed Sites/hint headers; vs 7yr as caption under gauge (not Apex name); overflow visible so card bottom border/shadow not clipped |
| 2026-08-20 ~15:30 | SiteCard metrics-only | `?/SiteCard/view.json`, `?/Globe/view.json`, `scripts/_sitecard_metrics_only.py` | Dropped home-page gauges; Site cards are live metric pens only (kWh / gas / production / temp) |
| 2026-08-20 ~15:35 | SiteCard spacing/type | `?/SiteCard/view.json`, `?/Globe/view.json` | Larger type (title 18 / value 18 / label 15); 12px label?value gap; 18px bottom padding; 220px card height |
| 2026-08-20 ~15:40 | SiteCard rail width | `?/SiteCard/view.json`, `?/Globe/view.json` | Rail 320px; equal 14px padding; pens hug content; values flush right on narrower card |
| 2026-08-20 ~15:50 | Hide Legend Key | `page-config/config.json` (+ resource.json via repair) | Page dock override: Legend `handle: hide` on `/` and all `/plants/*` KPI routes; shared Legend still on equipment pages |
| 2026-08-20 ~15:55 | SiteCard value align | `?/SiteCard/view.json`, `stylesheet.css` | Fixed-width value column so green digits share left edge regardless of unit text |
| 2026-08-20 ~15:58 | SiteCard scrollbar fix | `?/SiteCard/view.json`, `stylesheet.css` | Wider fixed px value/unit cols + overflow:hidden so pen rows no longer show H-scrollbars |
| 2026-08-20 ~16:05 | Groveport Site Dashboard | `?/Groveport/Site/Overview/view.json`, `docs/kpi/dashboard-series.json`, `_build_groveport_site_dashboard.py`, `stylesheet.css`, `docs/kpi/README.md` | Excel Dashboard-style Temp (36mo) + kWh (48mo) band charts; hero pens + metering/future KPI cards |
| 2026-08-20 ~16:15 | Coming-online placeholders | `Groveport/Site/Overview`, `KPI/.../ComingOnline/**`, `_seed_kpi_groveport_tags.py`, `_build_groveport_site_dashboard.py` | Metering-by-area rows, Cascade/Eneroi line-break shells, YoY stub charts, Innovative; tags seeded |
| 2026-08-20 ~16:20 | Dashboard domain sections | `Groveport/Site/Overview`, `_build_groveport_site_dashboard.py`, `stylesheet.css` | Restructured into EPMS / Utility / Production sections; coming-online nested under each domain |
| 2026-08-20 ~16:30 | Option B domain tabs | `Groveport/Site/Overview`, `_build_groveport_site_dashboard.py` | EPMS / Utility / Production TabContainer ? one domain visible at a time |
| 2026-08-20 ~16:40 | Executive canvas adapt | `Groveport/Site/Overview` (new), `OverviewClassic` (kept), `page-config`, `_build_groveport_executive_dashboard.py` | Canvas SPoG layout: KPI strip + Executive/Matrix/Innovations tabs; classic domain tabs at /plants/groveport/classic |
| 2026-08-20 ~16:45 | Exec chart band + no scrollbars | `Overview`, `_build_groveport_executive_dashboard.py`, `stylesheet.css` | Main kWh chart back to 7yr rangeArea band; fixed-height chart shells kill H-scrollbars |
| 2026-08-20 ~16:50 | Revert to domain tabs | `Overview` from Classic, `OverviewExecutive` saved, `page-config` | Default Groveport back to EPMS/Utility/Production tabs; executive at /plants/groveport/executive |
| 2026-08-20 ~17:05 | Layout flex polish | `Overview`, `_build_groveport_site_dashboard.py`, `stylesheet.css`, `_audit_groveport_layout.py` | Kill nested scrollbars/stretch: fixed pens/meter cols/chart shells; Playwright layout audit helper |
| 2026-08-20 ~17:10 | Tabs + globe hover + themes | `stylesheet.css`, `Globe/view.json`, `globe/index`, `mapMarkers/doPost.py`, `_Config/tags.json` (MapMarkerHover), `_build_groveport_site_dashboard.py` | Domain tabs CTA active state; marker hover pops matching SiteCard / dims others; dark-friendly chart colors + axis/legend text tokens |
| 2026-08-20 ~17:20 | Globe hover slide | `stylesheet.css`, `Globe/view.json` | Hot card `translateX(-40px)` toward globe (no scale/clip); rail left gutter; dim grey-out kept |
| 2026-08-20 ~17:45 | Globe rail auto-scroll | `globe/index/config.json`, `_patch_globe_rail_scroll.py` | Off-screen SiteCard scrolls into view on marker hover (iframe JS + poll; Perspective onChange JS unreliable) |
| 2026-08-21 ~05:45 | Quiet tabs + demo data | `stylesheet.css`, `Overview`, `_build_groveport_site_dashboard.py`, `_seed_kpi_groveport_tags.py` | Domain tabs: transparent strip + CTA underline only; Coming-online sections renamed with Demo chips + fake metering/YoY/line-break/Innovative values |
| | | | |

## Workstreams

1. **Nav clock** ? Date/time under search in docked Navigation
2. **Home KPI cards** ? Lightspeed-style cards on Globe/Landing (views only; no live tags yet)
3. **Sample data + placeholders** ? Utility Tracker ? docs + memory/placeholder tags (EPMS / Utility / Production)
4. **Groveport KPI dashboards** ? Site/area KPI pages patterned on Lightspeed Site/Building Overview
5. **Nav tree** ? Boars Head ? Groveport ? {Area} ? EPMS | Utility | Production

## Commit grouping (intent)

- Prefer one commit per workstream when possible; tags ship with the dashboard/nav that needs them.
- Always run `python scripts/repair-resource-signatures.py` (+ `--check`) after Perspective/script edits; POST scan.
