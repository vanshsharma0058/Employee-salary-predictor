from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model
model = joblib.load("model.pkl")

# Home route - renders form
@app.route("/")
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from form
        exp = float(request.form["experience"])
        test = float(request.form["test_score"])
        interview = float(request.form["interview_score"])
    except ValueError:
        # In case user enters text instead of numbers
        return render_template("index.html", prediction_text="❌ Please enter valid numbers!")

    # Create a DataFrame with correct column names for sklearn
    input_df = pd.DataFrame([[exp, test, interview]],
                            columns=['experience', 'test_score', 'interview_score'])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Send result back to HTML
    return render_template("index.html", prediction_text=f"✅ Predicted Salary: ₹{int(prediction)}")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)