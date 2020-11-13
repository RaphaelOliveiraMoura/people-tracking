import React from "react";

import ThingSpeakChart from "../../components/ThingSpeakChart";

import { Container, BubbleLegendStyled } from "./styles";

function Departaments() {
  return (
    <Container>
      <BubbleLegendStyled position="top" />
      <ThingSpeakChart plot_id="373454" refresh={false} />
      <ThingSpeakChart plot_id="373454" refresh={false} />
      <ThingSpeakChart plot_id="373454" refresh={false} />
      <ThingSpeakChart plot_id="373454" refresh={false} />
    </Container>
  );
}

export default Departaments;
