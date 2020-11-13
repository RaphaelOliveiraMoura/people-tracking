import React from "react";
import { NavLink } from "react-router-dom";

import { AiOutlineDotChart, AiOutlinePieChart } from "react-icons/ai";

import "./styles.css";

function BottomMenu() {
  return (
    <menu id="bottom-menu">
      <ul>
        <li>
          <NavLink activeClassName="active" to="/" exact>
            <AiOutlineDotChart size={26} />
            <span>Gráfico Geral</span>
          </NavLink>
        </li>
        <li>
          <NavLink activeClassName="active" to="/departaments" exact>
            <AiOutlinePieChart size={26} />
            <span>Gráficos Setores</span>
          </NavLink>
        </li>
      </ul>
    </menu>
  );
}

export default BottomMenu;
