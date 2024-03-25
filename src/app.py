from flask import Flask
from views.album_view import albums_blueprint
from views.home_view import home_blueprint
from views.about_us_view import about_us_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(albums_blueprint)
app.register_blueprint(about_us_blueprint)
