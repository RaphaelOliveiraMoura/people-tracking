import React from "react";

import BottomMenu from "../../components/BottomMenu";
import ThingSpeakChart from "../../components/ThingSpeakChart";
import BubbleLegend from "../../components/BubbleLegend";

import "./styles.css";

function Main() {
  return (
    <div id="main-page">
      <ThingSpeakChart plot_id="373454" />
      <BottomMenu />
      <BubbleLegend />
    </div>
  );
}

export default Main;
