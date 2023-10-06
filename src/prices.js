import embed from "vega-embed";
import createCard from "./createCard";
import pricesMonthly from "./data/prices_monthly.json" assert { type: "json" };
import gasMonthly from "./data/gas_monthly.json" assert { type: "json" };
import pricesAnnual from "./data/prices_annual.json" assert { type: "json" };
import gasAnnual from "./data/gas_annual.json" assert { type: "json" };

async function embedPlots() {
  const opt1 = {
    width: 500,
    height: 300,
  };
  const opt2 = {
    width: opt1.width - 5,
    height: opt1.height,
  };

  await embed("#plot1", pricesMonthly, opt1);
  await embed("#plot2", pricesAnnual, opt1);
  await embed("#plot3", gasMonthly, opt1);
  await embed("#plot4", gasAnnual, opt2);
}

function loadPrices() {
  const main = document.getElementById("main");
  main.textContent = "";
  main.appendChild(createCard("Monthly Trends: Electricity", "plot1"));
  main.appendChild(createCard("Annual Trends: Electricity", "plot2"));
  main.appendChild(createCard("Monthly Trends: Gasoline", "plot3"));
  main.appendChild(createCard("Annual Trends: Gasoline", "plot4"));
  embedPlots();
}

export default loadPrices;
