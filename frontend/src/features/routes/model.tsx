import { createStore, createEvent, createEffect, attach } from "effector";

import { TRoutes, IMenu } from './types';


import { data } from "./data";

export const initStore = createEvent();
export const $routes = createStore<TRoutes>(data.items.map(
    ({ id, path, component, helpUrl }) => ({ id, path, component, helpUrl, exact: true })
));

export const $menu = createStore<IMenu>({ items: data.items.map(item => (
  {
    id: item.id,
    title: item.title,
    icon: item.icon,
    path: item.path,
    tooltip: item.tooltip,
    helpUrl: item.helpUrl,
    exact: item.exact
  }
)) });


$routes.on(initStore, () => {
    const routerItems: TRoutes = [];
  
    data.items.forEach(
      ({ id, path, component, helpUrl }) => {
        // const hasPermission = await checkPermission(permission);
        // if (!hasPermission) return;
        routerItems.push({ id, path, component, helpUrl, exact: true });
      }
    );
  
    // data.routes.forEach(({ id, path, component }) => {
    // //   const hasPermission = await checkPermission(permission);
    // //   if (!hasPermission) return;
    //   routerItems.push({ id, path, component, exact: true });
    // });
    return routerItems;
  });