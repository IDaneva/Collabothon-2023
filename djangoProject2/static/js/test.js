setFilter();
setFilter(2);

function setFilter(filterNum = "") {
  document.addEventListener("DOMContentLoaded", function () {
    const customSelect = document.querySelector(`.custom-select${filterNum}`);
    const trigger = customSelect.querySelector(`.select-trigger${filterNum}`);
    const options = customSelect.querySelector(`.select-options${filterNum}`);
    const optionItems = customSelect.querySelectorAll(
      `.select-options${filterNum} li`
    );

    // Toggle options display on trigger click
    trigger.addEventListener("click", function () {
      options.style.display =
        options.style.display === "block" ? "none" : "block";
    });

    // Handle option selection
    optionItems.forEach((item) => {
      item.addEventListener("click", function () {
        trigger.textContent = item.textContent;
        options.style.display = "none";

        // Optionally, you can capture the selected value (e.g., item.getAttribute("data-value"))
      });
    });
  });
}