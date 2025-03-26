from flask import Flask, request, render_template
import pandas as pd
import joblib

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Load trained model and preprocessing tools
model = joblib.load("Assets/Models/logistic_regression.pkl")
scaler = joblib.load("Assets/Models/scaler.pkl")

# ✅ Define expected input features
categorical_cols = ['GENDER', 'SMOKING', 'EXPOSURE_TO_POLLUTION', 'LONG_TERM_ILLNESS', 
                    'FAMILY_HISTORY', 'SMOKING_FAMILY_HISTORY', 'ALCOHOL_CONSUMPTION']

num_cols = ['AGE', 'OXYGEN_SATURATION', 'ENERGY_LEVEL', 'STRESS_IMMUNE']

@app.route('/')
def home():
    return render_template('index.html')  # Load the frontend UI

@app.route('/predict', methods=['POST'])
def predict():
    # ✅ Extract user input from the form
    user_data = {
        'AGE': int(request.form['AGE']),
        'SMOKING': int(request.form['SMOKING']),
        'FINGER_DISCOLORATION': int(request.form['FINGER_DISCOLORATION']),
        'MENTAL_STRESS': int(request.form['MENTAL_STRESS']),
        'EXPOSURE_TO_POLLUTION': int(request.form['EXPOSURE_TO_POLLUTION']),
        'LONG_TERM_ILLNESS': int(request.form['LONG_TERM_ILLNESS']),
        'ENERGY_LEVEL': int(request.form['ENERGY_LEVEL']),
        'IMMUNE_WEAKNESS': int(request.form['IMMUNE_WEAKNESS']),
        'BREATHING_ISSUE': int(request.form['BREATHING_ISSUE']),
        'ALCOHOL_CONSUMPTION': int(request.form['ALCOHOL_CONSUMPTION']),
        'THROAT_DISCOMFORT': int(request.form['THROAT_DISCOMFORT']),
        'OXYGEN_SATURATION': int(request.form['OXYGEN_SATURATION']),
        'CHEST_TIGHTNESS': int(request.form['CHEST_TIGHTNESS']),
        'FAMILY_HISTORY': int(request.form['FAMILY_HISTORY']),
        'SMOKING_FAMILY_HISTORY': int(request.form['SMOKING_FAMILY_HISTORY']),
        'STRESS_IMMUNE': int(request.form['STRESS_IMMUNE'])
    }

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

if __name__ == "__main__":
    app.run(debug=True)
