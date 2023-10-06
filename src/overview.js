import embed from "vega-embed";
import createCard from "./createCard";
import consumptionMonthly from "./data/consumption_monthly.json" assert { type: "json" };
import productionMonthly from "./data/production_monthly.json" assert { type: "json" };
import consumptionAnnual from "./data/consumption_annual.json" assert { type: "json" };
import productionAnnual from "./data/production_annual.json" assert { type: "json" };

async function embedPlots() {
  const opt1 = {
    width: 500,
    height: 300,
  };
  const opt2 = {
    width: opt1.width - 5,
    height: opt1.height,
  };

  await embed("#plot1", consumptionMonthly, opt1);
  await embed("#plot2", consumptionAnnual, opt2);
  await embed("#plot3", productionMonthly, opt1);
  await embed("#plot4", productionAnnual, opt2);
}

function loadOverview() {
  const main = document.getElementById("main");
  main.textContent = "";
  main.appendChild(createCard("Monthly Trends: Consumption", "plot1"));
  main.appendChild(createCard("Annual Trends: Consumption", "plot2"));
  main.appendChild(createCard("Monthly Trends: Production", "plot3"));
  main.appendChild(createCard("Annual Trends: Production", "plot4"));
  embedPlots();
}

export default loadOverview;
