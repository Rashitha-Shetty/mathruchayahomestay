// Function to generate list items
function generateListItems() {
  data = document.querySelectorAll(".all_intrest");
  data.forEach((entry) => {
    // Add click event to reveal details
    entry.addEventListener("click", () => {
      const details = entry.querySelector(".details");
      details.style.display =
        details.style.display === "block" ? "none" : "block";
    });
  });
}

// Initial generation of list items
generateListItems();



 // JavaScript function to show and hide the message box
 function showMessage() {
  var messageBox = document.getElementById('messageBox');
  messageBox.style.display = 'block';
  setTimeout(function() {
      messageBox.style.display = 'none';
  }, 5000); // 5000 milliseconds = 5 seconds
}

// Call showMessage function to display the message box
showMessage();