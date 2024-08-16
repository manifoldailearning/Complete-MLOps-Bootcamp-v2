# Importing Dependencies
from flask import Flask,render_template,request
import joblib
import pandas as pd
import sys
import os
from pathlib import Path
# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# # Then perform import
from prediction_model.config import config 
from prediction_model.processing.data_handling import load_pipeline

classification_pipeline = load_pipeline(config.MODEL_NAME)

app = Flask(__name__)

def transform_to_integers(data):
    # List of columns to convert to integers
    columns_to_convert = [
        'no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 
        'cibil_score', 'residential_assets_value', 'commercial_assets_value', 
        'luxury_assets_value', 'bank_asset_value' 
    ]

    for col in columns_to_convert:
        try:
            # Attempt to convert the value to an integer
            data[col] = int(data[col])
        except ValueError:
            # Handle the case where conversion fails (e.g., non-numeric value)
            print(f"Warning: Could not convert '{col}' to integer. Value: {data[col]}")

    return data


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        request_data = dict(request.form)
        print(request_data)
        request_data = {k:v for k,v in request_data.items()}
        #format numeric columns
        request_data = transform_to_integers(request_data)
        print(request_data)
        data = pd.DataFrame([request_data])
        print(data)
        pred = classification_pipeline.predict(data)
        print(f"prediction is {pred}")


        if int(pred[0]) == 1:
            result = "Congratulations! your loan request is approved"
        if int(pred[0]) == 0:
            result = "Sorry! your loan request is rejected"
        return render_template('homepage.html',prediction = result)

@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
