import logging
import unittest
import pytest
from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_table = "show tables"
no_table = "no such table exists!"
table_name = "demo"


@pytest.fixture
def input_value():
    value = 1234
    return value


class TestCrudOperations:

    @staticmethod
    def test_update_table():
        """
        Function to insert data entries into a table.
        @item: data entries
        @return: data inserted response message
        """

        user_name = 'test_name'
        user_age = 25
        user_phone = 9044142219
        user_email = 'test@email.com'
        user_emp_code = 1234

        try:
            insert_data_query = f"INSERT INTO {table_name} (name, age, phone, email, emp_code) VALUES (%s, %s, %s, %s, %s)"
            user_data = [(user_name, user_age, user_phone, user_email, user_emp_code)]

            for data in user_data:
                cursor.execute(insert_data_query, data)

            connection.commit()
            return f"Data Successfully Inserted Into Table: {table_name}"

        except Exception as e:
            logging.error("Some error occured in: update_table function")
            return str(e)

    @staticmethod
    def test_get_tables_data():
        """
        Function to get all entries from the given table.
        @return: entries in the table
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]
            table_items = []

            if table_name in tables:
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                table_data = cursor.fetchall()

                if len(table_data) != 0:
                    for items in table_data:
                        table_items.append({'name': items[0], 'age': items[1], 'phone': items[2],
                                            'email': items[3], 'emp_code': items[4]})
                    return "Table Items"
                else:
                    return "table is empty!"
            else:
                return f"no such table name: {table_name} exists!"

        except Exception as e:
            logging.error("Some error occured in: get_tables_data function")
            return str(e)

    @staticmethod
    def test_get_individual_entries(input_value):
        """
        Function to get individual entry present in table.
        @param: table name
        @param: employee id
        @return: individual tabular data
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {input_value}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {input_value} does not exist in the table"

                else:
                    query = f'SELECT * FROM {table_name} WHERE emp_code = {input_value}'
                    cursor.execute(query)
                    return "Returned Individual Data Successfully"

            else:
                return no_table

        except Exception as e:
            logging.error("Some error occured in: get_table_entries function")
            return str(e)

    @staticmethod
    def test_delete_individual_entries(input_value):
        """
        Function to delete individual entries from table
        @param input_value: employee id from pytest fixtures
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {input_value}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {input_value} does not exist in the table"

                else:
                    query = f'DELETE FROM {table_name} WHERE emp_code = {input_value}'
                    cursor.execute(query)
                    connection.commit()

                    return f'deleted entry of user id:{input_value} successfully'
            else:
                return no_table

        except Exception as e:
            logging.error("Some error occured in: delete_individual_entries function")
            return str(e)

    @staticmethod
    def test_delete_all_entries():
        try:
            delete_query = f"DELETE FROM {table_name}"
            cursor.execute(delete_query)
            connection.commit()
            return "deleted all entries from table"

        except Exception as e:
            return str(e)

    @staticmethod
    def test_update_table_entries(input_value):
        """
        Function to update entries in table
        @param input_id: employee id from pytest fixtures
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]

            update_values = {
                'name': 'test_name',
                'age': 11,
                'phone': 1234567890,
                'email': 'test@test.com',
                'emp_code': 1234

            }

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {input_value}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {input_value} does not exist in the table"
                else:
                    update_query = f"UPDATE {table_name} SET name = %(name)s, age = %(age)s, phone = %(phone)s, email = %(email)s, emp_code = %(emp_code)s WHERE emp_code = {input_value}"
                    cursor.execute(update_query, update_values)
                    connection.commit()
                    return f"Updated Entry of id: {input_value}"
            else:
                return "no table exists in database"

        except Exception as e:
            logging.error("Some error occured in: update_table_entries function")
            return str(e)


class TestClass(unittest.TestCase):

    def test_for_update_table(self):
        test_tables_data = TestCrudOperations()
        result = test_tables_data.test_update_table()
        self.assertEquals(result, test_tables_data.test_update_table())

    def test_get_table_data(self):
        test_tables_data = TestCrudOperations()
        result = test_tables_data.test_get_tables_data()
        self.assertEquals(result, test_tables_data.test_get_tables_data())

    def test_for_individual_entries(self):
        test_tables_data = TestCrudOperations()
        test_tables_data.test_update_table()
        result = test_tables_data.test_get_individual_entries(1234)
        self.assertEquals(result, test_tables_data.test_get_individual_entries(1234))

    def test_for_update_entry(self):
        test_tables_data = TestCrudOperations()
        test_tables_data.test_update_table()
        result = test_tables_data.test_update_table_entries(1234)
        self.assertEquals(result, test_tables_data.test_update_table_entries(1234))

    def test_for_delete_individual_entries(self):
        test_tables_data = TestCrudOperations()
        result = test_tables_data.test_delete_individual_entries(1234)
        self.assertEquals(result, test_tables_data.test_delete_individual_entries(1234))

    def test_for_delete_all_entries(self):
        test_tables_data = TestCrudOperations()
        test_tables_data.test_update_table()
        result = test_tables_data.test_delete_all_entries()
        self.assertEquals(result, test_tables_data.test_delete_all_entries())


if __name__ == '__main__':
    unittest.main()
