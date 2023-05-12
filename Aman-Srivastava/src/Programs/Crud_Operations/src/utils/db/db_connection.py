import mysql.connector


def db_connection():
    connection = mysql.connector.connect(user='amanknoldus',
                                         password='amanknoldus',
                                         host='localhost',
                                         database='aman_knoldus')

    cursor = connection.cursor()
    return cursor, connection
