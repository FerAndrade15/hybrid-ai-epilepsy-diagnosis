"""
# File: repositories.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos
#
# Functions to interact with the SQL database 
# within graphic windows and pipelines.
"""
# Manager and SQL libraries
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from backend.database.db_manager import get_connection
from backend.database.models import Patient, EEGStudy, User

# Sessions generation
SessionLocal = sessionmaker(bind=get_connection(), autoflush=False, autocommit=False, expire_on_commit=False)

# Context manager
@contextmanager
def get_df_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

class PatientRepository:
    @staticmethod
    def get_by_code(patient_code):
        """Search patient by primary id code"""
        with get_df_session() as session:
            return session.query(Patient).filter(Patient.code == patient_code).first()

    @staticmethod
    def create(patient_data: dict) -> Patient:
        """Inserts new patient into the database"""
        with get_df_session() as session:
            new_patient = Patient(**patient_data)
            session.add(new_patient)
            session.flush()
            session.refresh(new_patient)
            return new_patient

    @staticmethod
    def list_all() -> list:
        """Recover the lsit of all discharged patients"""
        with get_df_session() as session:
            return session.query(Patient).all()

class StudyRepository:
    @staticmethod
    def create(study_data: dict) -> EEGStudy:
        """Saving a new  EEG study associated to a patient"""
        with get_df_session() as session:
            new_study = EEGStudy(**study_data)
            session.add(new_study)
            session.flush()
            session.refresh(new_study)
            return new_study
    
    @staticmethod
    def get_by_patient(patient_code: str) -> list:
        """Getting registered studies list for a certain patient code"""
        with get_df_session() as session:
            return session.query(EEGStudy).filter(EEGStudy.code == patient_code).all()

# Module test
if __name__ == "__main__":
    pacientes = PatientRepository.list_all()
    print(f"Prueba de repositorio exitosa.\nTotal de pacientes en BD {len(pacientes)}")