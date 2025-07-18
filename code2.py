from fastapi import FastAPI, Path, HTTPException, Query
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
    return HTTPException(status_code=404, detail="Patient not found")



@app.get('/sort')
def sort_patient(sort_by:str=Query(..., description='Sort on the basis of height, weigt or bmi'), order:str=Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = 'Invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail = 'Invalid order select from asc or desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse= sort_order)

    return sorted_data


