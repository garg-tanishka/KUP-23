from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_db = "show databases"


class TestCrudOperations:
    def __init__(self, data):
        self.user_input = data

    def test_get_database(self):
        """
        Function to perform operation like get all existing database,
        show tables in database.
        @return: list of databases, tables in databases
        """
        user_input = self.user_input

        operation = view_db
        cursor.execute(operation)
        databases = [row[0] for row in cursor.fetchall()]

        try:
            db_name = user_input.split()[-1]
            if user_input == 'databases':
                if databases:
                    return "Database Exists"
                else:
                    return "None Database Exists!"

            elif user_input.split()[0] == "use":
                db_name = user_input.split()[-1]
                cursor.execute(f"use {db_name};")
                cursor.execute("select database()")
                current_db = cursor.fetchone()
                return current_db

            elif user_input.split()[0] == "show" and db_name in databases:
                db_name = user_input.split()[-1]
                query = f"SHOW TABLES FROM {db_name}"
                cursor.execute(query)
                tables = cursor.fetchall()
                if not tables:
                    return f"database: {db_name} is empty"
                else:
                    return f"Table in {db_name} are: {tables}"
            else:
                return f"invalid input or no such database: {db_name} exists! try again"

        except Exception as e:
            return str(e)

    def test_create_database(self):
        """
        Function to create database.
        @return: response message
        """
        user_input = self.user_input
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if user_input in databases:
                return f"Database: '{user_input}' already exists."
            else:
                cursor.execute(f"create database {user_input}")
                connection.commit()
                return "Database created"

        except Exception as e:
            return str(e)

    def test_delete_database(self):
        """
        Function to delete database.
        @return: response message
        """
        user_input = self.user_input
        try:
            cursor.execute(view_db)
            databases = [row[0] for row in cursor.fetchall()]
            if user_input in databases:
                cursor.execute(f"drop database {user_input}")
                connection.commit()
                return f"Deleted database: '{user_input}'"
            else:
                return f"Failed to delete database: '{user_input}', does not exist"

        except Exception as e:
            return str(e)

    def test_get_table_data(self):
        """
        Function to get tables present in database or individual
        data of a table based on its emp_code.
        @return: tables in database, individual tabular data
        """
        table_name = self.user_input

        try:
            cursor.execute("show tables")
            tables = [row[0] for row in cursor.fetchall()]
            table_items = []

            if table_name == "tables":
                return tables

            elif table_name.split()[0] == "view" and table_name.split()[-1] in tables:
                name = table_name.split()[-1]
                query = f"SELECT * FROM {name}"
                cursor.execute(query)
                table_data = cursor.fetchall()

                if len(table_data) != 0:
                    for items in table_data:
                        table_items.append({'name': items[0], 'age': items[1], 'phone': items[2],
                                            'email': items[3], 'emp_code': items[4]})
                    return table_items
                else:
                    return "table is empty!"

            elif len(table_name.split()) == 4:
                col_name = table_name.split()[2]
                table = table_name.split()[1]
                user_id = table_name.split()[-1]

                query = f"SHOW COLUMNS FROM {table} WHERE Field = '{col_name}'"
                cursor.execute(query)

                if cursor.fetchone() is not None:
                    query = f'SELECT * FROM {table} WHERE {col_name} = {user_id}'
                    cursor.execute(query)
                    individual_data = cursor.fetchall()
                    return individual_data
                else:
                    return f"no columns name: {table_name.split()[-2]} exists in the table!"
            else:
                return "invalid input or table does not exists"

        except Exception as e:
            return str(e)

    def test_create_table(self):
        """
        Function to create table in database according to defined schema
        @return: response message
        """
        table_name = self.user_input

        table_schema = f"""CREATE TABLE {table_name} (
                    name VARCHAR(255),
                    age INT NOT NULL,
                    phone VARCHAR(10) NOT NULL,
                    email VARCHAR(255),
                    emp_code INT NOT NULL)"""

        try:
            cursor.execute(table_schema)
            connection.commit()
            return f"Created Table: '{table_name}' "

        except Exception as e:
            return str(e)

    def test_delete_table_data(self):
        """
        Function to delete table from database
        @return: response message
        """
        table_name = self.user_input

        try:
            cursor.execute("show tables")
            tables = [row[0] for row in cursor.fetchall()]

            dlt_table_query = f"drop table {table_name}"

            if table_name in tables:
                cursor.execute(dlt_table_query)
                connection.commit()
                return f"Deleted Table: '{table_name}'"
            else:
                return "No such table exists"

        except Exception as e:
            return str(e)

    def test_insert_data(self):
        """
        Function to insert user data into table based on column names defined input data.
        @return: response message
        """
        table_name = self.user_input['table']

        user_name = self.user_input['name']
        user_age = self.user_input['age']
        user_phone = self.user_input['phone']
        user_email = self.user_input['email']
        user_emp_code = self.user_input['emp_code']

        try:
            insert_data_query = f"INSERT INTO {table_name} (name, age, phone, email, emp_code) VALUES (%s, %s, %s, %s, %s)"
            user_data = [(user_name, user_age, user_phone, user_email, user_emp_code)]

            for data in user_data:
                cursor.execute(insert_data_query, data)
            connection.commit()
            return f"Data Successfully Inserted Into Table: {table_name}"

        except Exception as e:
            return str(e)
