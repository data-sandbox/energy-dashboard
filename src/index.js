import "./style.css";
import loadOverview from "./overview";
import loadPrices from "./prices";
import loadRenewables from "./renewables";
import loadAbout from "./about";
import setActiveButton from "./setActive";

function addNavEvents() {
  const navBtns = document.querySelectorAll(".btn-nav");
  navBtns.forEach((btn) => {
    btn.addEventListener("click", handleNavClick);
  });
}

function handleNavClick(e) {
  const navItem = e.target.id;

  switch (navItem) {
    case "overview":
      loadOverview();
      break;
    case "prices":
      loadPrices();
      break;
    case "renewables":
      loadRenewables();
      break;
    case "about":
      loadAbout();
      break;
    default:
      loadOverview();
  }

  setActiveButton(this);
}

loadOverview();
setActiveButton(document.querySelector(".btn-nav.overview"));
addNavEvents();
