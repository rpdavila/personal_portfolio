from flask import Flask
from flask_mail import Mail
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = config.get('portfolio')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = config.get('Email_User')
app.config['MAIL_PASSWORD'] = config.get('Email_Pass')
mail = Mail(app)

from website import routes
