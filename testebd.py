import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


connection = create_server_connection("127.0.0.1", "root", "")
cursor = connection.cursor()

# Criar um banco de dados
query = """
    CREATE DATABASE BancoDeDadosPython
"""
cursor.execute(query)

connection.close()
