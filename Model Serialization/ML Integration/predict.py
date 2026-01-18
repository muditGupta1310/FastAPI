# Making predictions logic

import joblib
import numpy as np
from typing import List

model = joblib.load('model.joblib')
print('Loaded the model')

def make_predications(data:dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']
        ]
    ])
    return model.predict(features)[0]
    

def make_batch_predictions(data:List[dict]) -> np.array:
    X = np.array([
        [
            x['longitude'],
            x['latitude'],
            x['housing_median_age'],
            x['total_rooms'],
            x['total_bedrooms'],
            x['population'],
            x['households'],
            x['median_income']
        ]
        for x in data
    ])
    print(X)
    return model.predict(X)