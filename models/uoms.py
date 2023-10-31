#!/usr/bin/python3
"""
This module provides functions to manage Units of Measurement (UOM).
"""


def get_uoms(connection):
    """
    Retrieve all Units of Measurement (UOM) from the database.

    Args:
        connection: A database connection.

    Returns:
        A list of dictionaries containing UOM information.
    """
    cursor = connection.cursor()
    query = "SELECT * FROM uom"
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # Example usage:
    # print(get_uoms(connection))
