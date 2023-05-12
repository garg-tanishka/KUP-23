import unittest
from src.utils.db.db_connection import db_connection
from test_suite.unit.test_crud_operations import TestCrudOperations

db_exist = "Database Exists"
table_data = "Table in aman_knoldus are: [('aman',), ('knoldus',), ('practice',)]"
cursor, connection = db_connection()


class TestClass(unittest.TestCase):

    def test_db_one(self):
        test_db_operation = TestCrudOperations("databases")
        result = test_db_operation.test_get_database()
        self.assertEquals(result, db_exist)

    def test_db_two(self):
        test_db_operation = TestCrudOperations("how many databases")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_three(self):
        test_db_operation = TestCrudOperations("show databases")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_four(self):
        test_db_operation = TestCrudOperations("all databases")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_five(self):
        test_db_operation = TestCrudOperations("^#$%325")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_fifth(self):
        test_db_operation = TestCrudOperations(54844)
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_six(self):
        test_db_operation = TestCrudOperations(54.84)
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, db_exist)

    def test_db_seven(self):
        test_db_operation = TestCrudOperations("show aman_knoldus")
        result = test_db_operation.test_get_database()
        self.assertEquals(result, table_data)

    def test_db_eight(self):
        cursor.execute("show tables")
        tables = [row[0] for row in cursor.fetchall()]
        table_items = []
        response = ""
        table_name = "aman_knoldus"
        if table_name == "tables":
            return tables

        elif table_name.split()[0] == "view" and table_name.split()[-1] in tables:
            query = "SELECT * FROM aman_knoldus"
            cursor.execute(query)
            table_data = cursor.fetchall()

            if len(table_data) != 0:
                for items in table_data:
                    table_items.append({'name': items[0], 'age': items[1], 'phone': items[2],
                                        'email': items[3], 'emp_code': items[4]})
                response = table_items
            else:
                response = "table is empty!"

        test_db_operation = TestCrudOperations("view aman_knoldus")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, response)

    def test_db_nine(self):
        test_db_operation = TestCrudOperations("delete aman_knoldus")
        result = test_db_operation.test_get_database()
        self.assertNotEquals(result, "Deleted database: aman_knoldus")

    def test_create__exist_db(self):
        test_db_operation = TestCrudOperations("aman_knoldus")
        result = test_db_operation.test_create_database()
        self.assertEquals(result, "Database: 'aman_knoldus' already exists.")

    def test_create_new_db(self):
        test_db_operation = TestCrudOperations("status")
        result = test_db_operation.test_create_database()
        self.assertEquals(result, "Database created")

    def test_delete_db(self):
        test_db_operation = TestCrudOperations("status")
        result = test_db_operation.test_delete_database()
        self.assertEquals(result, "Deleted database: 'status'")

    def test_delete_two(self):
        test_db_operation = TestCrudOperations("status")
        result = test_db_operation.test_delete_database()
        self.assertEquals(result, "Failed to delete database: 'status', does not exist")

    # def test_get_table(self):
    #     cursor.execute("show tables")
    #     tables = [row[0] for row in cursor.fetchall()]
    #
    #     test_db_operation = TestCrudOperations("tables")
    #     result = test_db_operation.test_get_table_data()
    #     self.assertEquals(result, tables)

    def test_show_table(self):
        table_items = []
        query = "SELECT * FROM knoldus"
        cursor.execute(query)
        table_datas = cursor.fetchall()

        for items in table_datas:
            table_items.append({'name': items[0], 'age': items[1], 'phone': items[2],
                                'email': items[3], 'emp_code': items[4]})

        test_db_operation = TestCrudOperations("view knoldus")
        result = test_db_operation.test_get_table_data()
        self.assertEquals(result, table_items)

    def test_show_individual_table(self):

        query = "SHOW COLUMNS FROM knoldus WHERE Field = 'emp_code'"
        cursor.execute(query)

        if cursor.fetchone() is not None:
            query = 'SELECT * FROM knoldus WHERE emp_code = 1851'
            cursor.execute(query)
            individual_data = cursor.fetchall()
            response = individual_data
        else:
            response = "no columns name: knoldus exists in the table!"

        test_db_operation = TestCrudOperations("view knoldus emp_code 1851")
        result = test_db_operation.test_get_table_data()
        self.assertEquals(result, response)

    def test_show_individual_table_two(self):

        query = "SHOW COLUMNS FROM knoldus WHERE Field = 'emp_code'"
        cursor.execute(query)

        if cursor.fetchone() is not None:
            query = 'SELECT * FROM knoldus WHERE emp_code = 1401'
            cursor.execute(query)
            individual_data = cursor.fetchall()
            response = individual_data
        else:
            response = "no columns name: knoldus exists in the table!"

        test_db_operation = TestCrudOperations("view knoldus emp_code 1401")
        result = test_db_operation.test_get_table_data()
        self.assertEquals(result, response)



if __name__ == '__main__':
    unittest.main()
