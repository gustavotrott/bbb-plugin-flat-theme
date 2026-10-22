import * as React from 'react';
import { useEffect } from 'react';

import { BbbPluginSdk } from 'bigbluebutton-html-plugin-sdk';

interface MainComponentProps {
  pluginUuid: string;
}

const PRESENTER_STYLE_ID = 'flat-theme-presenter';

// The theme is pure CSS (see ../theme.css). The only thing CSS cannot know is
// who the presenter is: the client does not put it on the avatar. So the
// plugin turns the presenter's user list row on through a CSS variable, and
// theme.css draws the badge.
function MainComponent(
  { pluginUuid: uuid }: MainComponentProps,
): React.ReactElement<MainComponentProps> {
  BbbPluginSdk.initialize(uuid);
  const pluginApi = BbbPluginSdk.getPluginApi(uuid);
  const { data } = pluginApi.useUsersBasicInfo();

  const presenterIds = (data?.user ?? [])
    .filter((user) => user.presenter)
    .map((user) => user.userId)
    .join(',');

  useEffect(() => {
    let style = document.getElementById(PRESENTER_STYLE_ID);
    if (!style) {
      style = document.createElement('style');
      style.id = PRESENTER_STYLE_ID;
      document.head.appendChild(style);
    }
    const selectors = presenterIds
      .split(',')
      .filter(Boolean)
      .map((id) => `[data-id="${CSS.escape(id)}"]`);
    style.textContent = selectors.length
      ? `${selectors.join(',\n')} { --theme-presenter-badge: block; }`
      : '';
  }, [presenterIds]);

  useEffect(() => () => document.getElementById(PRESENTER_STYLE_ID)?.remove(), []);

  return null;
}

export default MainComponent;
