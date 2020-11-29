import { RouteProps } from "react-router-dom";

export interface IMenu {
  items: Array<IMenuItem>;
}

export interface IMenuItem {
  id: string;
  title: string;
  tooltip: string;
  icon: string;
  path?: string;
  exact?: boolean;
}

export type TRoutes = Array<IRoute>;

interface IRoute extends RouteProps {
  id: string;
  componentPath?: string;
  helpUrl?: string;
}