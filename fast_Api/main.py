from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary Database
students = []

# -------------------------
# Pydantic Model
# -------------------------

class Student(BaseModel):
    name: str
    age: int

# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():
    return {"message": "FastAPI CRUD Working"}

# -------------------------
# CREATE
# -------------------------

@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student Added",
        "data": student
    }

# -------------------------
# READ ALL
# -------------------------

@app.get("/students")
def get_students():

    return students

# -------------------------
# READ ONE
# -------------------------

@app.get("/students/{index}")
def get_student(index: int):

    return students[index]

# -------------------------
# UPDATE
# -------------------------

@app.put("/students/{index}")
def update_student(index: int, student: Student):

    students[index] = student

    return {
        "message": "Student Updated",
        "data": student
    }

# -------------------------
# DELETE
# -------------------------

@app.delete("/students/{index}")
def delete_student(index: int):

    deleted_student = students.pop(index)

    return {
        "message": "Student Deleted",
        "data": deleted_student
    }