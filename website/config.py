from website import app
from flask_mail import Mail
import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('Email_User')
app.config['MAIL_PASSWORD'] = os.getenv('Email_Pass')
mail = Mail(app)
