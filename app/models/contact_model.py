# app/models/contact.py
class Contact:
    def __init__(self, id=None, name=None, email=None, phone=None, address=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

