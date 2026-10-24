// @ts-check
// Boar's Head SCADA Wiki: docs-only Docusaurus site served at "/".
// Build: npm run build   Dev: npm start (http://localhost:3030)   Regenerate reference: python -I tools/gen_all.py
const {themes: prismThemes} = require('prism-react-renderer');

// Strict by default: broken links, anchors, markdown links and images fail the build.
// For a quick draft build only, set WIKI_STRICT_LINKS=0 to downgrade them to warnings.
const LINK_POLICY = process.env.WIKI_STRICT_LINKS === '0' ? 'warn' : 'throw';

// Optional partial build while several people write at once, e.g.
//   WIKI_INCLUDE="gateway/**,tags/**" npx docusaurus build
// (comma-separated folder globs relative to docs/; '/*.{md,mdx}' is appended). Unset = the whole wiki.
const DOCS_INCLUDE = process.env.WIKI_INCLUDE
  ? ['intro.md', ...process.env.WIKI_INCLUDE.split(',').map((g) => g.trim()).filter(Boolean)
      .map((g) => (/\.mdx?$/.test(g) ? g : `${g.replace(/\/+$/, '')}/*.{md,mdx}`))]
  : ['**/*.{md,mdx}'];

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Boar's Head SCADA Wiki",
  tagline: 'Groveport refrigeration SCADA on Ignition 8.3.7: the BH Perspective project, gateway, tags and workflow',
  favicon: 'img/favicon.png',
  url: 'http://localhost:3030',
  baseUrl: '/',
  trailingSlash: false,
  onBrokenLinks: LINK_POLICY,
  onBrokenAnchors: LINK_POLICY,
  onDuplicateRoutes: 'warn',
  markdown: {
    mermaid: true,
    hooks: {onBrokenMarkdownLinks: LINK_POLICY, onBrokenMarkdownImages: LINK_POLICY},
  },
  i18n: {defaultLocale: 'en', locales: ['en']},
  themes: [
    '@docusaurus/theme-mermaid',
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: false,
        docsRouteBasePath: '/',
        language: ['en'],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        searchResultLimits: 12,
        searchResultContextMaxLength: 80,
        searchBarShortcutHint: true,
        removeDefaultStemmer: true,
      }),
    ],
  ],
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          include: DOCS_INCLUDE,
          sidebarPath: require.resolve('./sidebars.js'),
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
          breadcrumbs: true,
        },
        blog: false,
        pages: false,
        theme: {customCss: require.resolve('./src/css/custom.css')},
        sitemap: {changefreq: 'weekly'},
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {defaultMode: 'light', respectPrefersColorScheme: true},
      docs: {sidebar: {hideable: true, autoCollapseCategories: false}},
      navbar: {
        title: 'SCADA Wiki',
        logo: {
          alt: "Boar's Head",
          src: 'img/bh-logo-light.png',
          srcDark: 'img/bh-logo-dark.png',
          href: '/',
        },
        items: [
          {to: '/getting-started', label: 'Getting Started', position: 'left'},
          {to: '/getting-started/common-tasks', label: 'Common Tasks', position: 'left'},
          {to: '/gateway', label: 'Gateway', position: 'left'},
          {to: '/tags', label: 'Tags', position: 'left'},
          {to: '/perspective', label: 'Perspective', position: 'left'},
          {to: '/scripting', label: 'Scripting', position: 'left'},
          {to: '/git-workflow', label: 'Git Workflow', position: 'left'},
          {type: 'search', position: 'right'},
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Start Here',
            items: [
              {label: 'Introduction', to: '/'},
              {label: 'Getting Started', to: '/getting-started'},
              {label: 'Your First Change', to: '/getting-started/first-change'},
            ],
          },
          {
            title: 'Reference',
            items: [
              {label: 'Gateway', to: '/gateway'},
              {label: 'Tags', to: '/tags'},
              {label: 'Perspective', to: '/perspective'},
              {label: 'Scripting', to: '/scripting'},
            ],
          },
          {
            title: 'Process',
            items: [
              {label: 'Deployment', to: '/deployment'},
              {label: 'Git Workflow', to: '/git-workflow'},
              {label: 'Keeping The Wiki Current', to: '/contributing'},
            ],
          },
        ],
        copyright:
          "Boar's Head Groveport SCADA. Internal engineering documentation. \"Boar's Head\" and the medallion are trademarks of Boar's Head Brand.",
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['powershell', 'python', 'json', 'bash', 'sql', 'ini', 'yaml', 'diff'],
      },
      mermaid: {theme: {light: 'neutral', dark: 'dark'}},
      tableOfContents: {minHeadingLevel: 2, maxHeadingLevel: 4},
    }),
};

module.exports = config;
