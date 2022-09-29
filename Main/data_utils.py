import sqlite3
from math import ceil
import imdb
from time import time

ia = imdb.IMDb()


def movie_details_less(id):
    """
    Get the movie data(just id, title and poster bool) \n
    Parameters: id: string \n
    Return a dict with the data
    """
    # Movies data
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT id,title FROM movies WHERE id = (?)', (id, ))
    connection.commit()
    movie_data = db.fetchall()
    connection.close()


    if movie_data:
        return {
            'id': movie_data[0][0],
            'title': movie_data[0][1]
        }


def movie_details(id):
    """
    Get the movie data(id, title, year, genres and posters)
    Parameters: id: string
    Return a dict with the data
    """
    # Movies data
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT id,title,year,genres FROM movies WHERE id = (?)', (id, ))
    connection.commit()
    movie_data = db.fetchall()
    connection.close()


    if movie_data:
        movie = {
            'id': movie_data[0][0],
            'title': movie_data[0][1],
            'year': movie_data[0][2],
            'genres': movie_data[0][3]
        }

        movie['genres'] = movie['genres'].replace(',', ', ')

        if movie['genres'] == r"\N":
            movie['genres'] = ''
        

        return movie
        
    return False


def movie_details_more(id):
    """
    Get the movie data (id, title, year, genres, poster, directors, writers, people)
    Parameters: id: string
    Return a dict with the data
    """
    # Get some movie data
    movie_data = movie_details(id)

    #directors and writers
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT directors, writers FROM producers WHERE id = ?', (id, ))
    connection.commit()
    directors_writers_ids = db.fetchall()
    
    directors = person_details(directors_writers_ids[0][0])
    writers = person_details(directors_writers_ids[0][1])

    #If there is just one director or one writer put inside a list
    if type(directors) != list:
        directors = [directors]    
    if type(writers) != list:
        writers = [writers]

    if movie_data:
        movie = movie_data.copy()
        
        try:
            m_id = movie['id'][2:]
            plot = ia.get_movie(m_id)
            movie['plot'] = plot['plot']
        except:
            movie['plot'] = ''

        movie['directors'] = directors
        movie['writers'] = writers
        
        
        return movie
    return False


def person_details(id):
    """
    Get the person's data \n
    Parameters: person id: string \n
    Return: dict with data if success, and False otherwise
    """
    if ',' in id:
        list_ids = []
        ids = id.split(',')
        for i in ids:
            list_ids.append(person_details(i))
        return list_ids


    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT * FROM people WHERE id = ?', (id, ))
    connection.commit()
    person_bigdata = db.fetchall()
    connection.close()
    #id         name         professions              knownForTitles
    if person_bigdata:
        person_data = {
            'id': person_bigdata[0][0],
            'name': person_bigdata[0][1],
            'professions': person_bigdata[0][2],
            'knownForTitles': person_bigdata[0][3]
        }
        return person_data
    return False


def get_movies(number: int):
    """
    Get movies data from the database \n
    Parameters: number: int \n
    Return: List of dicts if success, False if not
    """
    number = str(number)
    if int(number) > 0:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute('SELECT id FROM movies ORDER BY title LIMIT (?)', (number, ))
        connection.commit()
        bigdata = db.fetchall()
        connection.close()
        data_movies = list()

        for data in bigdata:
            data_movies.append(movie_details_less(data[0]))

        if data_movies:
            return data_movies
    return False


def movies_per_year(year=2022, number=10):
    """
    Get movies data from the database by year of release, default is 2022
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
            data_movies.append(movie_details_less(data[0]))

        if data_movies:
            return data_movies
    return False


def next_year_movies(number):
    return movies_per_year(2023, number)


def people_in_movie(id):
    """
    Get the people know for the movie \n
    Parameters: id: Movie id : string \n
    Return: List of people, False if error
    """
    if type(id) == str and ';' not in id:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        query = f"SELECT * FROM people WHERE knownForTitles LIKE '%{id}%'"
        db.execute(query)
        connection.commit()
        people_data = db.fetchall()

        if people_data:
            return people_data
    return False


def search_movies(movie):
    """
    Function to search for a movie in the database \n
    Parameters: movie to search \n
    Return: List of dicts
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    query = f"SELECT id FROM movies WHERE title LIKE '%{movie}%' ORDER BY title LIMIT 5000"

    db.execute(query)
    connection.commit()
    ids = db.fetchall()
    movies = list()

    if ids:
        for id in ids:
            movies.append(movie_details(id[0]))

        connection.close()
        return movies
    return None

#Global variable
content = {
        'Previous Movies': get_movies,
        'Movies Released in This Year': movies_per_year,
        'Next Year Movies': next_year_movies
    }

def get_categories(number=10, categorie=None):
    if categorie:
        movies = content[categorie](number=number)
        return movies
    else:
        content_defined = dict()
        for key in content.keys():
            content_defined[key] = content[key](number=number)
        
        return content_defined


def movies_by_genre(genre):
    """
    Function to return movies by the genre \n
    Parameters: genre: string \n
    Return: List of dicts if success, false otherwise
    """
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    query = f'SELECT id FROM movies WHERE genres LIKE "%{genre}%"'
    
    db.execute(query)
    connection.commit()

    data = db.fetchall()
    if data:
        movies = list()
        for id in data:
            movies.append(movie_details_less(id[0]))
        
        return movies

    return False
        

def content_divider(content, number_items, part):
    """
    Function to return a part of a content \n
    Paremeters: number_items: nomber of each part will have, part: to return \n
    Return: list of items
    """
    if number_items > len(content):
        return content
    
    content_divided = list()
    number_items_in_content = len(content)
    #index to insert in content divided

    number_of_parts = ceil(number_items_in_content/number_items)
    if part > number_of_parts:
        return False

    index = part*number_items

    for _ in range(number_items):
        content_divided.append(content[index])
        index+=1

        if index == number_items_in_content:
            break
            

    return content_divided


def get_user_letter(id:int):
    """
    Get the first letter of the username by the id \n
    Parameters: id string \n
    Return: string with the letter
    """
    id = str(id)
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT name FROM users WHERE id = ? LIMIT 1', (id, ))
    connection.commit()
    name = db.fetchall()
    connection.close()
    if name:
        return name[0][0][0]
    return False

if __name__ == '__main__':
    pass
