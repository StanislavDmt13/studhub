import * as React from "react";
import { Switch, Route } from "react-router-dom";

import { useStore } from "effector-react";
import { $routes } from "./model";

export { $routes } from "./model";

export type { IMenuItem } from "./types";

export { history } from "./history";

import { initStore } from './model';

const Router = () => {

  initStore();
  
  const routes = useStore($routes);

    // const routes = [
    //     {
    //         'id': 1,
    //         'path': '',
    //         'component': React.lazy(() => import("../../pages/Home")),
    //         'helpUrl': ''
    //     }
    // ]

  return (
    <Switch>
      {routes.map(({ id, path, component: Component, helpUrl, ...props }) => (
        <Route
          key={id}
          path={`${path}`}
          {...props}
          render={() => {
            //@ts-ignore
            return <Component/>;
          }}
        />
      ))}
    </Switch>
  );
};

export default Router;