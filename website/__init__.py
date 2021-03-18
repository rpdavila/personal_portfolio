import os
from flask import Flask
from flask_mail import Mail

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = os.getenv('portfolio')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('Email_User')
app.config['MAIL_PASSWORD'] = os.getenv('Email_Pass')
mail = Mail(app)

from website import routes
