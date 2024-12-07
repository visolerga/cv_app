# app/models/course.py
class Course:
    def __init__(self, id=None, user_id=None, title=None, institution=None, completion_date=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.institution = institution
        self.completion_date = completion_date

