function toggleDarkMode() {
  const darkModeToggle = document.getElementById("darkModeToggle");
  const body = document.body;

  const userMode = getUserModeFromStorage();
  if (userMode === "darkMode") {
    body.classList.add("dark-mode");
  }

  darkModeToggle.addEventListener("click", function () {
    body.classList.toggle("dark-mode");
    updateUserMode();
    updateButtonBackground(); // Call the updateButtonBackground function when the mode is toggled
  });

  // Call updateButtonBackground when the page loads
  updateButtonBackground();
}

function updateUserMode() {
  const body = document.body;
  const userMode = body.classList.contains("dark-mode")
    ? "darkMode"
    : "lightMode";
  localStorage.setItem("userMode", userMode);
}

function getUserModeFromStorage() {
  return localStorage.getItem("userMode");
}

function updateButtonBackground() {
  const darkModeToggle = document.getElementById("darkModeToggle");
  const body = document.body;
  const isDarkMode = body.classList.contains("dark-mode");

  if (isDarkMode) {
    darkModeToggle.style.backgroundColor = "#000000"; // Dark background color in light mode
    darkModeToggle.style.color = "#ffffff"; // Light text color in light mode
  } else {
    darkModeToggle.style.backgroundColor = "#ffffff"; // Light background color in dark mode
    darkModeToggle.style.color = "#000000"; // Dark text color in dark mode
  }
}

// Call the function when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", toggleDarkMode);

