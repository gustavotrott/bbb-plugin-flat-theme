import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
// style-loader injects the theme into <head> as soon as the bundle runs
import './theme.css';
import MainComponent from './main/component';

const uuid = document.currentScript?.getAttribute('uuid') || 'root';

const pluginName = document.currentScript?.getAttribute('pluginName') || 'plugin';

const root = ReactDOM.createRoot(document.getElementById(uuid));
root.render(
  <MainComponent {...{
    pluginUuid: uuid,
    pluginName,
  }}
  />,
);
