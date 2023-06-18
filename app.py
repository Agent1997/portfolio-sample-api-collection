from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from logging import getLogger

app = FastAPI()
logger = getLogger(__name__)

@app.get("/students")
def get_students():
    data = [
        {
            "name": "One Uno",
            "school": "University of FastAPI",
            "subjects": [
                {
                    "name": "math",
                    "teacher": "Prof. Ichi",
                    "schedule": "1-2PM",
                    "room": "103"
                },
                {
                    "name": "english",
                    "teacher": "Prof. Karin",
                    "schedule": "4-5PM",
                    "room": "109"
                }
            ]
        },
        {
            "name": "Dos Two",
            "school": "University of FastAPI",
            "subjects": [
                {
                    "name": "math",
                    "teacher": "Prof. Ichi",
                    "schedule": "1-2PM",
                    "room": "103"
                },
                {
                    "name": "english",
                    "teacher": "Prof. Karin",
                    "schedule": "4-5PM",
                    "room": "109"
                }
            ]
        }
    ]
    
    return data

class Grades(BaseModel):
    subject: str
    grade: int
    
class Student(BaseModel):
    name: str
    grades: list[Grades]

@app.post("/grade")
def post_grades(student: Student):
    logger.info(student)
    return JSONResponse(content={"message": "Grade successfully posted","data":student.dict()}, status_code=201)