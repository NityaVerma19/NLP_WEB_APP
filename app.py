from flask import Flask, render_template, request, redirect
#render template loads html files
from db import Database
import api
app = Flask(__name__) #object of Flask class
dbo = Database()


@app.route('/')  #a decorator. routes are basically urls
#is someone adds a '/' at the end of the website, then login page will open

def index():
    return render_template('login.html')  #<h1> is a tag in html. Text becomes a heading
#using CSS to improve the style of the webpage
#yaha clients google hai and server pycharm

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/perform_registration', methods =['post']) #we have to specify ki data post se aa raha hai
def perform_registration():
    name = request.form.get("user name")         #in these steps we fetched data from the user in html and brought it flask

    email = request.form.get('user email')
    password = request.form.get('user password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html' ,message = "Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message = "Email Already Exists!")
    return name+" "+email+" "+ password



@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user email')
    password = request.form.get('user password')

    response = dbo.search(email, password)
    if response == 1:
        return redirect("/profile")
    else:
        return render_template('login.html', mess="Incorrect Email/Password")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods = ["post"])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)



    return render_template('ner.html', response = response)

app.run(debug = True) #baar baar run nahi karna padega. Reload karne par changes execute honge


















