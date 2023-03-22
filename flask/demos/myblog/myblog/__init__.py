import os
import click
from flask import Flask, url_for
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from . import blog

db = SQLAlchemy()

# application factory
def create_app():
    app = Flask(__name__)

    db_url = os.getenv('DATABASE_URL', 'sqlite:///blog.sqlite')

    # configuration de l'application
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DEBUG = True,
        SQLALCHEMY_DATABASE_URI = db_url
    )

    # initialisation de SqlAlchemy
    db.init_app(app)

    # Ajout de la commande d'initialisation de la db à l'app Flask
    app.cli.add_command(init_db_command)

    # ajout du blue print du blog
    app.register_blueprint(blog.bp)

    return app

def init_db():
    db.drop_all()
    db.create_all()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('database initialized')
