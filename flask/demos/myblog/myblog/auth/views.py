from flask import Blueprint, flash, redirect, render_template, request, url_for
from myblog import db
from .models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return 'hello'

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        error = ''
        username = request.form['username']
        password = request.form['password']

        if not username or len(username) > 50:
            error += 'wrong username'

        if not password or len(password) > 50:
            error += 'wrong password'

        # Création d'un requête
        query = (db.select(User).filter_by(username=username))

        # Vérification que l'utilisateur n'existe pas
        if db.session.execute(query).scalar() is not None:
            error += 'user already exist'


        if error == '':
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/user/<int:id>')
def user_detail(id: int):
    user = db.get_or_404(User, id)
    return render_template('auth/user_detail.html', user=user)