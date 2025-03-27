from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import traceback

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Load model and scaler only once
@app.before_first_request
def load_model():
    """Load trained model and preprocessing tools before first request."""
    global model, scaler
    try:
        model = joblib.load("Assets/Models/logistic_regression.pkl")
        scaler = joblib.load("Assets/Models/scaler.pkl")
        print("✅ Model and Scaler Loaded Successfully!")
    except Exception as e:
        print("❌ Error Loading Model/Scaler:", e)
        traceback.print_exc()

# ✅ Define expected input features
num_cols = ['AGE', 'OXYGEN_SATURATION', 'ENERGY_LEVEL', 'STRESS_IMMUNE']
all_features = num_cols + [
    'SMOKING', 'FINGER_DISCOLORATION', 'MENTAL_STRESS', 'EXPOSURE_TO_POLLUTION', 
    'LONG_TERM_ILLNESS', 'IMMUNE_WEAKNESS', 'BREATHING_ISSUE', 'ALCOHOL_CONSUMPTION', 
    'THROAT_DISCOMFORT', 'CHEST_TIGHTNESS', 'FAMILY_HISTORY', 'SMOKING_FAMILY_HISTORY'
]

@app.route('/')
def home():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle user input, process it, and return the model prediction."""
    try:
        # ✅ Extract user input safely
        user_data = {}
        for feature in all_features:
            if feature in request.form:
                user_data[feature] = int(request.form[feature])  # Convert to integer
            else:
                return jsonify({"error": f"Missing input for {feature}"}), 400

        # ✅ Convert input into a DataFrame
        new_df = pd.DataFrame([user_data])

        # ✅ Scale numerical features
        new_df[num_cols] = scaler.transform(new_df[num_cols])

        # ✅ Predict using the trained model
        prediction = model.predict(new_df)[0]
        probability = model.predict_proba(new_df)[:, 1][0]

        # ✅ Format the output
        result = "YES" if prediction == 1 else "NO"
        confidence = f"{probability * 100:.2f}%"

        return render_template('index.html', prediction=result, confidence=confidence)

    except Exception as e:
        print("❌ Error in Prediction:", e)
        traceback.print_exc()
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == "__main__":
    app.run(debug=True)
