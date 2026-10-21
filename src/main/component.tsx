import * as React from 'react';

import { BbbPluginSdk } from 'bigbluebutton-html-plugin-sdk';

interface MainComponentProps {
  pluginUuid: string;
}

// The theme is pure CSS (see ../theme.css). The plugin only needs to register
// itself with the client so it is reported as loaded.
function MainComponent(
  { pluginUuid: uuid }: MainComponentProps,
): React.ReactElement<MainComponentProps> {
  BbbPluginSdk.initialize(uuid);

  return null;
}

export default MainComponent;
