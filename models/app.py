#!/usr/bin/python3
from flask import Flask, request, jsonify
from DB_connections import get_sql_connection
import json
import products
import orders
import uoms

app = Flask(__name__)

connection = get_sql_connection()


@app.route('/getUOM', methods=['GET'])
def get_uom():
    """
    Get all Units of Measurement (UOM) from the database.

    Returns:
        JSON response with UOM data.
    """
    response = uoms.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProducts', methods=['GET'])
def get_products():
    """
    Get all products from the database.

    Returns:
        JSON response with product data.
    """
    response = products.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    """
    Insert a new product into the database.

    Returns:
        JSON response with the product ID.
    """
    request_payload = json.loads(request.form['data'])
    product_id = products.add_new_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    """
    Get all orders from the database.

    Returns:
        JSON response with order data.
    """
    response = orders.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    """
    Insert a new order into the database.

    Returns:
        JSON response with the order ID.
    """
    request_payload = json.loads(request.form['data'])
    order_id = orders.create_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    """
    Delete a product from the database.

    Returns:
        JSON response with the product ID.
    """
    return_id = products.remove_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting GlosAPP")
    app.run(port=5000)
