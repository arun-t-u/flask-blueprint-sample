from flask import Blueprint

site = Blueprint('site',__name__, url_prefix='/site')

@site.route('/home')
def index():
    return "Welcome to the Home Page"