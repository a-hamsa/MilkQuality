// Function to handle form submission and make predictions
async function handleSubmit(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get form inputs
    const ph_value = parseFloat(document.getElementById('ph_value').value);
    const temperature = parseFloat(document.getElementById('temperature').value);
    const taste = parseFloat(document.getElementById('taste').value);
    const odor = parseFloat(document.getElementById('odor').value);
    const fat = parseFloat(document.getElementById('fat').value);
    const turbidity = parseFloat(document.getElementById('turbidity').value);
    const red = parseFloat(document.getElementById('red').value);

    // Make prediction
    const result = await predict(ph_value, temperature, taste, odor, fat, turbidity, red);

    // Display prediction result
    displayResult(result);
}

// Function to make predictions
async function predict(ph_value, temperature, taste, odor, fat, turbidity, red) {
    // Load the model
    const model = await tf.loadLayersModel('/../../model_MooQ_dt.model');

    // Prepare input data
    const inputData = tf.tensor2d([[ph_value, temperature, taste, odor, fat, turbidity, red]]);

    // Make predictions
    const output = model.predict(inputData);

    // Process output
    const result = output.dataSync();

    // Return the result
    return result;
}

// Function to display prediction result
function displayResult(result) {
    const gradeOutput = document.getElementById('gradeOutput');
    gradeOutput.textContent = `Grade: ${result}`;
}

// Add event listener to the form
document.getElementById('qualityForm').addEventListener('submit', handleSubmit);
