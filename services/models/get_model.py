import mlflow
import pickle as pkl

# Работаем с MLflow локально
TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)   
mlflow.set_registry_uri(registry_uri)   

#RUN_NAME = 'aa4b283d67e944a7a65b38eb20eb647c'
RUN_NAME = '6ef44e804cba45f4a8b51ba54fcb873c'
loaded_model = mlflow.sklearn.load_model(f'runs:/{RUN_NAME}/models')

with open('model.pkl', 'wb+') as f:
   pkl.dump(loaded_model, f)