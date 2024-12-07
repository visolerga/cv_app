# app/models/social_link.py
class SocialLink:
    def __init__(self, id=None, user_id=None, platform=None, url=None):
        self.id = id
        self.user_id = user_id
        self.platform = platform
        self.url = url
