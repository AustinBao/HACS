from flask import Blueprint
import flask

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return flask.render_template('signup.html')