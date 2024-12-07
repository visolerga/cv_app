# app/services/user_service.py
# from app.models.contact_model import ContactModel
# from app.services.contact_service import get_contact_by_id
# from app.services.skill_service import get_skills_by_user_id
# from app.services.job_service import get_jobs_by_user_id
# from models.contact_model import Contact
# from services.contact_service import get_contact_by_id
# from services.skill_service import get_skills_by_user_id
# from services.job_service import get_jobs_by_user_id

from ..models.contact_model import Contact
from .contact_service import get_contact_by_id
from .skill_service import get_skills_by_user_id
from .job_service import get_jobs_by_user_id

def get_full_user_data(user_id):
    """Obtiene todos los datos de un usuario dado su ID."""
    contact = get_contact_by_id(user_id)
    skills = get_skills_by_user_id(user_id)
    jobs = get_jobs_by_user_id(user_id)
    # Agrega otras categorías según sea necesario
    return {
        "contact": contact,
        "skills": skills,
        "jobs": jobs
    }


# Podrías incluir funciones como `create_user` o `delete_user` aquí.

