from flask import Blueprint

frontend = Blueprint("admin", __name__, url_prefix="/")


@frontend.route("/")
def index():
    return "HELLO WORLD WHYYYYYY"
