import React from "react";

import { Container, LegendItem } from "./styles";

function BubbleLegend() {
  const legends = [
    { title: "Manhã", color: "#0f0", description: "06:00 ~ 12:00" },
    { title: "Tarde", color: "#f00", description: "12:00 ~ 18:00" },
    { title: "Noite", color: "#00f", description: "18:00 ~ 06:00" },
  ];

  return (
    <Container>
      {legends.map((legend) => (
        <LegendItem color={legend.color}>
          <h1>
            <div className="circle"></div>
            <strong>{legend.title}</strong>
          </h1>
          <span>{legend.description}</span>
        </LegendItem>
      ))}
    </Container>
  );
}

export default BubbleLegend;
