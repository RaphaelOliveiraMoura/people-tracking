import React from "react";

import { BrowserRouter } from "react-router-dom";

import Router from "./router";
import BottomMenu from "./components/BottomMenu";

import "./global/styles.css";

function App() {
  return (
    <BrowserRouter>
      <Router />
      <BottomMenu />
    </BrowserRouter>
  );
}

export default App;
