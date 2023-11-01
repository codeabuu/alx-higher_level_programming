document.addEventListener("DOMContentLoaded", function() {
            // Wait for the document to be fully loaded
            var headerElement = document.querySelector("header");
            
            if (headerElement) {
                headerElement.style.color = "#FF0000"; // Set text color to red
            } else {
                console.error("Header element not found.");
            }
        });
