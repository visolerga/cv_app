# app/models/education.py
class Education:
    def __init__(self, id=None, user_id=None, degree=None, institution=None, start_date=None, end_date=None):
        self.id = id
        self.user_id = user_id
        self.degree = degree
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date

