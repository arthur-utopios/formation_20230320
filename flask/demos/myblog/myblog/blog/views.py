
from flask import Blueprint, render_template, request

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/index.html')
