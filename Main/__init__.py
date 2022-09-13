from unicodedata import category
from flask import Blueprint, render_template, redirect, session, request
from Main.data_utils import *

main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='.static')


@main_bp.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the homepage of the site
    """

    # If the user is not logged in redirect to log in
    if session.get('id') is None:
        return redirect('/login')

    content = get_categories()
    # If the user is logged in show the homepage
    return render_template('home.html', content=content)


@main_bp.route('/movie')
def details():
    movie_id = request.args.get('id')
    movie_data = movie_details_more(movie_id)

    return render_template('movie_details.html', movie=movie_data)


@main_bp.route('/show_more')
def show_more():    
    categorie = request.args.get('categorie')
    part = int(request.args.get('part'))
    
    movies_big = get_categories(categorie=categorie, number=3000)
    movies = content_divider(movies_big, 30, part-1)

    max = ceil(len(movies_big)/30)

    return render_template('show.html', categorie=categorie, movies=movies, part=part, max=max, func='/show_more')


@main_bp.route('/search')
def search():
    search = request.args.get('search')
    part = int(request.args.get('part'))


    answer = search_movies(search)
    if answer:
        movies = content_divider(answer, 10, part-1)

        max = ceil(len(answer)/10)

        return render_template('search.html', search=search, movies=movies, part=part, max=max)
    return render_template('search.html')


@main_bp.route('/more/')
def more():
    categorie = request.args.get('categorie')
    part = request.args.get('part')
    if part:
        part = int(part)
    else:
        part = 1
        
    movies = movies_by_genre(categorie)

    movies_divided = content_divider(movies, 36, part-1)

    max= ceil(len(movies)/36)

    return render_template('show.html', categorie=categorie, movies=movies_divided, part=part, max=max, func='/more/')
    
