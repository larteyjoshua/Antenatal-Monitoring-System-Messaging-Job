from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.utils.database import Base


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(655))
    email = Column(String(655))
    password = Column(Text)
    telephone = Column(String(655))
    isActive = Column(Boolean(), default=True)
    dateAdded = Column(DateTime, default=datetime.now)
    mother = relationship("ExpectedMother", back_populates="admins")
    appointment = relationship("Appointment", back_populates="admin")
    which_user = relationship('UserRole', back_populates="which_role")


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(655))
    description = Column(String(655))
    date_created = Column(DateTime, default=datetime.now)
    roles = relationship('UserRole',  back_populates="user_role")


class UserRole(Base):
    __tablename__ = 'user_roles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('admins.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    date_modified = Column(
        DateTime, default=datetime.now,  onupdate=datetime.now)

    which_role = relationship('Admin', back_populates="which_user")
    user_role = relationship('Role',  back_populates="roles")


class ExpectedMother(Base):
    __tablename__ = 'ExpectedMothers'
    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(655))
    first_name = Column(String(655))
    telephone = Column(String(655))
    dateAdded = Column(DateTime, default=datetime.now)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    birth_date = Column(String(655), nullable=True)
    location = Column(String(655), nullable=True)
    first_antenatal_visit_date = Column(String(655), nullable=True)
    expected_delivery_date = Column(String(655), nullable=True)
    login_pin = Column(Text)

    added_by = Column(Integer, ForeignKey('admins.id'))

    admins = relationship("Admin", back_populates="mother")
    mother = relationship("Comment", back_populates="expected_mother")
    appointment = relationship("Appointment", back_populates="expected_mother")
    voice = relationship("Voice", back_populates="expected_mother")
    activity = relationship(
        "Activity", back_populates="expected_mother_activity")


class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)
    expected_mother_id = Column(Integer, ForeignKey('ExpectedMothers.id'))
    appointed_date = Column(String(655))
    appointed_time = Column(String(655))
    attended = Column(Boolean(), default=False)
    appointed_set_by = Column(Integer, ForeignKey('admins.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    appointment_note = Column(Text)

    admin = relationship("Admin", back_populates="appointment")
    expected_mother = relationship(
        "ExpectedMother", back_populates="appointment")
    comment = relationship("Comment", back_populates="appointment")
    recording = relationship("Voice", back_populates="appointment")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    expected_mother_id = Column(Integer, ForeignKey('ExpectedMothers.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))

    appointment = relationship("Appointment", back_populates="comment")
    expected_mother = relationship("ExpectedMother", back_populates="mother")


class Voice(Base):
    __tablename__ = 'voices'
    id = Column(Integer, primary_key=True, index=True)
    recording_name = Column(Text)
    expected_mother_id = Column(Integer, ForeignKey('ExpectedMothers.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))

    appointment = relationship("Appointment", back_populates="recording")
    expected_mother = relationship("ExpectedMother", back_populates="voice")


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    expected_mother_id = Column(Integer, ForeignKey('ExpectedMothers.id'))
    activity_type = Column(String, index=True)
    activity_date = Column(DateTime, default=datetime.now)
    status = Column(String, index=True)
    expected_mother_activity = relationship(
        "ExpectedMother", back_populates="activity")
