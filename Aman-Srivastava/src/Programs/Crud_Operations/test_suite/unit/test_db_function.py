import unittest
import pytest
import logging

from src.utils.db.db_connection import db_connection

view_db = "show databases"
db_exist = "Database Exists"
table_data = "Table in aman_knoldus are: [('aman',), ('knoldus',), ('practice',)]"
cursor, connection = db_connection()


@pytest.fixture
def db_name():
    return "test_database"


class TestDatabaseOperations:
    @staticmethod
    def test_get_database():
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
                return "databases exists"
            else:
                return "None Database Exists!"

        except Exception as e:
            logging.error("Some error occured in: get_database function")
            return str(e)

    @staticmethod
    def test_create_database(db_name):
        """
        Function to create database.
        @return: response message
        """
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if db_name in databases:
                return "Database: aman_knoldus already exists."
            else:
                cursor.execute(f"create database {db_name}")
                connection.commit()
                return "Database Created"

        except Exception as e:
            logging.error("Some error occured in: create_database function")
            return str(e)

    @staticmethod
    def test_delete_database(db_name):
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
                return "Deleted Databases Successfully"
            else:
                return f"Failed to delete database: '{db_name}', does not exist"

        except Exception as e:
            logging.error("Some error occured in: delete_database function")
            return str(e)


class TestClass(unittest.TestCase):

    def test_get_db(self):
        db_task = TestDatabaseOperations()
        result = db_task.test_get_database()
        self.assertEquals(result, "databases exists")

    def test_db_create(self):
        db_task = TestDatabaseOperations()
        result = db_task.test_create_database("test_database")
        self.assertEquals(result, "Database Created")

    def test_delete_db(self):
        db_task = TestDatabaseOperations()
        result = db_task.test_delete_database("test_database")
        self.assertEquals(result, "Deleted Databases Successfully")


if __name__ == '__main__':
    unittest.main()
