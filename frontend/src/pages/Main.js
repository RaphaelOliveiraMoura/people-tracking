import React from "react";

import BottomMenu from "../components/BottomMenu";

function Main() {
  return (
    <div>
      <iframe
        title="Main chart"
        width="100%"
        height="260"
        src="https://thingspeak.com/apps/matlab_visualizations/373454"
        scrolling="no"
      ></iframe>
      <BottomMenu />
    </div>
  );
}

export default Main;
