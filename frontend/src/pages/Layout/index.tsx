import * as React from "react";
import { Layout as AntLayout } from "antd";



const Layout: React.FC = ({ children }) => {

  
    return (
      <AntLayout className="main-layout">
        <AntLayout className="right-part-layout">
          <AntLayout.Content className="main-layout-content">
            <React.Suspense fallback={"LOADING..."}>{children}</React.Suspense>
          </AntLayout.Content>
        </AntLayout>
      </AntLayout>
    );
  };
  
  export default Layout;