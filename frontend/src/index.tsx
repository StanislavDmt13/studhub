import * as React from "react";
import { render } from "react-dom";

import App from './App';

const root = window.document.getElementById("root");


const init = async () => {
  
  render(<App />, root);
};

init();

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () =>
    navigator.serviceWorker.register("service-worker.js")
  );
}
