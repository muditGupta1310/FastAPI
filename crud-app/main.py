import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency with the DB 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


# endpoints
# 1. create an employee
@app.post('/create_employees',response_model = schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db : Session = Depends(get_db)):
    return crud.createEmployee(db,employee)

@app.get('/get_all_employees',response_model=List[schemas.EmployeeOut])
def get_all_employees(db : Session = Depends(get_db)):
    return crud.getEmployees(db)

@app.get('/get_employee/{emp_id}',response_model=schemas.EmployeeOut)
def get_employee(emp_id:int, db : Session = Depends(get_db)):
    employee = crud.getEmployee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee

    
@app.put('/update_employees/{emp_id}',response_model=schemas.EmployeeOut)
def update_employee(emp_id:int, employee: schemas.EmployeeUpdate, db:Session = Depends(get_db)):
    db_employee = crud.updateEmployee(db, emp_id,employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee

@app.delete('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def delete_employee(db:Session=Depends(get_db),emp_id = int):
    employee = crud.deleteEmployee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee
    

