from website import app, mail
from flask import render_template, request, redirect, url_for
from website.forms import ContactForm
from flask_mail import Message
import sqlite3
from sqlite3 import Error


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            db_connect(form)
            send_email(form)
            return redirect(url_for('home'))
    return render_template('contact.html', form=form, title='Contact')


def send_email(form):
    msg = Message(subject=f'{form.subject.data}',
                  sender=f'{form.email.data}',
                  recipients=['rafael.pietri@gmail.com'])
    msg.body = f'Hello my name is {form.name.data},\n{form.body.data}'
    mail.send(msg)


def db_connect(form):
    try:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        insert_query = "INSERT INTO contact(name,email,subject,body) VALUES(?,?,?,?)"
        cur.execute(insert_query, (form.name.data, form.email.data, form.subject.data, form.body.data))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')
