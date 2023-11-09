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
    query = ("SELECT * FROM uom")

    try:
        cursor.execute(query)
        response = []
        for (uom_id, uom_name) in cursor:
            response.append({
                'uom_id': uom_id,
                'uom_name': uom_name
            })
        return response
    except Exception as e:
        # Handle the exception, e.g., log the error or return None
        return None


if __name__ == '__main__':
    from DB_connections import get_sql_connection

    connection = get_sql_connection()
    uoms = get_uoms(connection)
    if uoms is not None:
        print(uoms)
    else:
        print("Failed to retrieve UOM data.")
    # Example usage:
    # print(get_uoms(connection))
