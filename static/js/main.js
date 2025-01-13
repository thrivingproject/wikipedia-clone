document.querySelector(".main-menu-icon").addEventListener("click", toggleMenu);
window.addEventListener("click", hideMenu);

/**
 * Toggle the menu when clicking on the menu icon
 */
function toggleMenu() {
  document.querySelector(".dropdown-content").classList.toggle("main-menu-show");
}

/**
 * Hide the menu when clicking outside of the menu
 * @param {*} event
 */
function hideMenu(event) {
  if (!event.target.matches(".main-menu-icon")) {
    document.querySelector(".dropdown-content").classList.remove("main-menu-show");
  }
}
