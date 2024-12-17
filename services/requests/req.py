import requests
import time
import random

for i in range(50):
    params = {'citizen_id': i}
    data = {        
    "age":35,
    "workclass":"Private",
    "education.num":10,
    "marital.status":"Married-civ-spouse",
    "occupation":"Sales",
    "relationship":"Husband",
    "race":"White",
    "sex":"Male",
    "capital.gain":5000,
    "capital.loss":1000,
    "hours.per.week":60
    }
        
    response = requests.post('http://income-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())