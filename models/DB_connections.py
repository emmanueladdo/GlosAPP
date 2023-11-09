#!/usr/bin/python3
"""
This module provides database connection handling.
"""

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
        __connection = connect(
            user="gstore",
            password="password",
            host="127.0.0.1",
            database="glosapp",
            port="3306"
        )
        return __connection
