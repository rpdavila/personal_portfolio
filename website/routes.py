from website import app, mail
from flask import render_template, request, redirect, url_for
from website.forms import ContactForm
from flask_mail import Message
import sqlite3


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit() and form.subject.data == "Constructive Feedback" or "Send Resume for Possible Hire"\
            or "Internship Opportunity":
        if request.method == "POST":
            if form.validate_on_submit():
                send_email(form)
                return redirect(url_for('home'))
    return render_template('contact.html', form=form, title='Contact')


def send_email(form):
    msg = Message(subject=f'{form.subject.data}',
                  sender=f'{form.email.data}',
                  recipients=['rafael.pietri@gmail.com'])
    msg.body = f'Hello my name is {form.name.data},\n{form.body.data}'
    mail.send(msg)


def db(form):
    pass


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')
