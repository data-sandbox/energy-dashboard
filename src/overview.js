import embed from "vega-embed";
import monthly from "./data/overview_monthly.json" assert { type: "json" };
import annual from "./data/overview_annual.json" assert { type: "json" };

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
  const opt2 = {
    width: opt1.width - 5,
    height: opt1.height,
  };

  await embed("#plot1", monthly, opt1);
  await embed("#plot2", annual, opt2);
}

function loadOverview() {
  const main = document.getElementById("main");
  main.textContent = "";
  main.appendChild(createCard("Monthly Trends", "plot1"));
  main.appendChild(createCard("Annual Trends", "plot2"));

  embedPlots();
}

export default loadOverview;
