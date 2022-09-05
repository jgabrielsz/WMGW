import sqlite3
import movieposters as mp
from math import ceil
from os.path import exists


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


def movie_details_less(id):
    """
    Get the movie data(less)
    Parameters: id: string
    Return a dict with the data
    """
    # Movies data
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    db.execute('SELECT * FROM movies WHERE id = (?)', (id, ))
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
        if exists(f'/home/gabriel/Documents/Final project/static/posters/{movie["id"]}.jpg'):
            movie['poster'] = True
        else:
            movie['poster'] = False

        if movie['genres'] == r"\N":
            movie['genres'] = ''

        return movie
        
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

    #directors and writers
    db.execute('SELECT directors, writers FROM producers WHERE id = ?', (id, ))
    connection.commit()
    directors_writers_ids = db.fetchall()
    #directors = []
    #writers = []
    directors = person_details(directors_writers_ids[0][0])
    writers = person_details(directors_writers_ids[0][1])
   

    if movie_data:
        movie = {
            'id': movie_data[0][0],
            'title': movie_data[0][1],
            'year': movie_data[0][2],
            'genres': movie_data[0][3],
            'people': people_in_movie(movie_data[0][0])
        }
        if exists(f'/home/gabriel/Documents/Final project/static/posters/{movie["id"]}.jpg'):
            movie['poster'] = True
        else:
            movie['poster'] = False
        people = people_in_movie(movie_data[0][0])
        if people:
            movie['people'] = people_in_movie(movie_data[0][0])
        else:
            movie['people'] = ''
        
        return movie
    return False


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
    query = f"SELECT id FROM movies WHERE title LIKE '%{movie}%' LIMIT 5000"

    db.execute(query)
    connection.commit()
    ids = db.fetchall()
    movies = list()

    if ids:
        for id in ids:
            movies.append(movie_details_less(id[0]))

        connection.close()
        return movies
    return None


def get_categories(number=10, categorie=None):
    content = {
        'Previous Movies': get_movies(number),
        'Movies Released in This Year': movies_per_year(2022, number),
        'Next Year Movies': movies_per_year(2023, number)
    }
    if categorie:
        movies = content[categorie]
        content.clear()
        return movies
    return content


def content_divider(content, number_items, part):
    """
    Function to returd a part of a content \n
    Paremeters: number_items: nomber of each part will have, part: to return \n
    Return: list of items
    """
    if number_items > len(content):
        return content
    
    content_divided = list()

    #index to insert in content divided
    i = 0

    number_of_parts = ceil(len(content)/number_items)
    
    for _ in range(number_of_parts):
        content_divided.append(list())

    for t, item in enumerate(content):
        content_divided[i].append(item)
        if (t+1) % number_items == 0:
            i+=1

    return content_divided[part]
        


if __name__ == '__main__':
    pass
