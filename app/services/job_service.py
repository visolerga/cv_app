# app/services/job_service.py
from app.models.job_model import Job

def create_job(user_id, company, role, start_date, end_date, description):
    return Job(user_id, company, role, start_date, end_date, description)
