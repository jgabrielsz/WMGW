from crypt import methods
from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from utils import *


main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='.static')



@main_bp.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the homepage of the site
    """

    # If the user is not logged in redirect to login
    if session.get('id') is None:
        return redirect('/login')

    # If the user is logged in show the homepage
    return render_template('home.html')
    