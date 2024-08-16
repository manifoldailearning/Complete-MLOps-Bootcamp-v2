# Importing Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np
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

app = FastAPI()



#Perform parsing
class LoanPred(BaseModel):
    Dependents: int 
    Education: str 
    Self_Employed: str 
    TotalIncome: int  # 'income_annum'
    LoanAmount: int 
    Loan_Amount_Term: int  # 'loan_term'
    Credit_History: int  # 'cibil_score'
    Residential_Assets_Value: int 
    Commercial_Assets_Value: int
    Luxury_Assets_Value: int 
    Bank_Asset_Value: int 


@app.get('/')
def index():
    return {'message': 'Welcome to Loan Prediction App'}

# defining the function which will make the prediction using the data which the user inputs 
@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
	data = loan_details.model_dump()
	new_data = {
    'no_of_dependents': data['Dependents'],
    'education': data['Education'],
    'self_employed': data['Self_Employed'],
    'income_annum': data['TotalIncome'],
    'loan_amount': data['LoanAmount'],
    'loan_term': data['Loan_Amount_Term'],
    'cibil_score': data['Credit_History'],
    'residential_assets_value': data['Residential_Assets_Value'],
    'commercial_assets_value': data['Commercial_Assets_Value'],
    'luxury_assets_value': data['Luxury_Assets_Value'],
    'bank_asset_value': data['Bank_Asset_Value']
	}

# Create a DataFrame with a single row from the new_data dictionary
	df = pd.DataFrame([new_data])

	# Making predictions 
	prediction = classification_pipeline.predict(df)

	if prediction[0] == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'

	return {'Status of Loan Application':pred}

if __name__ == '__main__':
	uvicorn.run("main:app", host="0.0.0.0",port=8005,reload=False)
