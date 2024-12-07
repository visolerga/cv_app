# app/services/project_service.py
from app.models.project_model import Project

def create_project(user_id, title, description, url):
    return Project(user_id, title, description, url)
