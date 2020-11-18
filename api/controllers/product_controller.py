from models import product as repo
from flask import request, make_response, jsonify

def list_product(ID):
    p = repo.Product()
    p.get(ID)
    response = p.to_json()
    return make_response(jsonify(response)), 200

def list_products():
    p = repo.Product()
    data = p.all()
    arr = []
    for i in data:
        arr.append(repo.to_json(i))
    result = {"data":arr}
    return make_response(jsonify(result)),200
    

