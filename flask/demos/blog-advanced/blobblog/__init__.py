import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "45f1a0c0-d026-4390-b637-cb451b35b403-8edb2384-4cea-4cf8-89e6-a70722f9d583"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    # Add init db command to flask cli
    app.cli.add_command(init_db_command)

    # import blog blueprint to the app
    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    # import auth blueprint to the app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    db.init_app(app)

    return app


def init_db():
    db.drop_all()
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('database initialized')
