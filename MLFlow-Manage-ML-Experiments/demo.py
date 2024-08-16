import os
import mlflow
import argparse
import time


def eval(p1, p2):
    output_metric = p1**2 + p2**2
    return output_metric

def main(inp1, inp2):
    mlflow.set_experiment("Demo_Experiment")
    #with mlflow.start_run(run_name='Example Demo'):
    with mlflow.start_run():
        mlflow.set_tag("version","1.0.0")
        mlflow.log_param("param1",inp1)
        mlflow.log_param("param2",inp2) # key, value
        metric = eval(p1 = inp1, p2 = inp2)
        mlflow.log_metric("Eval_Metric",metric)
        os.makedirs("dummy", exist_ok=True)
        with open("dummy/example.txt", "wt") as f:
            f.write(f"Artifact created at {time.asctime()}")
        mlflow.log_artifacts("dummy")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--param1","-p1", type=int, default=5)
    args.add_argument("--param2","-p2", type=int, default=10)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.param1, parsed_args.param2)