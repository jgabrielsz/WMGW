import sqlite3
from Auth.login_utils import login_user, request_username
from flask import flash



def name_in_database(name):
    """
    Function to verify if the name is already in the database \n
    Parameters: name: String \n
    Return True if Yes, and False if not.
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute("SELECT id FROM users WHERE name = ?", [name])
    connection.commit()
    resp = db.fetchall()
    connection.close()

    if resp:
        print('Tem')
        return True
    print('Não tem')
    return False


def id_by_name(user_name):
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute("SELECT id FROM users WHERE name = ?", [user_name])
    connection.commit()
    name = db.fetchall()
    connection.close()

    if name: 
        return name
    return False


def delete_user_db(user_id, password):
    """
    Function to delete a user from the database \n
    Parameters: name, password \n
    Return True if success, and False if not.
    """
    name = get_username(user_id)
    if name_in_database(name):
        if login_user(name, password):
            connection = sqlite3.connect('database.db')
            db = connection.cursor()
            db.execute('DELETE FROM users_lists WHERE id = ?', (user_id,))
            connection.commit()
            connection.close()

            connection = sqlite3.connect('database.db')
            db = connection.cursor()
            db.execute('DELETE FROM users WHERE id = ?', (user_id,))
            connection.commit()
            connection.close()

            if not name_in_database(get_username(user_id)):
                print('Deleted')

            return True
        else:
            flash('Password incorrect')
            return False
    else:
        flash('username not in database')
        return False
        


def changer_username(new_username,user_id):
    """
    Function to change the username \n
    Parameters: new_username \n
    Return: True if success, false if not
    """
    if name_in_database(new_username):
        flash('username already exists')
        return
    else:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute('UPDATE users SET name = ? WHERE id = ?', (new_username,user_id))
        connection.commit()
        connection.close()

        if not name_in_database(new_username):
            flash('Error')
            return    
    return


def get_username(id:int):
    """
    Function to get the user name by the id \n
    Parameters: id: int \n
    Return: username: string
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT name FROM users WHERE id = ?', (id, ))
    connection.commit()

    username = db.fetchall()

    connection.close()

    if username:
        return username[0][0]
    return False



if __name__ == "__main__":
    pass