import styled from "styled-components";
import BubbleLegend from "../../components/BubbleLegend";

export const Container = styled.div`
  overflow-y: scroll;
  overflow-x: hidden;
  height: calc(100% - 70px);

  #thingspeak-chart,
  .shimmer {
    margin: 12px 0;
  }
`;

export const BubbleLegendStyled = styled(BubbleLegend)`
  position: sticky;
  top: 0;
  z-index: 5;
`;
