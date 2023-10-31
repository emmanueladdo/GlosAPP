#!/usr/bin/python3
"""
This give connections to the DB
"""


from mysql.connector import connect
__connection = None


def get_sql_conn():
    global __connection
    if __connection is None:
        __connection = connect(user="root", password="root", host="127.0.0.1", database="glosapp")
        return __connection
