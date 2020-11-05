from ..controllers import product_controller, user_controller
from ..authentication import auth as Auth
from flask import Flask, request
from flask_httpauth import HTTPTokenAuth
from flask_negotiate import consumes, produces
from flask_cors import CORS


app = Flask(__name__)
auth = HTTPTokenAuth()
CORS(app)

@app.route('/status')
def ping_status():
    return "OK"

@auth.verify_token
def verify_token(token):
    return Auth.verify_token(token)

@app.route("/auth", methods=['POST'])
def authorize():
    return Auth.generate_token()

@app.route('/user', methods=['POST'])
@auth.login_required
def create_user():
    response = user_controller.create_user()
    return response

@app.route('/product', methods=['GET'])
#@produces('application/json')
def show_products():
    response = product_controller.list_products()
    return response

@app.route('/product/<product_id>', methods=['GET'])
#@produces('application/json')
def show_product(product_id):
    response = product_controller.list_product(product_id)
    return response

@app.route('/product/<product_id>', methods=['DELETE'])
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
