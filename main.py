from flask import Flask, request, redirect
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True )

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()


@app.route("/", methods=['POST'])
def welcome():

    user_name = request.form['user_name']
    user_password = request.form['user_password']
    user_verify = request.form['user_verify_password']
    user_email = request.form['user_email']
    error = ''
    
    


    if  user_name == '' or user_password == '' or user_verify == '':
        error = 'Please do not leave an empty field.'
        user_name = ''
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif re.search(r'\s',user_name) or re.search(r'\s',user_password):
        error = 'Invalid. Please do not use spaces.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif len(user_name) < 3 or len(user_name) > 20:
        error = 'User name must be greater than 3 or less than 20 characters.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif len(user_password) < 3 or len(user_password) > 20:
        error = 'Password must be greater than 3 or less than 20 characters.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif not user_password == user_verify:
        error = 'Password must match to verify.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif len(user_email) < 3 or len(user_email) > 20:
        error = 'Invalid Email.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    elif not re.match(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$',user_email):
        error = 'Invalid Email.'
        template = jinja_env.get_template('signup.html')
        return template.render(error=error)
    else:
        template = jinja_env.get_template('welcome.html')
        return template.render(name=user_name) 
    

              
app.run()