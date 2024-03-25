from flask import Blueprint, render_template,  redirect, url_for, request
from facades.album_facade import AlbumFacade
from facades.track_facade import TracksFacade

# Managing the entire view
# "albums" is the name of the view
albums_blueprint = Blueprint("albums", __name__)
albums_facade = AlbumFacade()
tracks_facade = TracksFacade()



# Display all albums
@albums_blueprint.route("/albums")
def albums():
    albums = albums_facade.get_albums()
    return render_template("album.html", albums=albums)


# Add album
@albums_blueprint.route("/albums/new", methods=["GET", "POST"])
def insert():
    if request.method == "GET":
        return render_template("insert.html")
    albums_facade.add_album()
    return redirect(url_for("albums.albums"))


# Update existing album
@albums_blueprint.route("/albums/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        album = tracks_facade.get_tracks_according_to_album(id)
        return render_template("edit.html", album = album)
    albums_facade.update_album()
    return redirect(url_for("albums.albums"))


# Delete album
@albums_blueprint.route("/albums/delete/<int:id>")
def delete(id):
    albums_facade.delete_album(id)
    return redirect(url_for("albums.albums"))

# Get album songs
@albums_blueprint.route("/albums/details/<int:id>")
def details(id):
    album = tracks_facade.get_tracks_according_to_album(id)
    return render_template("track.html", album = album)


# Purchase album
@albums_blueprint.route("/albums/purchase/<int:id>", methods=["GET", "POST"])
def purchase(id):
    album = albums_facade.get_album(id)
    if request.method == "POST":
        return redirect(url_for("albums.confirmation",  album= album, id = id))
    return render_template("purchase.html", album = album)

@albums_blueprint.route("/albums/purchase/<int:id>/confirmation", methods=["GET", "POST"])
def confirmation(id):
    album = albums_facade.get_album(id)  
    return render_template("confirmation.html", album = album, id= id)