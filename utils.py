from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, flash
import sqlite3


def request_username():
    """
    Function to get the username from the form and validate it \n
    Parameters: None \n
    Return: username if there is no error, and None for errors
    """
    username =  request.form.get('username')
    answer = []
    
    if not username or username.isspace() or username is None:
        answer.append('Username is required')
    elif ' ' in username:
        answer.append('Username must not contain spaces')
    elif len(username) < 3:
        answer.append('Username must be at least 3 characters')
    elif len(username) > 15:
        answer.append('Username must be less than 15 characters')
    elif not username.isalnum():
        answer.append('Username must contain only alphanumeric characters')
    elif not username[0].isalpha():
        answer.append('Username must start with an alphabetic character')
    
    if len(answer) > 0:
        flash(answer[0].capitalize())
        return None
    return username

def request_pass(passwd):
    """
    Function to get the password from the form and validate it \n
    Parameters: passwd: String \n
    Return: password if there is no error, and None for errors
    """
    password = request.form.get(passwd)
    answer = []
    
    if not password or password.isspace() or password is None:
        answer.append(f'{passwd} is required')
    elif ' ' in password:
        answer.append(f'{passwd} must not contain spaces')
    elif len(password) < 6:
        answer.append(f'{passwd} must be at least 6 characters')

    if len(answer) > 0:
        flash(answer[0].capitalize())
        return None
    return password

def name_in_database(name):
    """
    Function to verify if the name is already in the database \n
    Parameters: name: String \n
    Return True if Yes, and False if not.
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute("SELECT * FROM users WHERE name = ?", [name])
    connection.commit()
    resp = db.fetchall()
    connection.close()
    
    if len(resp) == 0:
        return False
    return True

def insert_user(name, password):
    """
    Function to insert a new user into the database \n
    Parameters: name, password \n
    Return True if success, and False if not.
    """
    if name_in_database(name):
        return False

    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute("INSERT INTO users(name, hash) VALUES (?, ?)", [name, generate_password_hash(password)])
    connection.commit()
    connection.close()
    
    if name_in_database(name):
        return True
    return False

def delete_user(name):
    """
    Function to delete a user from the database \n
    Parameters: name, password \n
    Return True if success, and False if not.
    """
    if name_in_database(name):
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute("DELETE FROM users WHERE name = ?", [name])
        connection.commit()
        connection.close()
        if not name_in_database(name):
            return True
        return False
    return False

def login_user(name, password):
    """
    Function to return the id of the user \n
    Parameters: name, passwords \n
    Return: id of the user if success, and 0 if not
    """
    if name_in_database(name):
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute("SELECT id, hash FROM users WHERE name = ?", [name])
        connection.commit()
        hash = db.fetchall()
        connection.close()

        #Return the id only if the passwords match
        if check_password_hash(hash[0][1], password):
            return hash[0][0]
    # When the password is incorrect
    return 0


# To run tests durring the development
if __name__ == "__main__":
    pass