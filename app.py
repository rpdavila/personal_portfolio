from flask import Flask, url_for, render_template, redirect
from forms import ContactForm
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOMETHING_SECRET'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return f'name: {form.name.data}, email: {form.email.data}, message: {form.body.data}'
    return render_template('contact.html', form=form, title='Contact')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


if __name__ == '__main__':
    app.run(debug=True)
