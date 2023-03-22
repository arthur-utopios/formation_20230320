import os
import click
from flask import Flask, url_for
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
toolbar = DebugToolbarExtension()


# application factory
def create_app(config):
    app = Flask(__name__)

    db_url = os.getenv('DATABASE_URL', "sqlite:///myblog.db")

    # configuration de l'application
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DEBUG = True,
        SQLALCHEMY_DATABASE_URI = db_url
    )

    # initialisation de SqlAlchemy
    db.init_app(app)

    # initialisation de la toolbar
    toolbar.init_app(app)

    # Ajout de la commande d'initialisation de la db à l'app Flask
    app.cli.add_command(init_db_command)

    from myblog import auth, blog

    # ajout du blue print du blog
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)

    return app

def init_db():
    db.drop_all()
    db.create_all()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('database initialized')
