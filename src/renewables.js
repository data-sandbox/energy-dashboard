import embed from "vega-embed";
import createCard from "./createCard";
import renewablesMonthly from "./data/renewables_monthly.json" assert { type: "json" };
import renewablesAnnual from "./data/renewables_annual.json" assert { type: "json" };

async function embedPlots() {
  const opt1 = {
    width: 500,
    height: 300,
  };
  // const opt2 = {
  //   width: opt1.width - 5,
  //   height: opt1.height,
  // };

  await embed("#plot1", renewablesMonthly, opt1);
  await embed("#plot2", renewablesAnnual, opt1);
}

function loadRenewables() {
  const main = document.getElementById("main");
  main.textContent = "";
  main.appendChild(createCard("Monthly Trends", "plot1"));
  main.appendChild(createCard("Annual Trends", "plot2"));
  embedPlots();
}

export default loadRenewables;
