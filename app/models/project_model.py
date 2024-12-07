# app/models/project.py
class Project:
    def __init__(self, id=None, user_id=None, title=None, description=None, url=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.url = url

