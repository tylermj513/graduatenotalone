const counterContainer = document.querySelector<HTMLDivElement>(".website-counter");
const resetButton = document.querySelector<HTMLButtonElement>("#reset");
let visitCount = localStorage.getItem("page_view");

// Check if page_view entry is present
if (visitCount) {
  visitCount = String(Number(visitCount) + 1);
  localStorage.setItem("page_view", visitCount);
} else {
  visitCount = "1";
  localStorage.setItem("page_view", visitCount);
}
if (counterContainer) {
  counterContainer.innerHTML = visitCount;
}

// Adding onClick event listener
if (resetButton) {
  resetButton.addEventListener("click", () => {
    visitCount = "1";
    localStorage.setItem("page_view", visitCount);
    if (counterContainer) {
      counterContainer.innerHTML = visitCount;
    }
  });
}
