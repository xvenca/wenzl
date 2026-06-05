const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE = 'http://localhost:1313';
const OUT  = path.join(__dirname, '../../screenshots');
fs.mkdirSync(OUT, { recursive: true });

const pages = [
  { url: '/',             name: 'no-home' },
  { url: '/svermer/',     name: 'no-swarms' },
  { url: '/bikuber/',     name: 'no-hives' },
  { url: '/pollinatorer/',name: 'no-pollinators' },
  { url: '/om-meg/',      name: 'no-about' },
  { url: '/medlemskap/',  name: 'no-membership' },
  { url: '/en/',          name: 'en-home' },
  { url: '/cs/',          name: 'cs-home' },
];

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    deviceScaleFactor: 1,
  });

  for (const { url, name } of pages) {
    const page = await context.newPage();
    try {
      await page.goto(BASE + url, { waitUntil: 'networkidle', timeout: 15000 });
      await page.screenshot({
        path: path.join(OUT, `${name}.png`),
        fullPage: false,
      });
      console.log(`✓ ${name}`);
    } catch (e) {
      console.error(`✗ ${name}: ${e.message}`);
    } finally {
      await page.close();
    }
  }

  await browser.close();
})();
