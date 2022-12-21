from flask import Blueprint, render_template, redirect, session, request, flash
from Main.data_utils import *
from Auth.login_required import login_required
from User.user_utils import get_username #to get username by id



main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='.static')

user_letter = 'Login'

@main_bp.route('/')
def home():
    """
    Render the home of the site
    """

    if session.get('id'):
        global user_letter
        user_letter = get_user_letter(session.get('id'))

    #tt10366460 -> img oscar active
    #list of 2022 Oscars
    oscars_movies = ['tt12789558', 'tt3228774', 'tt11286314', 'tt14039582', 'tt1160419', 'tt9620288', 'tt11271038', 'tt7740496', 'tt10293406', 'tt8721424', 'tt3581652']
    
    content = get_categories(number=25)
    
    return render_template('home.html', content=content, letter=user_letter, oscars=oscars_movies)


@main_bp.route('/movie/<movie_id>')
def details(movie_id):
    """
    Function to return the movie page\n
    Parameters: movie_id
    """
    
    #get all movie's data
    movie_data = movie_details_more(movie_id)

    #Check if the movie is in the user's watchlist
    if check_movie_in_list(movie_id, session.get('id')) == True:
        movie_in_list = True
    else:
        movie_in_list = False
    
    return render_template('movie_details.html', movie=movie_data, letter=user_letter, in_list=movie_in_list)


@main_bp.route('/search')
def search():
    """
    Function to return a search result\n
    No parameters\n
    """
    #movie to search
    search = request.args.get('search')

    #part of the search, 1 is the first
    part = int(request.args.get('part'))

    answer = search_movies(search)

    #If there are results for the search
    if answer:
        movies = content_divider(answer, 10, part-1)

        #number of pages
        max = ceil(len(answer)/10)

        return render_template('search.html', search=search, movies=movies, part=part, max=max, letter=user_letter)
    
    #If there is no results for the search
    return render_template('search.html')


@main_bp.route('/more/<categorie>/<part>')
def more(categorie, part):
    """
    Function to return a bunch of movies\n
    Parametes: categorie between list and movie categories, part of the list\n
    """

    part = int(part)
    watchlist = False
    
    if categorie == 'Watchlist':
        movies = users_movies(session.get('id'))
        if movies:
            watchlist = True
    else:
        movies = movies_by_genre(categorie)

    if not movies:
        return redirect('/')


    movies_divided = content_divider(movies, 36, part-1)

    max= ceil(len(movies)/36)

    return render_template('show.html', categorie=categorie, movies=movies_divided, part=part, max=max, letter=user_letter, watchlist=watchlist)


@main_bp.route('/add_to_list', methods=['GET', 'POST'])
@login_required
def add_to_list():
    movie_id = request.form.get('id')
    if insert_into_users_list(movie_id, session.get('id')):
        flash('Movie added to watchlist')
        return redirect(f'/movie/{movie_id}')
    else:
        flash('Movie not added')
        return redirect(f'/movie/{movie_id}')


@main_bp.route('/remove_to_list', methods=['GET', 'POST'])
@login_required
def remove_to_list():
    movie_id = request.form.get('id')

    if remove_movie_to_list(movie_id, session.get('id')):
        flash('Movie deleted to watchlist')
        return redirect(f'/movie/{movie_id}')
    else:
        flash('Movie not deleted')
        return redirect(f'/movie/{movie_id}')