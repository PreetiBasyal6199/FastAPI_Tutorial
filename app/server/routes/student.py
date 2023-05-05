from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import create_student, retrieve_students, retrieve_student
from server.models.student import (
    SuccessResponseModel,
    StudentModel
)

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_new_student(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await create_student(student)
    return SuccessResponseModel(new_student, "Student added successfully.")


@router.get("/", response_description="Students are retrieved successfully from the database")
async def get_students():
    students = await retrieve_students()
    return SuccessResponseModel(students, "Student List retrieved successfully.")


@router.get("/{id}", response_description="Student detail retrieved from the database.")
async def get_student(id):
    student = await retrieve_student(id)
    return SuccessResponseModel(student, "Student detail retrieved successfully.")
