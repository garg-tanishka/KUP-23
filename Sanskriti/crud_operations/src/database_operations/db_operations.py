from src.utils.database_connection.connection import database_connection
from mysql.connector import Error

cursor, connection = database_connection()
view_db = "show databases"


class DatabaseOperations:
    def get_database():
        """
        getting the database from database connection and performing different operations
        @return: list of databases, tables in databases
        """
        try:
            operation = view_db
            cursor.execute(operation)
            databases = [row[0] for row in cursor.fetchall()]

            if databases:
                return databases
            else:
                return "None Database Exists!"

        except Error as e:
            return e

    def create_database(database_name):
        """
        Function to create database.
        @return: response message
        """
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if database_name in databases:
                return f"Database: '{database_name}' already exists."
            else:
                cursor.execute(f"create database {database_name}")
                connection.commit()
                return f"Database: '{database_name}' created."

        except Error as e:
            return e

    def delete_database(database_name):
        """
        Function to delete database.
        @return: response message
        """
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if database_name in databases:
                cursor.execute(f"drop database {database_name}")
                connection.commit()
                return f"Deleted database: '{database_name}'"
            else:
                return f"Failed to delete database: '{database_name}', does not exist"

        except Exception as e:
            return str(e)
