# Path parameters for specific user...using filters...

# from fastapi import FastAPI

# user_db = {
#                 'David': {'uname':'David', 'DOJ': '01/01/2022', 'Loc': 'LA','age': 54, 'Role': 'Project Manager'},
#                 'John': {'uname':'John', 'DOJ': '01/01/2023', 'Loc': 'IL','age': 34, 'Role': 'Team Lead'},
#                  'Peter': {'uname':'Peter', 'DOJ': '01/01/2024', 'Loc': 'Toronto','age': 24,'Role': 'Developer'}}

# app = FastAPI()

# @app.get('/users')
# def get_users():
#     user_list = list(user_db.values())
#     return user_list

# from fastapi import FastAPI

# user_db = {
#                 'david': {'uname':'david', 'doj': '01/01/2022', 'loc': 'LA'},
#                 'john': {'uname':'john', 'doj': '01/01/2023', 'loc': 'IL'},
#                  'peter': {'uname':'peter', 'doj': '01/01/2024', 'loc': 'Toronto'}}
# from fastapi import FastAPI
# app = FastAPI()

# @app.get('/users/{username}')

# def get_user_path(username: str):
#         return user_db[username]

#####################################

# @app.get('/users')

# def get_users_query(limit: int = 2): # here query parameters we can make optional, but not for path parameters as below
#     user_list = list(user_db.values())
#     return user_list[:limit]

# @app.get('/users/{username}')

# def get_user_path(username: str = 'Peter'): # here path parameters we cannot make optional, always required...
#         return user_db[username]

####################################
# Add users....
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

user_db = {
                'David': {'username':'David', 'doj': '01/01/2022', 'Location': 'LA','age': 54, 'Role': 'Project Manager'},
                'John': {'username':'John', 'doj': '01/01/2023', 'Location': 'IL','age': 34, 'Role': 'Team Lead'},
                 'Peter': {'username':'Peter', 'doj': '01/01/2024', 'Location': 'Toronto','age': 24,'Role': 'Developer'}}

app = FastAPI()

class User(BaseModel):
      username: str = Field(min_length=3, max_length=20)
      doj: date
      location: Optional[str] = None
      age: int = Field(None, gt=5, lt=70)
      Role: str

class UserUpdate(User):
      doj: Optional[date] = None # this field is optional weather u want to update previous date or remain old date ?
      age: int = Field(None, gt=15, lt=100) # this field is applicable for patch update...
#app = FastAPI()  


# @app.get('/users')
# def get_users():
#     user_list = list(user_db.values())
#     return user_list

@app.get('/users')
def get_users_query(limit: int = 20): # here query parameters we can make optional, but not for path parameters as below
    user_list = list(user_db.values())
    return user_list[:limit]

#
@app.get('/users/{username}')

def get_user_path(username: str = 'Peter'): # here path parameters we cannot make optional, always required...
        return user_db[username]

@app.post('/users')
def create_user(user: User):  
     username = user.username
     user_db[username] = user.model_dump() 
#we can add user_db dictionary username equals, the dict() method converts data of 'user'
# into dictionary, this is required bcoz user model of class 'User' converted to dictionary   
# so, we are adding to 'user_db' a key of 'username' and value as 'dict()' user.  
     return {'message': f'Successfully created user: {username }'}

@app.delete('/users/{username}')
def delete_user(username: str):
      del user_db[username]

      return {'message': f'Successfully deleted user: {username }'}
###################
# update as new record by put operation...
@app.put('/users')
def update_user(user: User):  
     username = user.username
     user_db[username] = user.model_dump() 

     return {'message': f'Successfully updated user: {username }'}

#######################
# Partial update....by patch operation
# the difference between put and patch method ,
#  that put will update complete record, where as patch
# method will partially updates....

@app.patch('/users')
def update_user_partial(user: UserUpdate):  
     username = user.username
     user_db[username].update(user.model_dump(exclude_unset=True))

     return {'message': f'Successfully updated user: {username }'}