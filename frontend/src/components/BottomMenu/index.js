import React from "react";

import { AiOutlineDotChart, AiOutlinePieChart } from "react-icons/ai";

import "./styles.css";

function BottomMenu() {
  return (
    <menu id="bottom-menu">
      <ul>
        <li>
          <div>
            <AiOutlineDotChart size={26} />
            <span>Gráfico Geral</span>
          </div>
        </li>
        <li>
          <div>
            <AiOutlinePieChart size={26} />
            <span>Gráficos setores</span>
          </div>
        </li>
      </ul>
    </menu>
  );
}

export default BottomMenu;
