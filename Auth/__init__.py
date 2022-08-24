from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from utils import *
import sqlite3

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='.static')

# Connect to the database
connection = sqlite3.connect('./database.db')
db = connection.cursor()



# register page
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Render the register page of the site
    """
    # When the user press create account
    if request.method == 'POST':
        # Get the name, the password and the confirmation
        name = request_username()
        password = request_pass('password')
        password_confirm = request_pass('password_confirm')

        # if one of the data is none return an error
        if name is None or password is None or password_confirm is None:
            return redirect('/register')

        # Error if the passwords don't match
        if password != password_confirm:
            flash('Passwords do not match')
            return redirect('/register')

        # Insert into database only if the user not exists yet
        if not name_in_database(name):
            if insert_user(name, password):
                id = login_user(name, password)
                session['id'] = id
                flash('Account created successfully')
                return redirect('/')
            flash('Error')
            return redirect('/register')
        
        # When the name is already in the database
        flash('Username already exists')
        return redirect('/register')

    return render_template('register.html')

# login page
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Render the Login page of the site
    """
    if request.method == 'POST':
        # Get the name and the password of the user
        name = request_username()
        password = request_pass('password')
        
        # if one of the data is none return an error
        if name is None or password is None:
            return redirect('/login')
        
        # If the user exists
        if name_in_database(name):
            # Get the id of the user
            id = login_user(name, password)
            if id:
                session['id'] = id
                flash('Successfully logged in')
                return redirect('/')
            
            flash("Incorrect Password")
            return redirect('/login')

        flash("Username Not exists")
        return redirect('/login')

    return render_template('login.html')

# logout page
@auth_bp.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/')
