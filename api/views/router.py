from ..controllers import legacy_controller
from ..auth import authentification
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth

from flask_negotiate import consumes, produces

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/status')
def ping_status():
    return "OK"

@auth.verify_password
@limiter.exempt
def authenticate(username, password):
    return authentification.verify_password(username)

@app.route('/product', methods=['GET'])
@auth.login_required
@produces('application/json')
def show_products():
    #TODO
    return response

@app.route('/product/<int:product_id>', methods=['GET'])
@auth.login_required
@produces('application/json')
def show_product(product_id):
    #TODO
    return response

@app.route('/product/<int:product_id>', methods=['DELETE'])
@auth.login_required
@produces('application/json')
def delete_product(product_id):
    #TODO
    return response

@app.route('/product', methods=['POST'])
@auth.login_required
@produces('application/json')
def create_product():
    #TODO
    return response

@app.route('/product/<int:product_id>', methods=['PUT'])
@auth.login_required
@produces('application/json')
def edit_product(product_id):
    #TODO
    return response
