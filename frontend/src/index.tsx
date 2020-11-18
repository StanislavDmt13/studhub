import * as React from "react";
import { render } from "react-dom";

const root = window.document.getElementById("root");

const init = async () => {
  render(<h1>I Work</h1>, root);
};

init();

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () =>
    navigator.serviceWorker.register("service-worker.js")
  );
}
