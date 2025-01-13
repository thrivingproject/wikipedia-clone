document.querySelector(".main-menu-icon").addEventListener("click", function () {
  document.querySelector(".dropdown-content").classList.toggle("main-menu-show");
});

window.addEventListener("click", function (event) {
  if (!event.target.matches(".main-menu-icon")) {
    document.querySelector(".dropdown-content").classList.remove("main-menu-show");
  }
});
