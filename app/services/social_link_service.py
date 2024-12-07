# app/services/social_link_service.py
from app.models.social_link_model import SocialLink

def create_social_link(user_id, platform, url):
    return SocialLink(user_id, platform, url)
