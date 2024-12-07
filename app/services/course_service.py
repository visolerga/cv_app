# app/services/course_service.py
from models.course import Course

def create_course(user_id, title, institution, completion_date):
    return Course(user_id, title, institution, completion_date)
