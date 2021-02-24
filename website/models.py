from datetime import datetime
from website import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, subject, body):
        self.name = name
        self.email = email
        self.subject = subject
        self.body = body

