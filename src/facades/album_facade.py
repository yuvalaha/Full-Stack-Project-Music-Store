from logic.albums_logic import AlbumLogic
from flask import request # Request object arrived from the fronthand 
from models.album_model import AlbumModel


class AlbumFacade:
    
     # Constructor function 
    def __init__(self):
        self.album_logic = AlbumLogic()
        
    # Get all albums    
    def get_albums(self):
        return self.album_logic.get_albums()
    
    # Get album    
    def get_album(self, id):
        return self.album_logic.get_album(id)

    # Add new album
    def add_album(self):
        album_name = request.form.get("album_name") # <input type="text" name="album_name"/>
        band = request.form.get("band") # <input type="text" name="band"/>
        genre = request.form.get("genre") # <input type="text" name="genre"/>
        composer = request.form.get("composer") # <input type="text" name="composer"/>
        length = request.form.get("length")  # <input type="int" name="total_length"/>
        price = request.form.get("price")
        album = AlbumModel(None, album_name, band, genre, composer, length, price)
        self.album_logic.add_album(album)
        
    # # Update existing album
    # def update_album(self):
    #     id = request.form.get("id")
    #     album_name = request.form.get("album_name") 
    #     band = request.form.get("band") 
    #     genre = request.form.get("genre") 
    #     composer = request.form.get("composer") 
    #     length = request.form.get("length") 
    #     album = AlbumModel(id, album_name, band, genre, composer, length)
    #     self.album_logic.update_album(album)

    # Delete an album
    def delete_album(self, id):
        self.album_logic.delete_album(id)
    
    # Purchase an album
    def purchase(self, id):
        pass
    
    # Close Connection
    def close(self):
        self.album_logic.close()