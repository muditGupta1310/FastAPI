from fastapi import FastAPI, Path
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

@app.get('/view/{patient_id}')
def view_patient(patient_id: str = Path(...,description="ID of the patient in DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found"}, 404