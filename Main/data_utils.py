import sqlite3


def get_movies(number: int):
    """
    Get movies data from the database
    Parameters: number: int
    Return: List of dicts if success, False if not
    """
    number = str(number)
    if int(number) > 0:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute('SELECT * FROM movies LIMIT (?)', (number, ))
        connection.commit()
        bigdata = db.fetchall()
        connection.close()
        data_movies = list()

        for data in bigdata:
            data_movies.append({'id': data[0], 'title': data[1], 'year': data[2], 'genres': data[3]})

        if data_movies:
            return data_movies
    return False

def movies_per_year(year, number):
    """
    Get movies data from the database by year of release
    Parameters: year: int, number: int
    Return: List of dicts if success, False if not
    """
    number = str(number)
    year = str(year)
    if int(year) > 2000:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute('SELECT * FROM movies WHERE year = ? LIMIT ?', (year, number))
        connection.commit()
        bigdata = db.fetchall()
        connection.close()
        data_movies = list()

        for data in bigdata:
            data_movies.append({'id': data[0], 'title': data[1], 'genres': data[3]})

        if data_movies:
            return data_movies
    return False

def movie_details(id):
    """
    Get the movie data
    Parameters: id: string
    Return a dict with the data
    """
    # Movies data
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT * FROM movies WHERE id = (?)', (id, ))
    connection.commit()
    movie_data = db.fetchall()
    #print(movie_data)

    #directors and writers

    #db.execute('SELECT directors, writers FROM producers WHERE id = ?', (id, ))
    #connection.commit()
    #directors_writers_ids = db.fetchall()
    connection.close()

    if movie_data:
        movie = {
            'id': movie_data[0][0],
            'title': movie_data[0][1],
            'year': movie_data[0][2],
            'genres': movie_data[0][3],
        }
        return movie
    return 'NOT MOVIE'

if __name__ == '__main__':
    pass