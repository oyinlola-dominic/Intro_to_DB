#!/usr/bin/python3
"""
A script that creates the database 'alx_book_store' in MySQL.
If the database already exists, the script should not fail.
"""

import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_mysql_password'  # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except NameError:
        pass
