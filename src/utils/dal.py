from mysql.connector import connect
from utils.app_config import AppConfig


class Dal:

    # Constructor function
    def __init__(self):

        # Connection to the database
        self.connection = connect(host=AppConfig.mysql_host, user=AppConfig.mysql_user,
                                  password=AppConfig.mysql_password, database=AppConfig.mysql_database)

    # Get entire table
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()  # Get the table
            return table

    # Get one item
    def get_item(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            item = cursor.fetchone()  # Get the item
            return item

    # Insert new item
    def insert_item(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save the database
            last_row_id = cursor.lastrowid  # Get the last row id
            return last_row_id

    # Update an item 
    def update_item(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database
            row_count = cursor.rowcount 
            return row_count
        
    # Delete an item 
    def delete_item(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database
            row_count = cursor.rowcount 
            return row_count
    
    # Close resources
    def close(self):
        self.connection.close()
