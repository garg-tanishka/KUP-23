import logging
from src.utils.db.db_connection import db_connection

cursor, connection = db_connection()
view_table = "show tables"
no_table = "no such table exists!"
table_name = "knoldus"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
                    status = 200
                    return table_items, status
                else:
                    msg = "table is empty!"
                    status = 404
                    logging.info("Task: empty table in (get_tables_data) executed")
                    return msg, status
            else:
                msg = f"no such table name: {table_name} exists!"
                status = 404
                logging.info("Task: no table found in (get_tables_data executed")
                return msg, status

        except Exception as e:
            logging.error("Some error occured in (get_tables_data) function")
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
            logging.info("Task: fetching all tables from db in (get_individual_entries) executed")

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()
                logging.info("Task: fetching emp data based on id in (get_individual_entries) executed")

                if count[0] == 0:
                    msg = f"Emp ID: {emp_id} does not exist in the table"
                    error = 404
                    logging.info("Task: emp id not found in (get_individual_entries) executed")
                    return msg, error

                else:
                    query = f'SELECT * FROM {table_name} WHERE emp_id = {emp_id}'
                    cursor.execute(query)
                    individual_data = cursor.fetchall()
                    status = 200
                    logging.info("Task: fetching individual entry from table executed")
                    return individual_data, status

            else:
                logging.info("Task: no table found in (get_individual_entries) executed")
                error = 404
                return no_table, error

        except Exception as e:
            logging.error("Some error occured in (get_individual_entries) function")
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
            logging.info("Task: fetch all tables from db in (delete_individual_entries) executed")

            if table_name in tables:
                query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {emp_id}"
                cursor.execute(query)
                count = cursor.fetchone()
                logging.info("Task: selecting count from table based on id in (delete_individual_entries) executed")

                if count[0] == 0:
                    msg = f"Emp ID: {emp_id} does not exist in the table"
                    status = 404
                    logging.info("Task: emp id not exists in (delete_individual_entries) executed")
                    return msg, status

                else:
                    query = f'DELETE FROM {table_name} WHERE emp_id = {emp_id}'
                    cursor.execute(query)
                    connection.commit()
                    msg = f'deleted entry of user id:{emp_id} successfully'
                    status = 200
                    logging.info(
                        "Task: committing connection after deleted single entry in (delete_individual_entries) executed")
                    return msg, status
            else:
                status = 404
                logging.info("Task: no table found in (delete_individual_entries) executed")
                return no_table, status

        except Exception as e:
            logging.error("Some error occured in (delete_individual_entries) function")
            return str(e)

    @staticmethod
    def delete_all_entries():
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
                status = 200
                return msg, status
            else:
                msg = "table is already empty!"
                logging.info("Task: empty table in (get_tables_data) executed")
                return msg

        except Exception as e:
            logging.info("Task: delete all entries from table in (delete_all_entries) executed")
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
            logging.info("Task: fetch all tables from db in (update_table_entries) executed")

            update_values = {
                'name': item['name'],
                'age': item['age'],
                'phone': item['phone'],
                'email': item['email'],
                'emp_id': item['emp_id']
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
                    return msg, status

            else:
                msg = "no table exists in database"
                status = 404
                logging.info("Task: no table existing check in (update_table_entries) executed")
                return msg, status

        except Exception as e:
            logging.error("Some error occured in (update_table_entries) function")
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
        user_emp_id = item['emp_id']

        try:
            query = f"SELECT COUNT(*) FROM {table_name} WHERE emp_id = {user_emp_id}"
            cursor.execute(query)
            response = cursor.fetchone()
            count = response[0]
            logging.info("Task: getting count from table based on id in {update_table} executed")

            if count > 0:
                msg = f"entry of id: {user_emp_id} already exists in table!"
                status = 409
                logging.info("Task: entry already exists in table in {update_table} executed")
                return msg, status
            else:
                insert_data_query = f"INSERT INTO {table_name} (name, age, phone, email, emp_id) VALUES (%s, %s, %s, %s, %s)"
                user_data = [(user_name, user_age, user_phone, user_email, user_emp_id)]

                for data in user_data:
                    cursor.execute(insert_data_query, data)

                connection.commit()
                connection.close()
                logging.info("Task: committing connection in (update_table) executed")
                msg = f"Data Successfully Inserted Into Table: {table_name}"
                status = 200
                return msg, status

        except Exception as e:
            logging.error("Some error occured in (update_table) function")
            return str(e)
