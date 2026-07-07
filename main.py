from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students=[]
class student(BaseModel):
    id : int
    name : str
    email : str

# Add Student
@app.post('/create')
def add_student(student:student):
    students.append(student)
    return {
        "message":"create successfully"
    }

@app.get('/view')
def view_students():
    return students

# View One Student
@app.get('/views/{id}')
def view_one(id: int):
    for i in students:
        if i.id == id:
            return i
    return "Student Not Found"

#Update Student
@app.put('/update/{id}')
def update_student(id: int, updated_student: student):
    for student in students:
        if student.id == id:
            student.id = updated_student.id
            student.name = updated_student.name
            student.email = updated_student.email
            return "Student Updated Successfully"
    return  "Student Not Found"

# Delete Student
@app.delete('/delete/{id}')
def delete_student(id: int):
    for student in students:
        if student.id == id:
            students.remove(student)
            return "Student Deleted Successfully"

    return "Student Not Found"