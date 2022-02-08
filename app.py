from flask import Flask
from example_blueprint import example_blueprint
from myapp.api.routes import api
from myapp.site.routes import site

app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.register_blueprint(api)
app.register_blueprint(site)


# @app.route("/")
# def index():
#     return "This is a sample"

