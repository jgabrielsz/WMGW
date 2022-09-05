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

    # content = {
    #     'Previous Movies': get_movies(10),
    #     'Movies Released in This Year': movies_per_year(2022, 10),
    #     'Next Year Movies': movies_per_year(2023, 10),
    # }

    content = get_categories()
    # If the user is logged in show the homepage
    return render_template('home.html', content=content)


@main_bp.route('/movie')
def details():
    movie_id = request.args.get('id')
    movie_data = movie_details(movie_id)

    return render_template('movie_details.html', movie=movie_data)


@main_bp.route('/show_more')
def show_more():    
    categorie = request.args.get('categorie')
    part = int(request.args.get('part'))
    

    categ = get_categories(categorie=categorie, number=5000)
    movies = content_divider(categ, 36, part-1)

    max = ceil(len(categ)/36)

    return render_template('show_more.html', categorie=categorie, movies=movies, part=part, max=max)


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