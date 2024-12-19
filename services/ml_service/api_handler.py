import logging
import pandas as pd
import pickle as pkl
from datetime import datetime



logger = logging.getLogger("uvicorn.error")
class FastAPIHandler():

    def __init__(self):
        logger.warning('Loading model...')
        try:
            with open('../models/model.pkl', 'rb') as model_file:
                self.model = pkl.load(model_file)
            logger.info('Model is loaded')
        except pkl.UnpicklingError:
            logger.error('Error unpickling the model. The file may be corrupted or incompatible.')
        except FileNotFoundError:
            logger.error('Model file not found. Please check the path: ../services/models/model.pkl')
        except Exception as e:
            logger.error('Error loading model')

    def predict(self, citizen_id, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        prediction = self.model.predict(item_df)

        return (prediction[0])