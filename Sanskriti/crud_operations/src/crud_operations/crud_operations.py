from src.utils.database_connection.connection import database_connection

cursor, connection = database_connection()
view_table = "show tables"
no_table = "no such table exists!"
table_name = "knoldus"


class CrudOperations:
    @staticmethod
    def get_table_data():
        try:
            query = f"select * from {table_name}"
            cursor.execute(query)
            store = cursor.fetchall()
            return store
        except Exception as e:
            return str(e)










