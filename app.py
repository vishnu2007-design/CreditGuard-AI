from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained Decision Tree model
model_path = os.path.join(
    os.path.dirname(__file__),
    "credit_card_default_model.pkl"
)

model = joblib.load(model_path)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction Page
# -----------------------------
@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


# -----------------------------
# Prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Customer Information
        LIMIT_BAL = float(request.form["LIMIT_BAL"])
        SEX = int(request.form["SEX"])
        EDUCATION = int(request.form["EDUCATION"])
        MARRIAGE = int(request.form["MARRIAGE"])
        AGE = int(request.form["AGE"])

        # Repayment History
        PAY_0 = int(request.form["PAY_0"])
        PAY_2 = int(request.form["PAY_2"])
        PAY_3 = int(request.form["PAY_3"])
        PAY_4 = int(request.form["PAY_4"])
        PAY_5 = int(request.form["PAY_5"])
        PAY_6 = int(request.form["PAY_6"])

        # Billing Information
        BILL_AMT1 = float(request.form["BILL_AMT1"])
        BILL_AMT2 = float(request.form["BILL_AMT2"])
        BILL_AMT3 = float(request.form["BILL_AMT3"])
        BILL_AMT4 = float(request.form["BILL_AMT4"])
        BILL_AMT5 = float(request.form["BILL_AMT5"])
        BILL_AMT6 = float(request.form["BILL_AMT6"])

        # Payment Information
        PAY_AMT1 = float(request.form["PAY_AMT1"])
        PAY_AMT2 = float(request.form["PAY_AMT2"])
        PAY_AMT3 = float(request.form["PAY_AMT3"])
        PAY_AMT4 = float(request.form["PAY_AMT4"])
        PAY_AMT5 = float(request.form["PAY_AMT5"])
        PAY_AMT6 = float(request.form["PAY_AMT6"])


        # -----------------------------
        # Feature Engineering
        # -----------------------------

        # Total payment amount
        TOTAL_PAY_AMT = (
            PAY_AMT1 +
            PAY_AMT2 +
            PAY_AMT3 +
            PAY_AMT4 +
            PAY_AMT5 +
            PAY_AMT6
        )

        # Maximum payment delay
        MAX_PAY_DELAY = max(
            PAY_0,
            PAY_2,
            PAY_3,
            PAY_4,
            PAY_5,
            PAY_6
        )

        # Total bill amount
        TOTAL_BILL_AMT = (
            BILL_AMT1 +
            BILL_AMT2 +
            BILL_AMT3 +
            BILL_AMT4 +
            BILL_AMT5 +
            BILL_AMT6
        )


        # -----------------------------
        # Create Input DataFrame
        # -----------------------------

        data = {
            "LIMIT_BAL": LIMIT_BAL,
            "SEX": SEX,
            "EDUCATION": EDUCATION,
            "MARRIAGE": MARRIAGE,
            "AGE": AGE,

            "PAY_0": PAY_0,
            "PAY_2": PAY_2,
            "PAY_3": PAY_3,
            "PAY_4": PAY_4,
            "PAY_5": PAY_5,
            "PAY_6": PAY_6,

            "BILL_AMT1": BILL_AMT1,
            "BILL_AMT2": BILL_AMT2,
            "BILL_AMT3": BILL_AMT3,
            "BILL_AMT4": BILL_AMT4,
            "BILL_AMT5": BILL_AMT5,
            "BILL_AMT6": BILL_AMT6,

            "PAY_AMT1": PAY_AMT1,
            "PAY_AMT2": PAY_AMT2,
            "PAY_AMT3": PAY_AMT3,
            "PAY_AMT4": PAY_AMT4,
            "PAY_AMT5": PAY_AMT5,
            "PAY_AMT6": PAY_AMT6,

            "TOTAL_PAY_AMT": TOTAL_PAY_AMT,
            "MAX_PAY_DELAY": MAX_PAY_DELAY,
            "TOTAL_BILL_AMT": TOTAL_BILL_AMT
        }


        # Convert dictionary to DataFrame
        input_data = pd.DataFrame([data])


        # -----------------------------
        # Exact Feature Order
        # -----------------------------

        feature_order = [
            "LIMIT_BAL",
            "SEX",
            "EDUCATION",
            "MARRIAGE",
            "AGE",
            "PAY_0",
            "PAY_2",
            "PAY_3",
            "PAY_4",
            "PAY_5",
            "PAY_6",
            "BILL_AMT1",
            "BILL_AMT2",
            "BILL_AMT3",
            "BILL_AMT4",
            "BILL_AMT5",
            "BILL_AMT6",
            "PAY_AMT1",
            "PAY_AMT2",
            "PAY_AMT3",
            "PAY_AMT4",
            "PAY_AMT5",
            "PAY_AMT6",
            "TOTAL_PAY_AMT",
            "MAX_PAY_DELAY",
            "TOTAL_BILL_AMT"
        ]

        input_data = input_data[feature_order]


        # -----------------------------
        # Make Prediction
        # -----------------------------

        prediction_result = model.predict(input_data)[0]


        # Convert prediction into readable result
        if prediction_result == 0:
            result = "Low Default Risk"
            message = "Prediction: No Default"
        else:
            result = "High Default Risk"
            message = "Prediction: Default"


        # Send result to result.html
        return render_template(
            "result.html",
            prediction=result,
            message=message
        )


    except Exception as e:

        return render_template(
            "result.html",
            prediction="Error",
            message=f"Something went wrong: {str(e)}"
        )


# -----------------------------
# About Model Page
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# Run Flask Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)