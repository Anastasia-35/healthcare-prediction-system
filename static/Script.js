document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Get form data
        const formData = new FormData(form);

        // Send data to Flask using Fetch API
        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())  // Expect JSON response
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <h3>${data.prediction_text}</h3>
                    <h4>Diabetes Type: ${data.diabetes_type}</h4>
                    <p><strong>Diet Recommendations:</strong> ${data.diet}</p>
                    <p><strong>Exercise Recommendations:</strong> ${data.exercise}</p>
                    <p><strong>Medication Recommendations:</strong> ${data.medication}</p>
                `;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<p style="color: red;">Error: ${error}</p>`;
        });
    });
});
