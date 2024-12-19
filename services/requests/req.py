import requests
import time
import random

for i in range(50):
    params = {'citizen_id': i}
    data = {        
    "age":random.randint(20,50),
    "workclass":"Private",
    "education.num":random.randint(1,16),
    "marital.status":"Married-civ-spouse",
    "occupation":"Sales",
    "relationship":"Husband",
    "race":"White",
    "sex":"Male",
    "capital.gain":random.randint(2000,20000),
    "capital.loss":random.randint(1000,4000),
    "hours.per.week":40
    }
        
    response = requests.post('http://income-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())