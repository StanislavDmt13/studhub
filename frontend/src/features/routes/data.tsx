
import { RouteComponentProps } from "react-router-dom";
import { lazy } from "react";

type TypeNavigationDataItem = {
  id: string;
  title: string;
  icon: string;
  path: string;
  paths?: string[];
  exact?: boolean;
  helpUrl?: string;
  permission?: string;
  tooltip?: string;
  component?:
    | React.ComponentType<RouteComponentProps<any>>
    | React.ComponentType<any>;
};

type TypeRoute = {
  id: string;
  path: string;
  exact?: boolean;
  permission?: string;
  component?:
    | React.ComponentType<RouteComponentProps<any>>
    | React.ComponentType<any>
};

interface INavigationData {
  items: Array<TypeNavigationDataItem>;
  routes: Array<TypeRoute>;
}


export const data: INavigationData = {
    items: [
      {
        id: "1",
        title: "HOME",
        icon: "",
        path: '',
        component: lazy(() => import("../../pages/Home")),
        helpUrl: "home",
        // permission: "",
        tooltip: "HOME_TITLE",
        exact: true
      }],
      routes: [
        {
            id: "1",
            path: '',
            component: lazy(() => import("../../pages/Home"))
            // permission: "dc-predict-plan"
        },
      ]
    }