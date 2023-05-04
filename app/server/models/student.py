
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentModel(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    faculty: str = Field(...)
    gpa: int = Field(..., le=4)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Ram",
                "email": "ram@ram.com",
                "faculty": "Some",
                "gpa": 3
            }
        }


class UpdateStudentModel(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    faculty: Optional[str]
    gpa: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Ram",
                "email": "ram@ram.com",
                "faculty": "Some",
                "gpa": 3
            }
        }


def SuccessResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }

