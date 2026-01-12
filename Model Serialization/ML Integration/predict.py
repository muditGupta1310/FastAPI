# Making predictions logic

import joblib
import numpy as np

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
            data['median_income'],
        ]
    ])
    return model.predict(features)[0]
    