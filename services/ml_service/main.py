
import random
from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(citizen_id: int, item_features: dict):
    prediction = app.handler.predict(citizen_id, item_features)
    return ({
             'income': str(prediction),
             'citizen_id': citizen_id
            })
