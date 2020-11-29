import * as React from "react";
import { Layout as AntLayout } from "antd";


import Header from './containers/Header';
import Footer from './containers/Footer';

const Layout: React.FC = ({ children }) => {

  
    return (
      <AntLayout className="main-layout">
          <Header />
          <AntLayout.Content className="main-layout-content">
            <React.Suspense fallback={"LOADING..."}>{children}</React.Suspense>
          </AntLayout.Content>
          <Footer/>
      </AntLayout>
    );
  };
  
  export default Layout;