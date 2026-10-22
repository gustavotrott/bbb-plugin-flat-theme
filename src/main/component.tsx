import * as React from 'react';

import { BbbPluginSdk } from 'bigbluebutton-html-plugin-sdk';

interface MainComponentProps {
  pluginUuid: string;
}

// The theme is pure CSS (see ../theme.css). The client marks the presenter's
// avatar with .bbb-avatar--presenter, so there is nothing left to do here.
function MainComponent(
  { pluginUuid: uuid }: MainComponentProps,
): React.ReactElement<MainComponentProps> {
  BbbPluginSdk.initialize(uuid);

  return null;
}

export default MainComponent;
