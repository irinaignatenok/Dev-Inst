import flask

learninb_hub_bp= flask.Blueprint('hub', __name__, template_folder="templates")

from . import views