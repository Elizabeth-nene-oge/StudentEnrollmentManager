from pydantic import BaseModel
from enum import Enum
from datetime import datetime, date
from uuid import UUID
from typing import Optional


class RegistryStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    REGISTERED = "REGISTERED"
    GRADUATED = "GRADUATED"
    UNREGISTERED = "UNREGISTERED"
   
class StudentCourseStatus(str, Enum):
    REGISTERED = "REGISTERED"
    COMPLETED = "COMPLETED"
    DROPPED = "DROPPED"
    
class CourseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Registry(BaseModel):
    registry_id: UUID
    student_id: UUID
    class_id: UUID
    status: RegistryStatus
    date_created: datetime
    last_updated: datetime
        

class Class(BaseModel):
    class_id: UUID
    level: str
    name: str
    date_created: datetime
    last_updated: datetime
    # status:

class Course(BaseModel):
    course_id: UUID
    name: CourseStatus
    date_created: datetime
    last_updated: datetime

class Student(BaseModel):
    student_id: UUID
    first_name: str
    last_name: str
    other_names: Optional[str] = None
    date_of_birth: date
    date_created: datetime
    last_updated: datetime

class StudentCourse(BaseModel):
    student_courses_id: UUID
    student_id: UUID
    course_id: UUID
    status: StudentCourseStatus
    date_created: datetime
    last_updated: datetime



