#!/usr/bin/python3
"""
This module defines the function to manage product
"""
from DB_connections import get_sql_connection


def get_all_products(connection):
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
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()
    return response


def insert_new_product(connection, product):
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
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (
        product['product_name'],
        product['uom_id'],
        product['price_per_unit']
    )

    try:
        cursor.execute(query, data)
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        # Handle the exception, e.g., log the error or return None
        return None


def delete_product(connection, product_id):
    """
    Remove a product from the database.

    Args:
        connection: A database connection.
        product_id: The ID of the product to be removed.

    Returns:
        The ID of the removed product.
    """
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    data = (product_id, )

    try:
        cursor.execute(query)
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        # Handle the exception, e.g., log the error or return None
        return None


if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage
    # print(get_all_products(connection))
    print(add_new_product(connection, {
        'product_name': 'Fanyogo Strawbery 145ml',
        'uom_id': '1',
        'price_per_unit': 3
    }))
    # if product_id is not None:
    #    print(f"Product added with ID: {product_id}")
    # else:
    #    print("Failed to add a product.")
