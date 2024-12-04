from sqlalchemy import Column, String, DateTime, Date, UUID, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()


class Registry(Base):
    __tablename__ = 'registry'
    
    registry_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    studentId = Column(UUID, ForeignKey('students.student_id'), nullable=False)
    classId = Column(UUID, ForeignKey('classes.class_id'), nullable=False)
    status = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())
    
    student = relationship("Students", back_populates="registry")
    class_ = relationship("Classes", back_populates="registry")


class Classes(Base):
    __tablename__ = 'classes'

    class_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    level = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())
    status = Column(String, nullable=False)
    registry = relationship("Registry", back_populates="class_")


class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())
    student_courses = relationship("StudentCourses", back_populates="course")


class Students(Base):
    __tablename__ = 'students'

    student_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    otherNames = Column(String, nullable=True)
    dateOfBirth = Column(Date, nullable=False)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())

    registry = relationship("Registry", back_populates="student")
    student_courses = relationship("StudentCourses", back_populates="student")


class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_courses_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    studentId = Column(UUID(as_uuid=True), ForeignKey('students.student_id'), nullable=False)
    courseId = Column(UUID(as_uuid=True), ForeignKey('courses.course_id'), nullable=False)
    status = Column(String, nullable=False)
    dateCreated = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now(), onupdate=func.now())
    

    student = relationship("Students", back_populates="student_courses")
    course = relationship("Courses", back_populates="student_courses")