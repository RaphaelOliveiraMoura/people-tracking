import React from "react";

import ThingSpeakChart from "../../components/ThingSpeakChart";
import BubbleLegend from "../../components/BubbleLegend";

import "./styles.css";

function Main() {
  return (
    <div id="main-page">
      <ThingSpeakChart plot_id="373454" />
      <BubbleLegend />
    </div>
  );
}

export default Main;
