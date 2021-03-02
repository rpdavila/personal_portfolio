import sqlite3
from sqlite3 import Error


def grab_country_data():
    try:
        conn = sqlite3.connect('db.sqlite')
        curs = conn.cursor()
        query = "SELECT country FROM main.country_id"
        curs.execute(query)
        return curs.fetchall()
    except Error as e:
        print(e)


def insert_from_contact_form(form):
    try:
        conn = sqlite3.connect('db.sqlite')
        cur = conn.cursor()
        insert_query = "INSERT INTO main.contact(name,email,subject,body) VALUES(?,?,?,?)"
        cur.execute(insert_query, (form.name.data, form.email.data, form.subject.data, form.body.data))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def get_data_to_html_table():
    try:
        conn = sqlite3.connect('db.sqlite')
        curs = conn.cursor()
        query = "SELECT country,name,url,volume,date FROM main.twitter_trends"
        curs.execute(query)
        data = curs.fetchall()
    except Error as e:
        print(e)
