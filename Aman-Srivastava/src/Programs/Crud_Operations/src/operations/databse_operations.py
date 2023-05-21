import logging

from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_db = "show databases"


class DatabaseOperations:
    @staticmethod
    def get_database():
        """
        Function to perform operation like get all existing database,
        show tables in database.
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

        except Exception as e:
            logging.error("Some error occured in: get_database function")
            return str(e)

    @staticmethod
    def create_database(db_name):
        """
        Function to create database.
        @return: response message
        """
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if db_name in databases:
                return f"Database: '{db_name}' already exists."
            else:
                cursor.execute(f"create database {db_name}")
                connection.commit()
                return f"Database: '{db_name}' created."

        except Exception as e:
            logging.error("Some error occured in: create_database function")
            return str(e)

    @staticmethod
    def delete_database(db_name):
        """
        Function to delete database.
        @return: response message
        """
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if db_name in databases:
                cursor.execute(f"drop database {db_name}")
                connection.commit()
                return f"Deleted database: '{db_name}'"
            else:
                return f"Failed to delete database: '{db_name}', does not exist"

        except Exception as e:
            logging.error("Some error occured in: delete_database function")
            return str(e)
