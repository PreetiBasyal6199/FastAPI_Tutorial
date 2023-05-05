import os

import motor.motor_asyncio
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()
MONGO_CONN = os.getenv("MONGO_CONN")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONN)

database = client.students
student_collection = database.get_collection("students_collection")


# helper

def student_helper(student):
    return {
        "id": str(student["_id"]),
        "fullname": student["full_name"],
        "email": student["email"],
        "faculty": student["faculty"],
        "GPA": student["gpa"],

    }


# Create new student and add it into the database
async def create_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve all the students
async def retrieve_students() -> list:
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
