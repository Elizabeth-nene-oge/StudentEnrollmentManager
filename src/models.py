from sqlalchemy import Column, String, DateTime, Float, Integer, JSON, Date, UUID, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
# import uuid
# from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()


class Registries(Base):
    __tablename__ = 'registry'
    
    registry_id = Column(UUID, primary_key=True, index=True)
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

    class_id = Column(UUID, primary_key=True, index=True)
    level = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    status = Column(String, nullable=False)


class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())


class Students(Base):
    __tablename__ = 'students'

    student_id = Column(UUID, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lasttName = Column(String, nullable=False)
    otherNames = Column(String, nullable=False)
    dateOfBirth = Column(Date, nullable=False)
    lastUpdated = Column(DateTime(timezone=True), 
                         nullable=False, server_default=func.now(), onupdate=func.now())


class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_courses_id = Column(UUID, primary_key=True)
    studentId = Column(UUID, ForeignKey('students.student_id'), nullable=False)
    courseId = Column(UUID, ForeignKey('courses.course_id'), nullable=False)
    status = Column(String, nullable=False)
    dateCreated = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())