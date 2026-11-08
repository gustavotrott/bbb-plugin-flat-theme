// Builds dist/theme.css: the same styles as the plugin, as one static
// stylesheet for BigBlueButton's custom style URL (public.app.customStyleUrl in
// settings.yml, or userdata-bbb_custom_style_url on /join).
// Local images become data URIs and @import rules move to the top.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const pkg = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8'));
const MIME = { '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp' };

function inline(file) {
  const dir = path.dirname(file);
  return fs.readFileSync(file, 'utf8').replace(/url\((['"]?)(\.{1,2}\/[^'")]+)\1\)/g, (m, q, ref) => {
    const asset = path.resolve(dir, ref);
    const type = MIME[path.extname(asset)];
    if (!type) throw new Error(`${file}: no MIME type for ${ref}`);
    return `url("data:${type};base64,${fs.readFileSync(asset).toString('base64')}")`;
  });
}

const imports = [];
const body = inline(path.join(root, 'src', 'theme.css')).replace(/^@import[^;]+;\s*\n?/gm, (rule) => {
  imports.push(rule.trim());
  return '';
}).trim();
fs.mkdirSync(path.join(root, 'dist'), { recursive: true });
const out = path.join(root, 'dist', 'theme.css');
fs.writeFileSync(out, [`/* ${pkg.name} ${pkg.version}. ${pkg.license} license. */`, ...imports, '', body, ''].join('\n'));
console.log('dist/theme.css', `${Math.round(fs.statSync(out).size / 1024)} KB`);
