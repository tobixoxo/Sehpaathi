import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from chat import chat

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    firstname = db.Column(db.String(100), nullable= False)
    lastname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(80), unique= True, nullable= False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone = True), 
    server_default = func.now())
    bio = db.Column(db.Text)
    Course = db.Column(db.String(100), nullable= False)
    def __repr__(self) -> str:
        return f'<Student {self.firstname}>'

CHAT_HISTORY = []
@app.route('/chatbot', methods = ['POST', 'GET'])
def chatbot():
    if request.method == 'POST':
        student_query = request.form['query']
        if student_query == "":
            return
        bot_response = chat(student_query)
        # print("Query is : ", bot_response)
        CHAT_HISTORY.append(student_query)
        CHAT_HISTORY.append(bot_response)
        return render_template('chatbot.html',CHAT_HISTORY = CHAT_HISTORY)
    return render_template('chatbot.html')

@app.route('/signup' , methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        print("hello world!")
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        course = request.form['Course']

        student = Student(firstname = firstname,
        lastname = lastname,
        email = email,
        age = age, 
        bio = bio,
        Course = course)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['firstname']
        email = request.form['email']
        if name == "" or email == "":
            return redirect(url_for('invalid_login'))
        id = db.session.query(Student.id).filter_by(email = email).first()[0]
        if id is not None:
            id_name = db.session.query(Student.firstname).filter_by(id = id).first()[0]
            print(id_name)
            if id_name == name:
                return redirect(url_for('chatbot'))
            else:
                return redirect(url_for('invalid_login'))
        else:
            return redirect(url_for('invalid_login'))
    return render_template('login.html')

@app.route('/error')
def invalid_login():
    return '<h1>invalid login!!</h1>'