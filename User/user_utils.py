import sqlite3



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

def change_username():
    ...

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