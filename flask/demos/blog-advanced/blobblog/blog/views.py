from flask import render_template, Blueprint, redirect, url_for, flash, abort, request
from .models import Post
from .. import db
from .forms import PostForm

blog = Blueprint('blog', __name__)


@blog.route('/')
def index():
    posts = db.session.execute(db.select(Post).order_by(Post.created_at)).scalars()
    return render_template('index.html', posts=posts)


@blog.route('/create', methods=('GET', 'POST'))
def create():
    """creation d'un post"""
    form = PostForm()

    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        flash('post created')
        return redirect(url_for('blog.index'))

    return render_template('blog/create.html', form=form)


@blog.get('/<int:id>/update')
def update(id: int):
    """maj d'un post"""
    post = db.session.get(Post, id)

    if post is None:
        abort(404)

    form = PostForm(obj=post)

    return render_template('blog/update.html', form=form)


@blog.post('/<int:id>/update')
def update_post(id: int):
    form = PostForm()

    post = db.session.get(Post, id)

    if post is None:
        abort(404)

    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash('post updated')
        return redirect(url_for('blog.index'))

    return render_template('blog/update.html', form=form)


@blog.route('/<int:id>/delete')
def delete(id: int):
    post = db.session.get(Post, id)
    db.session.delete(post)
    db.session.commit()
    flash('post deleted')
    return redirect(url_for('blog.index'))
