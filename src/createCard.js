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

export default createCard;
