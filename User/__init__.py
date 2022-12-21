from User.user_utils import *
from flask import Blueprint, render_template,session, redirect, request
from Main.data_utils import get_user_letter
from Auth.login_required import login_required

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='.static')



@user_bp.route('/user', methods=['GET', 'POST'])
@login_required
def user():

    #Delete account
    if request.method == 'POST':
        password = request.form.get('password')
        if password:
            deleted = delete_user_db(session.get('id'), password)
            if deleted:
                return redirect('/login')
            else:
                return redirect('/user')

    user_letter = get_user_letter(session['id'])
    return render_template('user.html', letter=user_letter, username=get_username(session['id']))


@user_bp.route('/change_username', methods=['GET', 'POST'])
@login_required
def change_username():
    new_username = request_username()
    if new_username:
        changer_username(new_username, session.get('id'))
    return redirect('/user')


