from logic.track_logic import TrackLogic
from flask import request # Request object arrived from the fronthand 
from models.album_model import AlbumModel


class TracksFacade:
    
     # Constructor function 
    def __init__(self):
        self.track_logic = TrackLogic()
        
    # Get all tracks    
    def get_tracks(self):
        return self.track_logic.get_tracks()
    
    # Get one track    
    def get_track(self, id):
        return self.track_logic.get_track(id)
    
    # Get tracks according to album_id   
    def get_tracks_according_to_album(self, album_id):
        return self.track_logic.get_tracks_according_to_album(album_id)
    
    # Add new track
    def add_track(self):
        track_name = request.form.get("track_name") 
        genre_id = request.form.get("genre_id") 
        composer = request.form.get("composer") 
        length = request.form.get("length") 
        megabytes = request.form.get("megabytes") 
        track = AlbumModel(None, track_name, genre_id, composer, length, megabytes)
        self.track_logic.add_track(track)
        
    # # Update existing track
    # def update_track(self):
    #     track_id = request.form.get("track_id") 
    #     track_name = request.form.get("track_name") 
    #     album_id = request.form.get("album_id") 
    #     genre_id = request.form.get("genre_id") 
    #     composer = request.form.get("composer") 
    #     millie_seconds = request.form.get("millie_seconds") 
    #     bytes = request.form.get("bytes") 
    #     track = TrackModel(track_id, track_name, album_id, genre_id, composer, millie_seconds, bytes)
    #     self.track_logic.add_track(track)

    # # Delete track
    # def delete_track(self, id):
    #     self.track_logic.delete_track(id)
    
    # Close Connection
    def close(self):
        self.track_logic.close()