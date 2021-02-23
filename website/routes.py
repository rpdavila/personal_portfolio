from website import app
from flask import render_template
from website.forms import ContactForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return f'name: {form.name.data}, email: {form.email.data}, subject: {form.subject.data}, ' \
               f'message: {form.body.data}'
    return render_template('contact.html', form=form, title='Contact')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')
