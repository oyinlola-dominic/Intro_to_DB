# MySQLServer.py
# Script to create 'alx_book_store' database in MySQL

import mysql.connector
from mysql.connector import Error
import getpass

def create_database(host, user, password, port=3306):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

        if not conn.is_connected():
            print("Failed to connect to the MySQL server.")
            return

        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()

        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    print("Enter MySQL connection details (press Enter for defaults):")
    host = input("Host [localhost]: ") or "localhost"
    user = input("User [root]: ") or "root"
    password = getpass.getpass("Password: ")
    port_input = input("Port [3306]: ") or "3306"

    try:
        port = int(port_input)
    except ValueError:
        print("Invalid port, using 3306.")
        port = 3306

    create_database(host, user, password, port)
