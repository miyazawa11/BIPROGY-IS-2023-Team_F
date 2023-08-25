from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import click

db = SQLAlchemy()
ma = Marshmallow()

# アプリでDB操作を行えるように初期設定する
def init_db(app):
    db.init_app(app)
    ma.init_app(app)


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')
