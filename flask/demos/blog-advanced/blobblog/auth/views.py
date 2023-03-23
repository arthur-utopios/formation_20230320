from flask import Blueprint, render_template
from .models import User
from .forms import UserForm

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')


@auth.route('/register', methods=('POST', 'GET'))
def register():
    """permet d'enregistrer un utilisateur"""
    form = UserForm()

    if form.validate_on_submit():
        print('hello')
        pass

    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=('POST', 'GET'))
def login():
    """permet de connecter un utilisateur"""
    return render_template('auth/login')
