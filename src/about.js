function createAbout() {
  const about = document.createElement("div");
  about.classList.add("about");

  const heading = document.createElement("h1");
  heading.textContent = "⚡️ How This Dashboard Works";

  const text1 = document.createElement("p");
  text1.textContent = `This dashboard is created using data from the U.S. Energy Information Administration (EIA) which provides a plethora of interesting energy statistics. The time-series data is updated monthly and obtained using the EIA's free RESTful API.`;

  const text2 = document.createElement("p");
  text2.textContent += `The API data is accessed using Python. The plots are created using the Python library Altair for its rich interactivity features. Each plot is then exported as a JSON file, which is read by a JavaScript file that embeds the plot into the web page.`;

  const text3 = document.createElement("p");
  text3.textContent += `The overall dashboard is a single-page application built using vanilla JavaScript, HTML, and CSS. In this implementation only a single web document is loaded and the content is dynamically updated via JavaScript as the user interacts with the navigation buttons.`;

  const elements = [heading, text1, text2, text3];

  elements.forEach((element) => about.appendChild(element));

  return about;
}

function loadAbout() {
  const main = document.getElementById("main");
  main.textContent = "";
  main.appendChild(createAbout());
}

export default loadAbout;
