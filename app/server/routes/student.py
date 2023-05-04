from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import create_student
from server.models.student import (
    SuccessResponseModel,
    ErrorResponseModel,
    StudentModel,
    UpdateStudentModel
)

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_new_student(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await create_student(student)
    return SuccessResponseModel(new_student, "Student added successfully.")
