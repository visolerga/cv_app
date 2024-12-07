# app/models/skill.py
class Skill:
    def __init__(self, id=None, name=None, source_type=None, source_id=None, user_id=None):
        self.id = id
        self.name = name
        self.source_type = source_type
        self.source_id = source_id
        self.user_id = user_id

