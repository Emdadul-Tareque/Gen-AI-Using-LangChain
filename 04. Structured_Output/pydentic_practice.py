from pydantic import BaseModel, EmailStr, Field
from typing import Optional

"""Pydantic feature: Default Values, Optional Fields, Type Conversion, 
Buildin Validation, Field Function -> Default Values, Constraints, Descriptions, Regex"""

class Student(BaseModel):
    name: str # = 'Tareque', # Default value
    age: int
    email: Optional[EmailStr] = 'none'
    cgpa: float = Field(gt=0, lt=5.0, description="CGPA must be between 0 and 5") # Constraints and Description


new_student = {'name': 'tareque', 'age': '30','cgpa': 4} # Here age is string, but will be converted to int

new_student = Student(**new_student)
print(new_student)
#print(type(new_student.age))   # <class 'int'> automatic type conversion
#print(type(new_student['age'])) # <class 'str'> Optional field with default value

new_student_dict= dict(new_student)

