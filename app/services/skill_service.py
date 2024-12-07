# app/services/skill_service.py
from app.models.skill_model import Skill

def create_skill(name, source_type, source_id, user_id):
    return Skill(name, source_type, source_id, user_id)
