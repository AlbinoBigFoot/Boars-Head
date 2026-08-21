#!/usr/bin/env python3
"""Playwright layout audit helpers for Groveport Site Dashboard.

Run against a live page via MCP browser_evaluate — paste AUDIT_JS — or:
  python scripts/_audit_groveport_layout.py   # prints the JS to stdout

Fail conditions (must be zero):
  - nestedScrollbars: overflow auto/scroll hosts inside domain panel that
    actually scroll (excluding .psc-kpi-domain-panel itself)
  - overlaps: intersecting hero pens or meter-row label boxes
  - meterStretch: meter row wider than 440px OR first→status gap > 24px
  - penStretch: hero pen width outside 150–210px
"""
from __future__ import annotations

AUDIT_JS = r"""() => {
  const fail = [];
  const info = {};

  const rectsOverlap = (a, b) =>
    !(a.right <= b.left + 1 || b.right <= a.left + 1 ||
      a.bottom <= b.top + 1 || b.bottom <= a.top + 1);

  // Nested scrollbars (exclude the domain panel's own page scroll)
  const nested = [];
  document.querySelectorAll('.psc-kpi-domain-panel *').forEach((el) => {
    const cs = getComputedStyle(el);
    const cls = (el.className || '').toString();
    if (cls.includes('kpi-domain-panel')) return;
    const oy = cs.overflowY === 'auto' || cs.overflowY === 'scroll';
    const ox = cs.overflowX === 'auto' || cs.overflowX === 'scroll';
    if (!oy && !ox) return;
    const contentY = el.scrollHeight > el.clientHeight + 3;
    const contentX = el.scrollWidth > el.clientWidth + 3;
    const vBar = el.offsetWidth - el.clientWidth > 2;
    const hBar = el.offsetHeight - el.clientHeight > 2;
    if ((oy && (contentY || vBar)) || (ox && (contentX || hBar))) {
      nested.push({
        cls: cls.slice(0, 100),
        oy: cs.overflowY,
        ox: cs.overflowX,
        sh: el.scrollHeight,
        ch: el.clientHeight,
      });
    }
  });
  info.nestedScrollbars = nested;
  if (nested.length) fail.push('nestedScrollbars:' + nested.length);

  // Hero pens
  const pens = [...document.querySelectorAll('.psc-kpi-hero-pen')];
  info.penCount = pens.length;
  info.penWidths = pens.map((p) => Math.round(p.getBoundingClientRect().width));
  for (const w of info.penWidths) {
    if (w < 150 || w > 210) {
      fail.push('penStretch:' + w);
      break;
    }
  }
  for (let i = 0; i < pens.length; i++) {
    for (let j = i + 1; j < pens.length; j++) {
      if (rectsOverlap(pens[i].getBoundingClientRect(), pens[j].getBoundingClientRect())) {
        fail.push('penOverlap:' + i + '-' + j);
      }
    }
  }

  // Meter rows — must hug content, not stretch across the panel
  const rows = [...document.querySelectorAll('.psc-kpi-coming-meter-row')];
  info.meterRows = rows.length;
  const stretch = [];
  for (const row of rows) {
    const r = row.getBoundingClientRect();
    const labels = [...row.querySelectorAll('.ia_labelComponent')]
      .map((l) => ({
        t: (l.textContent || '').trim(),
        box: l.getBoundingClientRect(),
      }))
      .filter((x) => x.t);
    const status = labels.find((x) => /Planned|Live|Installed/i.test(x.t));
    const area = labels[0];
    const gap = status && area ? status.box.left - area.box.right : null;
    if (r.width > 440 || (gap != null && gap > 24)) {
      stretch.push({
        w: Math.round(r.width),
        gap: gap == null ? null : Math.round(gap),
        area: area && area.t,
      });
    }
    // label overlaps inside row
    for (let i = 0; i < labels.length; i++) {
      for (let j = i + 1; j < labels.length; j++) {
        if (rectsOverlap(labels[i].box, labels[j].box)) {
          fail.push('meterLabelOverlap:' + labels[i].t + '/' + labels[j].t);
        }
      }
    }
  }
  info.meterStretch = stretch;
  if (stretch.length) fail.push('meterStretch:' + stretch.length);

  // Chart shells fixed height
  const shells = [...document.querySelectorAll('.psc-kpi-chart-shell')].map((el) =>
    Math.round(el.getBoundingClientRect().height)
  );
  info.chartShellHeights = shells;
  for (const h of shells) {
    if (h < 140 || h > 280) fail.push('chartShellHeight:' + h);
  }

  // Pens → chart vertical gap should not be a dead zone
  if (pens.length && document.querySelector('.psc-kpi-dashboard-chart-card')) {
    const gap = Math.round(
      document.querySelector('.psc-kpi-dashboard-chart-card').getBoundingClientRect().top -
        pens[pens.length - 1].getBoundingClientRect().bottom
    );
    info.gapPensToChart = gap;
    if (gap > 40) fail.push('deadZonePensChart:' + gap);
  }

  info.ok = fail.length === 0;
  info.fail = fail;
  return info;
}"""


def main() -> None:
    print(AUDIT_JS)


if __name__ == "__main__":
    main()
