#!/usr/bin/python3
"""
This module defines functions for managing orders.
"""

from datetime import datetime
from DB_connections import get_sql_connection


def insert_order(connection, order):
    """
    Create a new order in the database.

    Args:
        connection: A database connection.
        order: A dictionary containing order information.

    Returns:
        The ID of the newly created order.
    """
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    try:
        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid

        order_details_query = (
            "INSERT INTO order_details "
            "(order_id, product_id, quantity, total_price)"
            "VALUES (%s, %s, %s, %s)"
        )

        order_details_data = []
        for order_detail_record in order['order_details']:
            order_details_data.append([
                order_id,
                int(order_detail_record['product_id']),
                float(order_detail_record['quantity']),
                float(order_detail_record['total_price'])
            ])
        cursor.executemany(order_details_query, order_details_data)

        connection.commit()

        return order_id
    except Exception as e:
        # Handle the exception, e.g., log the error or return an error response
        return None


def get_order_details(connection, order_id):
    """
    Retrieve order details for a specific order.

    Args:
        connection: A database connection.
        order_id: The ID of the order to retrieve details for.

    Returns:
        A list of dictionaries containing order details.
    """
    cursor = connection.cursor()

    query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, " \
            "products.name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.product_id where order_details.order_id = %s"

    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records


def get_all_orders(connection):
    """
    Retrieve information about all orders in the database.

    Args:
        connection: A database connection.

    Returns:
        A list of dictionaries containing order information.
    """
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # Append order details in each order
    for record in response:
        record['order_details'] = retrieve_order_details(connection, record['order_id'])

    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # Example usage:
    # print(retrieve_order_details(connection, 4))
    # print(create_order(connection, {
    #     'customer_name': 'haspharma',
    #     'grand_total': '235',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 60
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 115
    #         }
    #     ]
    # }))
