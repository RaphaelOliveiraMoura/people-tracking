import styled, { css } from "styled-components";

const containerPositionStyles = {
  top: css`
    padding-top: 36px;
    padding-bottom: 36px;
  `,
  bottom: css`
    margin-top: 18px;
    padding-top: 18px;
  `,
};

const detailsPositionStyles = {
  top: css`
    bottom: 16px;
  `,
  bottom: css`
    top: 0;
  `,
};

export const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  position: relative;
  background: white;

  ${({ position }) => containerPositionStyles[position]}

  &::before {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 42px;
    height: 4px;
    border-radius: 4px;
    background: #cc1d1d;

    ${({ position }) => detailsPositionStyles[position]}
  }
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
