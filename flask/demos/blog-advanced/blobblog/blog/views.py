from flask import render_template, Blueprint, redirect, url_for, flash
from .models import Post
from .. import db
from .forms import PostForm

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def index():
    posts = db.session.execute(db.select(Post).order_by(Post.created_at)).scalars()
    return render_template('index.html', posts=posts)


@blog.route('/create', methods=('GET', 'POST'))
def create():
    """creation d'un post"""
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash('post created')
        return redirect(url_for('blog.index'))

    return render_template('blog/create.html', form=form)


@blog.route('/<int:id>/update', methods=('GET', 'POST'))
def update():
    """maj d'un post"""
    pass

@blog.route('/<int:id>/delete')
def delete():
    pass