import sqlite3
from Auth.login_utils import login_user, request_username



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

def delete_user_db(name, password):
    """
    Function to delete a user from the database \n
    Parameters: name, password \n
    Return True if success, and False if not.
    """
    if name_in_database(name):
        if not login_user(name, password):
            return False
            
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute("DELETE FROM users WHERE name = ?", [name])
        connection.commit()
        connection.close()
        if not name_in_database(name):
            return True
    return False

def changer_username(new_username):
    """
    Function to change the username \n
    Parameters: new_username \n
    Return: True if success, false if not
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('UPDATE users SET name = ?', (new_username, ))
    connection.commit()
    connection.close()

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

    if username[0]:
        return username[0][0]
    return False



if __name__ == "__main__":
    print(get_username(1))