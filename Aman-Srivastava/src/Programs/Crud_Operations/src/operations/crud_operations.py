import logging
from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_table = "show tables"
no_table = "no such table exists!"
table_name = "demo"


class CrudOperations:

    @staticmethod
    def get_tables_data():
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
                    return table_items
                else:
                    return "table is empty!"
            else:
                return f"no such table name: {table_name} exists!"

        except Exception as e:
            logging.error("Some error occured in: get_tables_data function")
            return str(e)

    @staticmethod
    def get_individual_entries(emp_id):
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
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {emp_id} does not exist in the table"

                else:
                    query = f'SELECT * FROM {table_name} WHERE emp_code = {emp_id}'
                    cursor.execute(query)
                    individual_data = cursor.fetchall()
                    return individual_data

            else:
                return no_table

        except Exception as e:
            logging.error("Some error occured in: get_table_entries function")
            return str(e)

    @staticmethod
    def delete_individual_entries(emp_id):
        """
        Function to delete individual entries from table
        @param emp_id: employee id
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {emp_id} does not exist in the table"

                else:
                    query = f'DELETE FROM {table_name} WHERE emp_code = {emp_id}'
                    cursor.execute(query)
                    connection.commit()

                    return f'deleted entry of user id:{emp_id} successfully'
            else:
                return no_table

        except Exception as e:
            logging.error("Some error occured in: delete_individual_entries function")
            return str(e)

    @staticmethod
    def delete_all_entries():
        try:
            delete_query = f"DELETE FROM {table_name}"
            cursor.execute(delete_query)
            connection.commit()
            return "deleted all entries from table"

        except Exception as e:
            return str(e)

    @staticmethod
    def update_table_entries(emp_id, item):
        """
        Function to update entries in table
        @param emp_id: employee id
        @param item: new data entries
        @return: response message
        """
        try:
            cursor.execute(view_table)
            tables = [row[0] for row in cursor.fetchall()]

            update_values = {
                'name': item['name'],
                'age': item['age'],
                'phone': item['phone'],
                'email': item['email'],
                'emp_code': item['emp_code'],

            }

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_code = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()

                if count[0] == 0:
                    return f"Emp ID: {emp_id} does not exist in the table"
                else:
                    update_query = f"UPDATE {table_name} SET name = %(name)s, age = %(age)s, phone = %(phone)s, email = %(email)s, emp_code = %(emp_code)s WHERE emp_code = {emp_id}"
                    cursor.execute(update_query, update_values)
                    connection.commit()
                    return f"updated entries of id: {emp_id} successfully"
            else:
                return "no table exists in database"

        except Exception as e:
            logging.error("Some error occured in: update_table_entries function")
            return str(e)

    @staticmethod
    def update_table(item):
        """
        Function to insert data entries into a table.
        @item: data entries
        @return: data inserted response message
        """

        user_name = item['name']
        user_age = item['age']
        user_phone = item['phone']
        user_email = item['email']
        user_emp_code = item['emp_code']

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
