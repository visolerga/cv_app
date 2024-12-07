# app/models/job.py
class Job:
    def __init__(self, id=None, user_id=None, company=None, role=None, start_date=None, end_date=None, description=None):
        self.id = id
        self.user_id = user_id
        self.company = company
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

