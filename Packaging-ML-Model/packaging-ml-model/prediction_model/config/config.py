import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

FILE_NAME = 'loan_approval_dataset.csv'
TEST_FILE = "test_data.csv"

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')



TARGET = 'loan_status'

#Final features used in the model
FEATURES = ['no_of_dependents', 'education', 'self_employed', 'income_annum',
       'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
       'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value','loan_status']

PRED_FEATURES = ['no_of_dependents', 'education', 'self_employed', 'income_annum',
       'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
       'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['education', 'self_employed']

# Dict for transformation
FEATURES_TO_ENCODE = {
  'education': ['Graduate'],
  'self_employed': ['Yes']
}

NEW_FEATURE_ADD = 'total_assets_value'
FEATURE_TO_ADD = ['residential_assets_value','commercial_assets_value', 'luxury_assets_value','bank_asset_value' ]

DROP_FEATURES = ['residential_assets_value','commercial_assets_value', 'luxury_assets_value','bank_asset_value' ]

LOG_FEATURES = ['income_annum','loan_amount','total_assets_value'] # taking log of numerical columns


