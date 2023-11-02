#!/usr/bin/python3
"""
This module defines the function to manage product
"""
from DB_connections import get_sql_connection


def get_all_products_info(connection):
    """
    Retrieve information about all products in the database.

    Args:
        connection: A database connection.

    Returns:
        A list of dictionaries containing product information.
    """
    cursor = connection.cursor()
    query = (
        "select products.product_id, products.name, "
        "products.uom_id, products.price_per_unit, "
        "uom.uom_name "
        "from products "
        "inner join uom on products.uom_id=uom.uom_id "
    )
    cursor.execute(query)
    response = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response


def add_new_product(connection, product):
    """
    Add a new product to the database.

    Args:
        connection: A database connection.
        product: A dictionary containing product information.

    Returns:
        The ID of the newly added product.
    """
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (
        product['product_name'],
        product['uom_id'],
        product['price_per_unit']
    )
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def remove_product(connection, product_id):
    """
    Remove a product from the database.

    Args:
        connection: A database connection.
        product_id: The ID of the product to be removed.

    Returns:
        The ID of the removed product.
    """
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage
    # print(get_all_products(connection))
    print(add_new_product(connection, {
        'product_name': 'Fanyogo Strawbery 145ml',
        'uom_id': '1',
        'price_per_unit': 3
    }))
