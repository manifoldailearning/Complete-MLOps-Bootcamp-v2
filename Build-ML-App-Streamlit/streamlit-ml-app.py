import joblib
import streamlit as st
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


def prediction(Dependents,Education,SelfEmployed,AnnualIncome,LoanAmount,
         LoanAmountTerm,CibilScore,ResidentialAssetsValue,CommercialAssetsValue,LuxuryAssetsValue,BankAssetsValue):
        data = {'no_of_dependents': Dependents, 
        'education': Education, 
        'self_employed': SelfEmployed, 
        'income_annum': AnnualIncome, 
        'loan_amount': LoanAmount, 
        'loan_term': LoanAmountTerm, 
        'cibil_score': CibilScore, 
        'residential_assets_value':ResidentialAssetsValue , 
        'luxury_assets_value': LuxuryAssetsValue, 
        'bank_asset_value': BankAssetsValue,
        'commercial_assets_value':CommercialAssetsValue }

        df = pd.DataFrame(data, index=[0])
        prediction = classification_pipeline.predict(df)
        print(print(prediction))

        if prediction[0]==0:
            pred = "Rejected"

        else:
            pred = "Approved"
        return pred        


def main():
    # Front end
    st.title("Welcome to Loan Application")
    st.header("Please enter your details to proceed with your loan Application")
    Dependents = st.number_input("Number of Dependents")
    Education = st.selectbox("Education",("Graduate","Not Graduate"))
    SelfEmployed = st.selectbox("Self Employed",("Yes","No"))
    AnnualIncome = st.number_input("Applicant Income")
    LoanAmount = st.number_input("LoanAmount")
    LoanAmountTerm = st.number_input("Loan Amount Term (in years)")
    CibilScore = st.number_input("Cibil Score")
    ResidentialAssetsValue = st.number_input("Residential Assets Value")
    CommercialAssetsValue = st.number_input("Commercial Assets Value")
    LuxuryAssetsValue = st.number_input("Luxury Assets Value")
    BankAssetsValue = st.number_input("Bank Assets Value")

    if st.button("Predict"):
        result = prediction(Dependents,Education,SelfEmployed,AnnualIncome,LoanAmount,
         LoanAmountTerm,CibilScore,ResidentialAssetsValue,CommercialAssetsValue,LuxuryAssetsValue,BankAssetsValue)
        
        if result == "Approved":
            st.success("Your loan Application is Approved")
        else:
            st.error("Your loan Application is Rejected")

if __name__ == "__main__":
    main()
