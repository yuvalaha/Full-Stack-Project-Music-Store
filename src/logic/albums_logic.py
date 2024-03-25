from utils.dal import Dal

class AlbumLogic:

    # Constructor function
    def __init__(self):
        self.album_dal = Dal()

    # Get all albums
    def get_albums(self):
        sql = "SELECT * FROM album_full_details"
        table = self.album_dal.get_table(sql)
        return table

    # Get one album
    def get_album(self, id):
        sql = "SELECT * FROM album_full_details WHERE id = %s"
        print(id)
        return self.album_dal.get_item(sql, (id,))

    # Add new album
    def add_album(self, album):
        sql = "INSERT INTO album_full_details (album_name, band, genre, composer, total_length, price) VALUES (%s, %s, %s, %s, %s)"
        self.album_dal.insert_item(sql, (album.album_name, album.band, album.genre, album.composer, album.length, album.price))

    # # Update existing album
    # def update_album(self, album):
    #     sql = "UPDATE album_full_details SET album_name=%s, band=%s, genre=%s, composer=%s, total_length=%s WHERE id = %s"
    #     self.album_dal.update_item(sql, (album.album_name, album.band, album.genre, album.composer, album.length, album.id))

    # Delete existing album:
    def delete_album(self, id):
        sql = "DELETE FROM album_full_details WHERE id = %s"
        self.album_dal.delete_item(sql, (id,))

    # Close resources
    def close(self):
        self.album_dal.close()
