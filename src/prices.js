import embed from "vega-embed";
import pricesMonthly from "./data/prices_monthly.json" assert { type: "json" };
import gasMonthly from "./data/gas_monthly.json" assert { type: "json" };
import pricesAnnual from "./data/prices_annual.json" assert { type: "json" };
import gasAnnual from "./data/gas_annual.json" assert { type: "json" };

function createCard(title, id) {
  const card = document.createElement("div");
  card.classList.add("card");

  const titleBlock = document.createElement("div");
  titleBlock.classList.add("card-title");
  const cardTitle = document.createElement("p");
  cardTitle.textContent = title;

  const plotBlock = document.createElement("div");
  plotBlock.classList.add("plot");
  plotBlock.setAttribute("id", id);

  titleBlock.appendChild(cardTitle);
  card.appendChild(titleBlock);
  card.appendChild(plotBlock);

  return card;
}

async function embedPlots() {
  const opt1 = {
    width: 500,
    height: 300,
  };
  // const opt2 = {
  //   width: opt1.width - 5,
  //   height: opt1.height,
  // };

  await embed("#plot1", pricesMonthly, opt1);
  await embed("#plot2", pricesAnnual, opt1);
  await embed("#plot3", gasMonthly, opt1);
  await embed("#plot4", gasAnnual, opt1);
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
