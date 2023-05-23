from mysql.connector import connect, Error
import mysql.connector


def database_connection():
    connection = mysql.connector.connect(host="localhost",
                                         user="sanskriti",
                                         password="knoldus",
                                         database="sans")

    cursor = connection.cursor()
    return cursor, connection
