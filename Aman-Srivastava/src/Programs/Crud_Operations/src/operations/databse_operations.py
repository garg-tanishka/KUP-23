import logging

from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_db = "show databases"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
            logging.info("Task: fetching all db in (get_database) executed")

            if databases:
                status = 200
                logging.info("Task: returning all db in (get_database) executed")
                return databases, status
            else:
                msg = "None Database Exists!"
                status = 404
                logging.info("Task: no database found in (get_database) executed")
                return msg, status

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
            logging.info("Task: fetching all db in (get_database) executed")

            if db_name in databases:
                logging.info("Task: checking if db already exists in (create_database) executed")
                msg = f"Database: '{db_name}' already exists."
                status = 409
                return msg, status
            else:
                cursor.execute(f"create database {db_name}")
                connection.commit()
                msg = f"Database: '{db_name}' created."
                status = 201
                logging.info("Task: creating db in (create_database) executed")
                return msg, status

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
            logging.info("Task: fetching all db in (delete_database) executed")

            if db_name in databases:
                cursor.execute(f"drop database {db_name}")
                connection.commit()
                logging.info("Task: committing drop db in (delete_database) executed")
                msg = f"Deleted database: '{db_name}'"
                status = 200
                return msg, status
            else:
                msg = f"Failed to delete database: '{db_name}', does not exist"
                status = 404
                logging.info("Task: failed to delete db in (delete_database) executed")
                return msg, status

        except Exception as e:
            logging.error("Some error occured in: delete_database function")
            return str(e)
