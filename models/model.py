from sqlalchemy import Column, Table,Integer, String, ForeignKey, DateTime, Float, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from utils.database import Base


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    telephone = Column(String)
    isActive = Column(Boolean(), default=True)
    dateAdded = Column(DateTime, default=datetime.now)
    mother = relationship("ExpectedMother", back_populates="admins")
    appointment = relationship("Appointment", back_populates="admin")

class ExpectedMother(Base):
    __tablename__ = 'ExpectedMothers'
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    telephone = Column(String)
    dateAdded = Column(DateTime, default=datetime.now)
    added_by =  Column(Integer, ForeignKey('admins.id'))

    admins = relationship("Admin", back_populates="mother")
    mother = relationship("Comment", back_populates="expected_mother")
    appointment = relationship("Appointment", back_populates="expected_mother")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key =True, index = True)
    message = Column(String)
    expected_mother_id =  Column(Integer, ForeignKey('ExpectedMothers.id'))
    dateAdded = Column(DateTime, default=datetime.now) 
    expected_mother = relationship("ExpectedMother", back_populates="mother") 

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key =True, index = True)
    expected_mother_id =  Column(Integer, ForeignKey('ExpectedMothers.id'))
    appointed_date = Column(String)
    attended = Column(Boolean(), default=False)
    appointed_set_by =  Column(Integer, ForeignKey('admins.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    admin = relationship("Admin", back_populates="appointment")
    expected_mother = relationship("ExpectedMother", back_populates="appointment") 
  