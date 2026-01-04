from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id:int = Field(..., gt=0)
    name:str = Field(..., min_length=3, max_length=50, regex=r'^[A-Za-z]+(\.[A-Za-z]+)*$')
    department:str = Field(..., min_length=2, max_length=50, regex=r'^[A-Za-z]+([ .-][A-Za-z]+)*$')
    age: Optional[int] = Field(default=None, ge=18, le=100)




