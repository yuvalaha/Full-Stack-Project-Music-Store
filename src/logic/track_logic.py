from utils.dal import Dal

# Constructor function
class TrackLogic:
    def __init__(self):
        self.track_dal = Dal()

    # Get all tracks
    def get_tracks(self):
        sql = "SELECT * FROM track"
        table = self.track_dal(sql)
        return table
    
    # Get one track 
    def get_track(self):
        sql = "SELECT * FROM track  WHERE TrackId = %s"
        scalar = self.track_dal.get_item(sql, (id, ))
        return scalar
        
    # Get tracks according to album
    def get_tracks_according_to_album(self, id):
        sql = "SELECT * FROM track WHERE AlbumId = %s"
        table = self.track_dal.get_table(sql, (id,))  
        return table


    # Add new track
    def add_track(self, track):
        sql = "INSERT INTO track(Name, GenreId, Composer, length, megabytes) VALUES (%s, %s, %s, %s, %s)"
        self.track_dal.insert_item(sql, (track.name, track.genre_id, track.composer, track.length, track.megabytes))
        
    # # Update existing track
    # def update_track(self, track):
    #     sql = "UPDATE track SET Name=%s, AlbumId = %s, GenreId = %s, Composer = %s, Milliseconds = %s, Bytes = %s WHERE TrackId = %s "
    #     self.track_dal.update_item(
    #         sql, (track.name, track.album_id, track.genre_id, track.composer, track.millie_seconds, track.bytes, track.track_id))

    # # Delete existing track:
    # def delete_track(self, id):
    #     sql = "DELETE FROM track WHERE TrackId = %s"
    #     self.track_dal.delete_item(sql, (id,))

    # Close resources
    def close(self):
        self.track_dal.close()
