# app/services/education_service.py
from app.models.education_model import Education

def create_education(user_id, degree, institution, start_date, end_date):
    return Education(user_id, degree, institution, start_date, end_date)
