import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin-top: 26px;
`;

export const LegendItem = styled.div`
  h1 {
    display: flex;
    align-items: center;
  }

  strong {
    margin-left: 5px;
    font-size: 14px;
  }

  .circle {
    border-radius: 50%;
    width: 15px;
    height: 15px;
    background: ${({ color }) => color};
  }

  span {
    font-size: 10px;
    color: #888;
  }
`;
