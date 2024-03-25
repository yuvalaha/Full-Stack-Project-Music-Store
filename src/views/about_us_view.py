from flask import Blueprint, render_template

about_us_blueprint = Blueprint("about_us", __name__)

@about_us_blueprint.route("/about_us")
def about_us():
    return render_template("about_us.html")
