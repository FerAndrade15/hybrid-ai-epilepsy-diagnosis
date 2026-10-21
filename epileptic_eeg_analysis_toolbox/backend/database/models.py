"""
# File: models.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos
#
# Object-Relational Mapping module, to create SQL database and keep it related to python for connections.
# 
# Additional information to clarify the use of SQL Alchemy library:
#   Each class represents a database table
#   Each atriute represents a column
#   Each instance representes a row/register
"""
# Imports to work with SQL sentences as variables
from sqlalchemy import (
    Column, Integer, String, Float, Date, ForeignKey, Boolean, Text, Time
)
from sqlalchemy.orm import declarative_base, relationship

# Foundational class
base = declarative_base()

# Users Table
class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(128))
    role = Column(String(20))
    email = Column(String(60))
    type = Column(String(15))
    
    # System permissions
    admin_users = Column(Boolean(), default=False)
    test_analysis = Column(Boolean(), default=False)
    patients_input = Column(Boolean(), default=False)
    patients_consult = Column(Boolean(), default=False)
    confidential_consult = Column(Boolean(), default=False)
    automatic_annotations = Column(Boolean(), default=False)
    create_algorithm = Column(Boolean(), default=False)
    create_algorithm_2 = Column(Boolean(), default=False)
    first_login = Column(Boolean(), default=True)
    recover_password = Column(Boolean(), default=False)

# Patients Table
class Patient(base):
    __tablename__ = 'patients'
    code = Column(String(20), primary_key=True)
    name = Column(String(100))
    sex = Column(String(1), nullable=False)
    birth_date = Column(Date(), nullable=False)
    personal_bckg = Column(Text())
    diagnosis = Column(Text())
    condition = Column(String(100), nullable=False)
    confidential_notes = Column(String(50))

    # Relation
    studies = relationship("EEGStudy", back_populates="patient", cascade="all, delete-orphan")

# EEG Study Table
class EEGStudy(base):
    __tablename__ = 'eeg_studies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), ForeignKey('patients.code'))

    # Temporal metadata
    test_date = Column(Date(), nullable=False)
    start_time = Column(Time(), nullable=False)
    duration_s = Column(Float())
    sampling_freq_hz = Column(Float())
    no_channels = Column(Integer())

    edf_file_path = Column(String(500), nullable=False)

    # Relation
    patient = relationship("Patient", back_populates="studies")