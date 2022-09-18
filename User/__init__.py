from User.user_utils import *
from flask import Blueprint, render_template,session, redirect
from Main.data_utils import get_user_letter

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='.static')



@user_bp.route('/user')
def user():
    if not session.get('id'):
        return redirect('/login')

    user_letter = get_user_letter(session['id'])
    return render_template('user.html', letter=user_letter, username=get_username(session['id']))




