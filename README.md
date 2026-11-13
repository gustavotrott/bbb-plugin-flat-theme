# bbb-plugin-flat-theme

A theme plugin for the BigBlueButton 4.0 HTML5 client. It is pure CSS, so you can use it in two ways:

- **As a plugin** (`pluginManifests`): no client rebuild and nothing else to configure.
- **As a plain stylesheet** (`customStyleUrl`): one static `theme.css` with every icon inlined, if you would rather not run a plugin. See [Use it as a custom style](#use-it-as-a-custom-style-css-only).

> **Requires BigBlueButton 4.0.1 or later.** The theme styles the client through its static `bbb-*` classes (`bbb-avatar--presenter`, `bbb-navigation__item--active`...), added in 4.0.1 ([#26193](https://github.com/bigbluebutton/bigbluebutton/pull/26193)). For 4.0.0, use the [4.0.0 stylesheet](#use-it-as-a-custom-style-css-only), or the plugin from the [`bbb-4.0.0`](https://github.com/gustavotrott/bbb-plugin-flat-theme/tree/bbb-4.0.0) branch.

![Flat theme on BigBlueButton 4.0](docs/after.jpg)

## Before and after

The same meeting, same window, with and without the theme.

| Before (default client) |
|---|
| ![Before](docs/before.jpg) |

| After (with this plugin) |
|---|
| ![After, with the main changes numbered](docs/after-annotated.jpg) |


_Camera images in the screenshots are illustrations._

## What it changes

**Icon bar (left)**
- Full height, no padding and no rounded corners, on a solid blue background.
- Narrower: 72px instead of the client's `60px + 2% of the window`.
- 44px buttons with white 24px icons in a thin stroke (1.25 instead of the 2 used everywhere else). The active item gets a lighter background and a marker on the right edge.
- On desktop the groups of icons sit together at the top instead of being spread over the whole height. Only the last group (dashboard, settings) stays at the bottom.
- On desktop each icon has a short name under it (Profile, People, Chat, Notes, Apps, Polls, Timer, Reports, Settings, Rooms), like Slack, in English, Portuguese or Spanish by the page language. The full names stay in the tooltips. The icon grows a little under the pointer.
- The logo (when there is one) sits on a white tile, so any logo reads well on the dark bar.
- On phones, where the client overlays a 48px bar, buttons shrink to 40px and the list scrolls only vertically, with the scroll shadow drawn in the bar color.

**Sidebar panel (chat, users, notes...)**
- Flush with the icon bar and full height: no padding, no rounded corners, no shadow.
- 64px header with a bottom line, title in regular case and regular weight.
- Chat input pinned to the bottom: a one-line field that grows as you type, with an outline paper plane beside it.

**Action bar**
- 40px buttons (the size Meet uses) with 10px corners and 20px icons, the same shape as the icon bar buttons. Active buttons (microphone on, hand raised...) are blue with a white icon.
- Muted microphone and camera off show a red icon, so "I am muted" reads at a glance.
- Soft hover on the action and icon bar buttons, keeping the icon dark (the client turns it white for its darker hover).
- The presentation and media area buttons stay together in a single capsule, with the same height and corners.

**Media area panel (screen share, slides, video...)**
- Wider, and it grows with the window: 540px on a laptop and up to 720px on a large monitor, instead of a fixed 420px. On a phone it takes the screen width and never gets taller than the visible screen. The title is in regular case like the sidebar panels.
- The options are wide tiles, four per row, instead of 63px squares, so every label fits ("Share camera as content" was cut).
- Slides: the presentations are a grid (two per row on a phone, three on a laptop, more on a large monitor) that scrolls down, with the upload box and the Share button always in view, instead of one row that scrolls sideways after the second file. Every thumbnail gets the same 16:9 frame, so a portrait page (A4) sits inside it instead of stretching the row. Readable file names, and two matching small buttons under each one.
- Play video from link: a real text field in a quiet box, instead of an underline in a dashed frame.
- Whoever is not the presenter only gets a line of text and one button ("Take presenter"), so the panel is a compact 320px card there.

**Cameras**
- Videos fill their tile (`object-fit: cover`, like Meet) instead of showing black bars above and below, also while the person is speaking. In fullscreen the whole image is shown, without cropping.
- The name tag over each video gets a darker background and slightly larger text, and the presenter badge gets the same treatment.

**Avatars**
- The client tells moderators apart by a square avatar. Here every avatar is round and moderators get a small gold crown on the top right corner instead, clear of the initials.
- In the user list, the presenter gets a small blue presentation badge on the bottom right corner. The chat does not get it: its messages carry no user id, only the avatar color, which can repeat.

**Top bar**
- The options button (top right) shows a menu icon on a light tile, matching the connection and leave buttons beside it, instead of three bare dots.

**Presentation and notifications**
- The presentation area uses 10px corners, like the cameras and the action bar.
- On a short and wide window (or with a portrait page) the slide leaves empty space beside it, and the slide toolbar was as narrow as the slide, or wider. The block that holds both is now a darker "stage", like the bars of a video player, with the toolbar across its full width, so it reads as one presentation area (`--theme-stage`).
- The slide toolbar is white, with light gray tiles and darker 18px icons (Lucide chevrons, minus and plus). Previous, the slide picker and next are one segmented control, and so are the zoom buttons. Disabled buttons fade.
- Notifications use 8px corners, a soft shadow and the client's font instead of Arial.

**Menus and modals**
- Dropdown menus (options, leave, user actions, audio devices) are rounded cards with a soft shadow and rounded rows. "End session for all" and "Remove user" are red.
- Modals get a lighter, slightly blurred backdrop, the title in regular case, and 40px selects with padding (they were 28px tall, with the text on the edge).

**User list**
- "Mute all users except presenter" and "Permissions and Policies" sit one per row, so the labels are no longer cut.
- "Clear all reactions" is a quiet text action with a small icon under them, instead of a large underlined link.
- The unread dot on the icon bar is a round dot on the top right corner of the icon, instead of a pill over the user count. The user count under the users icon is brighter and bolder.

**Chat**
- Your own messages are light blue and the others gray.
- The time sits right after the name. The first message of each person is a speech bubble, with an almost square corner next to the name, and the ones that follow are round and closer together. A thin blue border shows on hover.
- The pinned message is a card with room around it and a soft shadow, with text the size of the messages.
- Reactions under a message get room above and below, a softer border and a smaller bold count, and they wrap. The emoji picker is a rounded card with the theme accent.

**Camera pages**
- The page buttons beside the camera grid are translucent instead of solid blue, and the arrows of the page bar on phones are 16px chevrons.

**Other buttons and fields**
- Every other button uses 8px corners instead of circles and capsules: top bar (start recording, connection status, leave, options), panels (mute all, polls, timer, breakout rooms, profile), slide navigation and zoom, undo/redo, menus and modals.
- Text fields and selects get the same 8px corners. The small audio device arrow on the microphone stays round.
- Panels get thin, quiet scrollbars.
- If [bbb-plugin-reaction-stack](https://github.com/bigbluebutton/bbb-plugin-reaction-stack) is installed, its reaction pills get the theme's 10px corners instead of round capsules (through its `--reaction-stack-radius` variables).

**Accessibility**
- A visible focus ring for keyboard navigation (`:focus-visible`), the same everywhere.
- Animations and transitions are turned off when the system asks for reduced motion.

**Icons**
- The icon bar and the action bar use [Lucide](https://lucide.dev) icons instead of the `bbb-icons` font: microphone, camera, screen share, reactions, raise hand, profile settings, users, chat, notes, apps, breakout rooms, polls, timer, learning dashboard and settings.
- The user list (row buttons, search, download) and the dropdown menus (user options, audio devices, options, presentation) use them too. "Make moderator" shows the same crown the moderator avatars get, "Remove user" a user with an x, "End meeting" a power icon.
- Icons keep showing the state, like the client does: a crossed microphone when muted, a crossed camera when it is off, a crossed screen when not sharing, a crossed presentation when it is minimized.
- Icons elsewhere keep the client defaults.

## Try it without installing

The plugin is hosted on GitHub Pages. Pass its manifest when you create a meeting, and that meeting loads the theme with nothing installed on the server:

```text
pluginManifests=[{"url":"https://gustavotrott.github.io/bbb-plugin-flat-theme/manifest.json"}]
```

You can add it to the `create` call in [API Mate](https://mconf.github.io/api-mate/) or in your own integration. The BigBlueButton server reads the manifest when the meeting is created, so it must reach `github.io`. The participants' browsers load the plugin from there too.

## Install on your server

These steps install from the latest [release](https://github.com/gustavotrott/bbb-plugin-flat-theme/releases/latest).

1. Download it into a folder served by nginx:

   ```bash
   sudo mkdir -p /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme
   curl -fsSL https://github.com/gustavotrott/bbb-plugin-flat-theme/releases/latest/download/bbb-plugin-flat-theme.tar.gz \
     | sudo tar xz --no-same-owner -C /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme
   ```

2. Add the manifest to `pluginManifests` in `/etc/bigbluebutton/bbb-web.properties`. Keep the other plugins you already have in the list:

   ```properties
   pluginManifests=[{"url":"https://<your-server>/plugins/bbb-plugin-flat-theme/manifest.json"}]
   ```

3. Restart bbb-web:

   ```bash
   sudo systemctl restart bbb-web
   ```

Meetings created from then on load the theme. To update, run step 1 again. No restart is needed.

You can skip the download and put the GitHub Pages manifest (`https://gustavotrott.github.io/bbb-plugin-flat-theme/manifest.json`) in `bbb-web.properties` instead. The theme then always follows the latest version on `main`.

If you used a `customStyleUrl` before, remove it from `/etc/bigbluebutton/bbb-html5.yml` and restart `bbb-apps-akka` as well: the client settings are stored per meeting by akka-apps, which only reads that file on startup.

## Use it as a custom style (CSS only)

The build also writes `dist/theme.css`: the same theme as one static stylesheet, with the icons inlined as data URIs. The client adds it as a `<link rel="stylesheet">`, so nothing runs besides the CSS. Use the plugin or the stylesheet, not both.

Pick the stylesheet for your BigBlueButton version:

| BigBlueButton | Stylesheet |
|---|---|
| 4.0.3 or later (with [#26415](https://github.com/bigbluebutton/bigbluebutton/pull/26415)) | `https://gustavotrott.github.io/bbb-plugin-flat-theme/4.0.3/theme.css` |
| 4.0.1 and 4.0.2 | `https://gustavotrott.github.io/bbb-plugin-flat-theme/4.0.1/theme.css` |
| 4.0.0 | `https://gustavotrott.github.io/bbb-plugin-flat-theme/4.0.0/theme.css` |

`https://gustavotrott.github.io/bbb-plugin-flat-theme/theme.css` always follows the newest version on `main`, and every release attaches it as `theme.css`.

The 4.0.0 and 4.0.1 stylesheets are frozen in [`versions/`](versions): new changes only go to the newest version. The 4.0.0 one reaches the client through the `data-test` attributes and ids that 4.0.0 already had, so a few details need a newer client: the presenter badge in the user list, the color of your own chat messages, the ring on the avatar of whoever speaks and the unread dot on the icon bar.

**For one user**, pass it on the `join` call:

```text
userdata-bbb_custom_style_url=https://gustavotrott.github.io/bbb-plugin-flat-theme/theme.css
```

**For the whole server**, host it yourself (or use the GitHub Pages URL):

1. Download it into a folder served by nginx:

   ```bash
   sudo mkdir -p /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme
   sudo curl -fsSL -o /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme/theme.css \
     https://gustavotrott.github.io/bbb-plugin-flat-theme/4.0.1/theme.css   # the URL for your version
   ```

2. Set `public.app.customStyleUrl` in `/etc/bigbluebutton/bbb-html5.yml`:

   ```yaml
   public:
     app:
       customStyleUrl: https://<your-server>/plugins/bbb-plugin-flat-theme/theme.css
   ```

3. Restart BigBlueButton (`sudo bbb-conf --restart`). The client settings are stored per meeting by akka-apps, which only reads `bbb-html5.yml` on startup.

Meetings created from then on load the stylesheet. To update, run step 1 again.

## Build from source

```bash
npm ci
npm run build-bundle
sudo mkdir -p /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme
sudo cp dist/* /var/www/bigbluebutton-default/assets/plugins/bbb-plugin-flat-theme/
```

Then follow steps 2 and 3 of [Install on your server](#install-on-your-server). `npm run build-bundle` also writes `dist/theme.css` and copies the frozen stylesheets from `versions/`; `npm run build-css` does only that.

## Customizing

Colors and the icon bar width are CSS variables at the top of [`src/theme.css`](src/theme.css):

| Variable | Default | Used for |
|---|---|---|
| `--theme-background` | `#102133` | Background behind the presentation, top bar and action bar |
| `--theme-nav` | `#133459` | Icon bar |
| `--theme-nav-active` | `#1E4877` | Active item in the icon bar |
| `--theme-primary` | `#0F70D7` | Active marker, active buttons, focus ring |
| `--theme-danger` | `#D93025` | Muted microphone and camera off |
| `--theme-moderator` | `#F5B700` | Moderator crown badge |
| `--theme-stage` | `#0A1622` | Empty space around the slide, inside the presentation area |
| `--theme-nav-width` | `72px` | Icon bar width |

Change them and rebuild.

## How it works

The plugin imports `src/theme.css` through `style-loader`, which injects it into `<head>` when the bundle loads. SVG icons are inlined as data URIs, so the plugin is a single JS file. The React component only registers the plugin: the client marks the presenter's avatar with `bbb-avatar--presenter`, and the badge is drawn in `theme.css`.

Some details worth knowing if you change the CSS:

- The client positions the icon bar, sidebar panel, presentation and action bar in JS, with inline `left`/`top`/`width`/`height`. The theme only changes padding, color, border, radius and inner sizes. To make the icon bar narrower, the sidebar panel moves left by the difference and grows by the same amount, so it still meets the presentation.
- The narrower icon bar only applies on screens with a mouse (`pointer: fine`, at least 768px wide). On phones the client uses a different width (48px), so the bar is left alone there.
- Selectors use the client's static `bbb-*` classes (`block`, `block__element`, `block--state`), because styled-components class names change on every client build. A few elements without one still go by their `data-test` attribute.
- Icons replace the `::before` glyph of the `icon-bbb-*` classes with an SVG used as a mask, so they still follow the text color.

Tested on BigBlueButton 4.0.2 (`v4.0.x-develop` of 11/11/2026), on desktop and on an iPhone, with plugin SDK `1.0.0-beta`.

The theme targets the client's light mode. On the test server, turning on the client's own dark mode (Settings, Application) left the whole screen blank even with this plugin removed, so dark mode was not styled.

## Releases

Every push to `main` publishes `dist/` (plugin and `theme.css`) on GitHub Pages. Pushing a `v*` tag, with the same version as `package.json` and `manifest.json`, builds the plugin and attaches `bbb-plugin-flat-theme.tar.gz` and `theme.css` to a GitHub release.

## More themes

[bbb-plugin-themes](https://github.com/gustavotrott/bbb-plugin-themes) has seven more themes built on this one: Cozy, Kids, Light, Midnight, Synthwave, Moodle and School (K-12).

## License

MIT, see [LICENSE](LICENSE). Icons are from [Lucide](https://lucide.dev), ISC license, see [src/icons/LICENSE](src/icons/LICENSE).
