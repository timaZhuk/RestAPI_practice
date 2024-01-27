from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#create instance of FastAPI

app = FastAPI()

#end point
# for url ='localhost/delete-user' endpoint is=delete-user
#GET - get information and return information
#POST - CREATE ITEM, OBJECT
#PUT - CHANGE, UPDATE ITEM, OBJECT
#DELETE - Delete something
#----------------------------------------------------------
students={
    1:{
        "name":"Timmy",
        "age":17,
        "year":"year 12"
    },
    2:{
        "name":"Anny",
        "age":18,
        "year":"year 13"
    }
}
class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[age]=None
    year:Optional[year]=None

#---------------------------------------------------------------
#---Query pass parameters into url-----google.com/results?search=Python
#----------------------------------------------------
#--------creating page or endpoint------------
@app.get('/')  
def index():
    # use json (but we can use dictionary)
    return {"name":"First API url"}

#path parameters and data inside function
@app.get('/get-student/{student_id}')
def get_student(student_id:int=Path(description="input the Id of the student")):
    return students[student_id]
#-query
@app.get('/get-by-name/{student_id}')
def get_student(*,student_id ,name:Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}

#-------------------POST------------------------------------
#request and body parameter together
@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error": "Student exist"}
    students[student_id]=student
    return students[student_id]

# ------------------PUT------------------------
@app.put('/update-student/{student_id}')
def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {"Error ":"No such student with this id"}
    #----------------------------------------------------
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    #------------------------------------------------
    students[student_id] = student
    return students[student_id]
#------------DELETE------------------------------------------
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"This student is not in DataBase"}
    del students[student_id]
    return {"Message":"Student was deleted!!"}
 
    



