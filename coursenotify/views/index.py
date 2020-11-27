from flask import Blueprint, current_app, send_file, url_for
import os

frontend = Blueprint("index",
                     __name__,
                     url_prefix="/",
                     static_folder="static/frontend/dist/",
                     static_url_path="")


@frontend.route("/")
def index():
    return send_file(os.path.join(current_app.config["VUE_DIST_DIR"], "index.html"))
