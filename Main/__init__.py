from urllib import request
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

    content = {
        'Movies Released in This Year': movies_per_year(2022, 10),
        'Next Year Movies': movies_per_year(2023, 10),
    }


    # If the user is logged in show the homepage
    return render_template('home.html', content=content)


@main_bp.route('/movie')
def details():
    movie_id = request.args.get('id')
    movi = movie_details(movie_id)
    return render_template('movie_details.html', movie=movi)
