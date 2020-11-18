from models import purchase as repo
from models import user

from flask import request, make_response, jsonify
import json

def create_purchase(client_id):
    data = request.get_json()
    p = repo.Purchase()
    p.client_id = client_id
    p.products = data["products"]
    p.create_order()

    return make_response("Created"),200

def get_purchases(client_id):
    u = user.User()
    u.get(client_id)
    p = repo.Purchase()
    p.client_id = client_id
    data = p.get_purchases() if u.u_type == "Client" else p.all()
    arr = []
    for record in data:
        arr.append(repo.client_order_to_json(record))
    result = {"data":arr}
    return make_response(jsonify(result)),200

def get_products_from_order(clientOrder):
    p = repo.Purchase()
    p.clientOrder = clientOrder
    data = p.get_order()
    arr = []
    result = {}
    for record in data:
        arr.append(repo.client_detail_to_json(record))
        result["status"]=record["status"]
        result["date"]=record["date"]
        result["total"]= str(record["total"])
    result["data"] =arr
    return make_response(jsonify(result)),200

def update_status (clientOrder,value):
    p = repo.Purchase()
    p.clientOrder = clientOrder
    p.update_status(value)
    return make_response("Modified"),200
