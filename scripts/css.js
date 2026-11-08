// Builds the theme as one static stylesheet for BigBlueButton's custom style
// URL (public.app.customStyleUrl in settings.yml, or userdata-bbb_custom_style_url
// on /join). Local images become data URIs and @import rules move to the top.
//
//   node scripts/css.js         dist/theme.css, for the newest BigBlueButton, plus the
//                               frozen stylesheets for older versions, copied as they
//                               are from versions/<version>/theme.css
//   node scripts/css.js --root <dir> --version 4.0.3
//                               builds the checkout in <dir> (another branch) into
//                               dist/4.0.3/theme.css
const fs = require('fs');
const path = require('path');

const repo = path.resolve(__dirname, '..');
const args = process.argv.slice(2);
const opt = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args.splice(i, 2)[1] : undefined;
};
const root = path.resolve(opt('--root') || repo);
const version = opt('--version');
const pkg = JSON.parse(fs.readFileSync(path.join(repo, 'package.json'), 'utf8'));
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
const body = inline(path.join(root, 'src', 'theme.css')).replace(/^@import\b.*;[ \t]*\n?/gm, (rule) => {
  imports.push(rule.trim());
  return '';
}).trim();
const css = (label) => [`/* ${pkg.name} ${pkg.version} for BigBlueButton ${label}. ${pkg.license} license. */`, ...imports, '', body, ''].join('\n');

function write(rel, text) {
  const file = path.join(repo, 'dist', rel);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, text);
  console.log(`dist/${rel}`, `${Math.round(text.length / 1024)} KB`);
}

if (version) {
  write(path.join(version, 'theme.css'), css(version));
} else {
  write('theme.css', css('4.0.1 or later'));
  // Older client versions: stylesheets frozen when that version was current
  const frozen = path.join(repo, 'versions');
  if (fs.existsSync(frozen)) {
    fs.cpSync(frozen, path.join(repo, 'dist'), { recursive: true });
    console.log(`dist/: ${fs.readdirSync(frozen).join(', ')} (frozen)`);
  }
}
