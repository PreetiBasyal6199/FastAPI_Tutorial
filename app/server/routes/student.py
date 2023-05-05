from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    create_student, retrieve_students, retrieve_student, delete_student, update_student)
from server.models.student import (
    SuccessResponseModel,
    StudentModel,
    ErrorResponseModel,
    UpdateStudentModel
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
    if student:
        return SuccessResponseModel(student, "Student detail retrieved successfully.")
    return ErrorResponseModel("An error occurred", 404, f"Student with id {id} doesn't exist")


@router.delete("/{id}")
async def remove_student(id):
    deleted_student = await delete_student(id)
    if deleted_student:
        return SuccessResponseModel(f"Student with ID {id} removed.", "Student deleted successfully.")
    return ErrorResponseModel("An error occurred", 404, f"Student with id {id} doesn't exist")


@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return SuccessResponseModel(f"Student with ID {id} updated.", "Student updated successfully.")
    return ErrorResponseModel("An error occurred", 404, "There was an error updating this student")
