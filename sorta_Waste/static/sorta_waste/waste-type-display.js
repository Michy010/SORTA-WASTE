document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("wasteBtn").addEventListener("click", function() {
    document.querySelector(".waste-options").style.display = "flex";
    document.querySelector(".amount-options").style.display = "none";
  });

  document.getElementById("amountBtn").addEventListener("click", function() {
    document.querySelector(".waste-options").style.display = "none";
    document.querySelector(".amount-options").style.display = "flex";
  });
});