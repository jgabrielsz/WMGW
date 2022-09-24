from User.user_utils import *
from flask import Blueprint, render_template,session, redirect, request
from Main.data_utils import get_user_letter

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='.static')



@user_bp.route('/user', methods=['GET', 'POST'])
def user():
    if not session.get('id'):
        return redirect('/login')

    if request.method == 'POST':
        password = request.form.get('password')
        if password:
            name = get_username(session.get('id'))
            deleted = delete_user_db(name, password)
            if deleted:
                return redirect('/login')


    user_letter = get_user_letter(session['id'])
    return render_template('user.html', letter=user_letter, username=get_username(session['id']))


@user_bp.route('/change_username', methods=['GET', 'POST'])
def change_username():
    new_username = request_username()
    if new_username:
        changer_username(new_username)
    return redirect('/user')


