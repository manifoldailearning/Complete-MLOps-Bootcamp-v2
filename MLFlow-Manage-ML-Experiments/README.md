
## Virtual Environment
Create Virutal Environment with Conda

```python
conda create -n mlflow-venv python=3.10
```

```python
conda activate mlflow-venv
```

```python
pip install mlflow
```

# Notes on MLflow Tracking
`mlflow.set_tracking_uri()` connects to a tracking URI. You can also set the MLFLOW_TRACKING_URI environment variable to have MLflow find a URI from there. In both cases, the URI can either be a HTTP/HTTPS URI for a remote server, a database connection string, or a local path to log data to a directory. The URI defaults to mlruns.

`mlflow.get_tracking_uri()` returns the current tracking URI.

`mlflow.create_experiment()` creates a new experiment and returns its ID. Runs can be launched under the experiment by passing the experiment ID to mlflow.start_run.

`mlflow.set_experiment()` sets an experiment as active. If the experiment does not exist, creates a new experiment. If you do not specify an experiment in mlflow.start_run(), new runs are launched under this experiment.

`mlflow.start_run()` returns the currently active run (if one exists), or starts a new run and returns a mlflow.ActiveRun object usable as a context manager for the current run. You do not need to call start_run explicitly: calling one of the logging functions with no active run automatically starts a new one.

`mlflow.end_run()` ends the currently active run, if any, taking an optional run status.

`mlflow.log_param()` logs a single key-value param in the currently active run. The key and value are both strings. Use mlflow.log_params() to log multiple params at once.

`mlflow.log_metric()` logs a single key-value metric. The value must always be a number. MLflow remembers the history of values for each metric. Use mlflow.log_metrics() to log multiple metrics at once.

`mlflow.set_tag()` sets a single key-value tag in the currently active run. The key and value are both strings. Use mlflow.set_tags() to set multiple tags at once.

`mlflow.log_artifact()` logs a local file or directory as an artifact, optionally taking an artifact_path to place it in within the run’s artifact URI. Run artifacts can be organized into directories, so you can place the artifact in a directory this way.

`mlflow.log_artifacts()` logs all the files in a given directory as artifacts, again taking an optional artifact_path.





#### If you get Port Already in use error while using mlflow
- Get list of Services & PID running
`sudo lsof -i tcp:5000 `
- Kill them
`kill -15 <PID>`


# MLFlow Projects

- Create Run using MLFlow project file
`mlflow run . --experiment-name Loan_prediction`  # run from folder where `MLProject` file is present

- Run from git repository
`mlflow run https://github.com/manifoldailearning/ml-flow-project --experiment-name Loan_prediction` 

# MLFlow Models
- install virtualenv
`pip install virtualenv`

- install chardet
`pip install chardet`

- Serve the Models with Local REST server
`mlflow models serve -m runs:/<RUN_ID>/model --port 9000`

`mlflow models serve -m /Users/nachiketh/Desktop/author-repo/Complete-MLOps-BootCamp/MLFlow-Manage-ML-Experiments/mlruns/636758781795674813/91ef1ea3f63d40a7a33c4251dd088618/artifacts/RandomForestClassifier --port 9000`


# Generate Predictions
- http://127.0.0.1:9000/invocations

```json
{
    "dataframe_split": {
        "columns": [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ],
        "data": [
            [
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]
        ]
    }
}
```

# Curl

http://localhost:9000

```bash
curl --location 'http://127.0.0.1:9000/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "dataframe_split": {
        "columns": [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ],
        "data": [
            [
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]
        ]
    }
}'
```
```yaml
LogisticRegression/
    - conda.yaml
    - MLmodel
    - model.pkl
    - requriments.txt
```

- Installation
`pip install mysqlclient`

-port 5001
`mlflow server --host 0.0.0.0 --port 5001 --backend-store-uri mysql://root:admin123@localhost/db_mlflow --default-artifact-root $PWD/mlruns`

- port 5000
`mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri mysql://root:admin123@localhost/db_mlflow --default-artifact-root $PWD/mlruns`

`export MLFLOW_TRACKING_URI=http://0.0.0.0:5001`

`mlflow models serve -m "models:/Prediction_Model_RF/Production" -p 1234`

