import mysql.connector
from mysql.connector import connect
from mysql.connector import Error
import pandas as pd

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", "usbw")
connection = mysql_connection("localhost", "root", "usbw", "teste")

query = '''
    INSERT INTO clientes VALUES
        (1001, 'Joãozinho Silva', '7199999-9999', 'joao@email.com', 'Salvador'),
        (1002, 'Paula Silva', '2199999-9999', 'paula@email.com', 'Rio'),
        (1003, 'Patricia Silva', '1199999-9999', 'paty@email.com', 'Sampa'),
        (1004, 'Zé Silva', '4199999-9999', 'ze@email.com', 'Curitiba'),
        (1005, 'Richarlison Pombo', '3199999-9999', 'pombo@email.com', 'Nova Venécia'),
        (1006, 'Vini Junior', '2199999-9999', 'vini@email.com', 'Rio'),
        (1007, 'Neymar Junior', '1199999-9999', 'ney@email.com', 'Santos')
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()