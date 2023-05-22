import logging
import unittest
import pytest
import mysql.connector

connection = mysql.connector.connect(user='amanknoldus',
                                     password='amanknoldus',
                                     host='localhost',
                                     database='test_data')

cursor = connection.cursor()

view_table = "show tables"
no_table = "no such table exists!"
table_name = "test_table"

test_data = {
    "age": 12,
    "email": "test@testemail.com",
    "emp_id": 1234,
    "name": "test user",
    "phone": 1234567890}


@pytest.fixture()
def test_set():
    test_values = {
        "age": 12,
        "email": "test@testemail.com",
        "emp_id": 1234,
        "name": "Test Data",
        "phone": 1234567890}
    return test_values


@pytest.fixture
def emp_id():
    value = 1234
    return value


class TestCrudOperations:

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
            logging.debug("Task: fetching all table from db in (get_tables_data) executed")

            if table_name in tables:
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                table_data = cursor.fetchall()
                logging.info("Task: selecting data from table in (get_tables_data) executed")

                if len(table_data) != 0:
                    for items in table_data:
                        table_items.append({'name': items[0], 'age': items[1], 'phone': items[2],
                                            'email': items[3], 'emp_id': items[4]})
                    logging.info("Task: returning data from table executed")
                    return table_items
                else:
                    msg = "table is empty!"
                    logging.info("Task: empty table in (get_tables_data) executed")
                    return msg
            else:
                msg = f"no such table name: {table_name} exists!"
                logging.info("Task: no table found in (get_tables_data executed")
                return msg

        except Exception as e:
            logging.error("Some error occured in (get_tables_data) function")
            return str(e)

    @staticmethod
    def test_get_individual_entries(emp_id):
        """
        Function to get individual entry present in table.
        @param: table name
        @param: employee id
        @return: individual tabular data
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]
            logging.info("Task: fetching all tables from db in (get_individual_entries) executed")

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()
                logging.info("Task: fetching emp data based on id in (get_individual_entries) executed")

                if count[0] == 0:
                    msg = f"Emp ID: {emp_id} does not exist in the table"
                    logging.info("Task: emp id not found in (get_individual_entries) executed")
                    return msg

                else:
                    query = f'SELECT * FROM {table_name} WHERE emp_id = {emp_id}'
                    cursor.execute(query)
                    individual_data = cursor.fetchall()
                    logging.info("Task: fetching individual entry from table executed")
                    return individual_data

            else:
                logging.info("Task: no table found in (get_individual_entries) executed")
                return no_table

        except Exception as e:
            logging.error("Some error occured in (get_individual_entries) function")
            return str(e)

    @staticmethod
    def test_delete_individual_entries(emp_id):
        """
        Function to delete individual entries from table
        @param emp_id: employee id
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]
            logging.info("Task: fetch all tables from db in (delete_individual_entries) executed")

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()
                logging.info("Task: selecting count from table based on id in (delete_individual_entries) executed")

                if count[0] == 0:
                    msg = f"Emp ID: {emp_id} does not exist in the table"
                    logging.info("Task: emp id not exists in (delete_individual_entries) executed")
                    return msg

                else:
                    query = f'DELETE FROM {table_name} WHERE emp_id = {emp_id}'
                    cursor.execute(query)
                    connection.commit()
                    msg = f'deleted entry of user id:{emp_id} successfully'
                    logging.info(
                        "Task: committing connection after deleted single entry in (delete_individual_entries) executed")
                    return msg
            else:
                logging.info("Task: no table found in (delete_individual_entries) executed")
                return no_table

        except Exception as e:
            logging.error("Some error occured in (delete_individual_entries) function")
            return str(e)

    @staticmethod
    def test_delete_all_entries():
        try:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            table_data = cursor.fetchall()
            logging.info("Task: selecting data from table in (get_tables_data) executed")

            if len(table_data) != 0:
                delete_query = f"DELETE FROM {table_name}"
                cursor.execute(delete_query)
                connection.commit()
                logging.error("Task: committing connection after deleted all entries in (delete_all_entries) executed")
                msg = "deleted all entries from table"
                return msg
            else:
                msg = "table is already empty!"
                logging.info("Task: empty table in (get_tables_data) executed")
                return msg

        except Exception as e:
            logging.info("Task: delete all entries from table in (delete_all_entries) executed")
            return str(e)

    @staticmethod
    def test_update_table_entries(emp_id, test_set):
        """
        Function to update entries in table
        @param emp_id: employee id
        @param test_set: new data entries
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]
            logging.info("Task: fetch all tables from db in (update_table_entries) executed")
            update_values = {
                'name': test_set['name'],
                'age': test_set['age'],
                'phone': test_set['phone'],
                'email': test_set['email'],
                'emp_id': test_set['emp_id']
            }

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {emp_id}"
                cursor.execute(query)
                existing_entry = cursor.fetchone()
                logging.info("Task: select from table based on id in (update_table_entries) executed")

                if existing_entry is None:
                    msg = f"Emp ID: {emp_id} does not exist in the table"
                    status = 404
                    logging.info("Task: employee id not found in (update_table_entries) executed")
                    return msg, status
                else:
                    update_query = f"UPDATE {table_name} SET name = %(name)s, age = %(age)s, phone = %(phone)s, email = %(email)s, emp_id = %(emp_id)s WHERE emp_id = {emp_id}"
                    cursor.execute(update_query, update_values)
                    connection.commit()
                    logging.info("Task: committing connection after update of entry in (update_table_entries) executed")
                    msg = f"updated entries of id: {emp_id} successfully"
                    status = 202
                    return msg

            else:
                msg = "no table exists in database"
                status = 404
                logging.info("Task: no table existing check in (update_table_entries) executed")
                return msg, status

        except Exception as e:
            logging.error("Some error occured in (update_table_entries) function")
            return str(e)

    @staticmethod
    def test_update_table(test_set):
        """
        Function to insert data entries into a table.
        @item: data entries
        @return: data inserted response message
        """

        user_name = test_set['name']
        user_age = test_set['age']
        user_phone = test_set['phone']
        user_email = test_set['email']
        user_emp_id = test_set['emp_id']

        try:
            query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {user_emp_id}"
            cursor.execute(query)
            response = cursor.fetchone()
            count = response[0]
            logging.info("Task: getting count from table based on id in {update_table} executed")

            if count > 0:
                msg = f"entry of id: {user_emp_id} already exists in table!"
                logging.info("Task: entry already exists in table in {update_table} executed")
                return msg
            else:
                insert_data_query = f"INSERT INTO {table_name} (name, age, phone, email, emp_id) VALUES (%s, %s, %s, %s, %s)"
                user_data = [(user_name, user_age, user_phone, user_email, user_emp_id)]

                for data in user_data:
                    cursor.execute(insert_data_query, data)

                connection.commit()
                logging.info("Task: committing connection in (update_table) executed")
                msg = f"Data Successfully Inserted Into Table: {table_name}"
                return msg

        except Exception as e:
            logging.error("Some error occured in (update_table) function")
            return str(e)


class TestClass(unittest.TestCase):

    def test_for_empty_table(self):
        test = TestCrudOperations()
        result = test.test_get_tables_data()
        self.assertEquals(result, "table is empty!")

    def test_for_individual_entry(self):
        emp_id = 1821
        test = TestCrudOperations()
        result = test.test_get_individual_entries(emp_id)
        self.assertEquals(result, f"Emp ID: {emp_id} does not exist in the table")

    def test_for_delete_individual_entry(self):
        emp_id = 1821
        test = TestCrudOperations()
        result = test.test_delete_individual_entries(emp_id)
        self.assertEquals(result, f"Emp ID: {emp_id} does not exist in the table")

    def test_for_delete_individual_entry_two(self):

        emp_id = 1234
        test = TestCrudOperations()
        test.test_update_table(test_data)
        result = test.test_delete_individual_entries(emp_id)
        self.assertEquals(result, f'deleted entry of user id:{emp_id} successfully')

    def test_for_delete_entry(self):
        test = TestCrudOperations()
        result = test.test_delete_all_entries()
        self.assertEquals(result, "deleted all entries from table")

    def test_for_update_entry(self):
        emp_id = 1851
        test = TestCrudOperations()
        result = test.test_update_table_entries(emp_id, test_data)
        self.assertEquals(result, f"updated entries of id: {emp_id} successfully")

    def test_for_update_table(self):
        test = TestCrudOperations()
        test.test_delete_all_entries()
        result = test.test_update_table(test_data)
        self.assertEquals(result, f"Data Successfully Inserted Into Table: {table_name}")

    def test_for_update_table_two(self):
        user_emp_id = 1234
        test = TestCrudOperations()
        result = test.test_update_table(test_data)
        self.assertEquals(result, f"entry of id: {user_emp_id} already exists in table!")


if __name__ == '__main__':
    unittest.main()
