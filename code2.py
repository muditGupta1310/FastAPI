from fastapi import FastAPI
import json

app = FastAPI()
# to make this project patient.json file was created 

def load_data():
    with open('patient.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get('/about')
def about():
    return {'message':'A fully functional API t manage your patient records.'}


@app.get('/view')
def view():
    data = load_data()
    return data