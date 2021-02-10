from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, length, Email


class ContactForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), length(min=4)])
    email = EmailField('Email',
                       validators=[Email(), DataRequired()])

    body = TextAreaField('Message',
                         validators=[DataRequired(), length(min=4)])

    submit = SubmitField('Submit')
