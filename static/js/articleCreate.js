const textInput = document.getElementById("article-create-title-input");
const submitButton = document.getElementById("article-create-submit");

textInput.addEventListener("input", toggleButtonDisabled);

/**
 * Enable the submit button if the text input is not empty
 */
function toggleButtonDisabled() {
  if (textInput.value.trim() !== "") {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}
