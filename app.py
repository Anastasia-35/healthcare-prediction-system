from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Define file paths
model_path = "stacking_model1.pkl"
scaler_path = "scaler1.pkl"

# Check if model and scaler files exist
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found!")

if not os.path.exists(scaler_path):
    raise FileNotFoundError(f"Scaler file '{scaler_path}' not found!")

# Load trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        input_data = [float(x) for x in request.form.values()]
        input_array = np.array(input_data).reshape(1, -1)

        # Scale input data
        input_scaled = scaler.transform(input_array)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1] * 100  # Confidence %

        # Determine result
        result = "Diabetes Detected" if prediction == 1 else "No Diabetes"
        
        # Medical recommendations
        if prediction == 1:
            diabetes_type = "Consult further tests to determine the type of diabetes"
            diet = "Focus on a low-carb, high-fiber diet. Include vegetables, whole grains, and lean proteins."
            exercise = "Regular exercise like walking, swimming, or cycling for at least 30 minutes daily."
            medication = "Consider medications such as Metformin, but a specialist consultation is required before prescribing."
        else:
            diabetes_type = "No Diabetes"
            diet = "Maintain a balanced diet with regular meals and healthy snacks."
            exercise = "Regular physical activity such as walking or swimming."
            medication = "No medication required; focus on a healthy lifestyle."

        # Return JSON response
        return jsonify({
            "prediction_text": f"{result} ({probability:.2f}% confidence)",
            "diabetes_type": diabetes_type,
            "diet": diet,
            "exercise": exercise,
            "medication": medication
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message in JSON format

if __name__ == '__main__':
    app.run(debug=True)
