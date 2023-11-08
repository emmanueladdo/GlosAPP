#!/usr/bin/python3
"""
This module provides database connection handling.
"""

import os
from mysql.connector import connect
__connection = None


def get_sql_connection():
    """
    Get a MySQL database connection.
    Returns:
        MySQL database connection.
    """
    global __connection
    if __connection is None:
        try:
            user = os.environ.get("DB_USER")
            password = os.environ.get("DB_PASSWORD")
            host = os.environ.get("DB_HOST")
            database = os.environ.get("DB_DATABASE")
            port = os.environ.get("DB_PORT")

            if not (user and password and host and database and port):
                raise ValueError(
                    "Database configuration missing in environment variables"
                )
            __connection = connect(
                user=user,
                password=password,
                host=host,
                database=database,
                port=port
            )
            return __connection
        except Exception as e:
            # Handle and log the exception, e.g., print the error message
            print(f"Error connecting to the database: {e}")
    return __connection
    """
    __connection = connect(
        user="root",
        password="1@werty.coM",
        host="127.0.0.1",
        database="glosapp",
        port="3305"
    )
    return __connection
    """
