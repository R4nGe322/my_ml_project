import mlflow
import wandb

mlflow.start_run()
mlflow.log_param("n_estimators", 100)
mlflow.log_metric("accuracy", accuracy)
mlflow.sklearn.log_model(model, "model")
mlflow.end_run()

wandb.login(key="c55fa3e94ecb4b464a8982c7adc34aa1612a2ad7")
wandb.init(project="my_ml_project")
wandb.config.n_estimators = 100
wandb.log({"accuracy": accuracy})
