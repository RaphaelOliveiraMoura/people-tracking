import React from "react";

import ThingSpeakChart from "../../components/ThingSpeakChart";

import { Container, BubbleLegendStyled } from "./styles";

function Departaments() {
  return (
    <Container>
      <BubbleLegendStyled position="top" />
      <ThingSpeakChart plot_id="375594" refresh={false} />
      <ThingSpeakChart plot_id="375595" refresh={false} />
      <ThingSpeakChart plot_id="375597" refresh={false} />
      <ThingSpeakChart plot_id="375598" refresh={false} />
    </Container>
  );
}

export default Departaments;
