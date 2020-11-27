import * as React from "react";

import { BrowserRouter } from "react-router-dom";

import Layout from "./pages/Layout";
import Router from './features/routes';

const App = () => {

  return (
      <BrowserRouter>
            <Layout>
                <Router />
            </Layout>
      </BrowserRouter>
  );
};

export default App;