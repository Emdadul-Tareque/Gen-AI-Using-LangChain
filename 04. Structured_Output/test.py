from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name:str 
    age: str
  

new_user = {"name": 'tareque',"age" : '30'}
user = User(**new_user)
user_dict = dict(user)
print(user_dict)
print(user_dict['age'])

user_json = user.model_dump_json()  
print(user_json)