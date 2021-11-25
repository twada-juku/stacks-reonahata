import os

from flask import Flask, render_template

# create_app 関数は Flask の Application Factory パターンを踏襲
# https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/#the-application-factory


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.get('/hello')
    def hello():
        return render_template('/hello.html.jinja')

    from .db import create_session
    sa_session = create_session(test_config)

    from . import projects
    app.register_blueprint(projects.create_bp(
        sa_session), url_prefix='/projects')

    return app
