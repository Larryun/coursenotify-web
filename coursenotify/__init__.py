import os

from flask import Flask

from coursenotify import db


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.app_context()

    env = os.environ.get("ENV")
    if env is None or env == "development":
        app.config.from_pyfile("dev/config.dev.py", silent=False)
    elif env == "production":
        app.config.from_pyfile("prod/config.prod.py")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if app.config["UPDATE_COLLECTION"]:
        with app.app_context():
            db.init_course_db()

    from coursenotify.views.index import frontend
    app.register_blueprint(frontend)

    return app
