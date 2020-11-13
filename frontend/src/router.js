import React from "react";

import { Switch, Route } from "react-router-dom";

import Main from "./pages/Main";
import Departaments from "./pages/Departaments";

function src() {
  return (
    <Switch>
      <Route path="/" component={Main} exact />
      <Route path="/departaments" component={Departaments} exact />
    </Switch>
  );
}

export default src;
