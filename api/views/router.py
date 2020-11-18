from ..controllers import product_controller, user_controller, purchase_controller
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
def create_user():
    response = user_controller.create_user()
    return response

#Obtener informacion de usuario logeado
@app.route('/user/<user_id>', methods=['GET'])
@auth.login_required
def get_user(user_id):
    response = user_controller.get_user(user_id)
    return response

#Ver todos los productos de una orden
@app.route('/purchase/<clientOrder>', methods=['GET'])
@auth.login_required
def get_all_products_from_purchase(clientOrder):
    response = purchase_controller.get_products_from_order(clientOrder)
    return response

#Modificar status o info de una compra realizada
@app.route('/purchase/<clientOrder>/<value>', methods=['PATCH'])
@auth.login_required
def update_purchase_status(clientOrder,value):
    st_val  =  {"1":'En tránsito',"2":'Entregado',"0" :'En proceso'}
    status = st_val[value]
    response = purchase_controller.update_status(clientOrder,status)
    return response

#Obtener todas las purchases
"""
Si es admin regresa todos los purchases pendientes
"""
@app.route('/user/<user_id>/purchase', methods=['GET'])
@auth.login_required
def get_all_purchases(user_id):
    response = purchase_controller.get_purchases(user_id)
    return response

#Crea una orden de compra de un usuario
@app.route('/user/<user_id>/purchase', methods=['POST'])
@auth.login_required
def create_purchase(user_id):
    response = purchase_controller.create_purchase(user_id)
    return response

#Obtiene todos los productos
@app.route('/product', methods=['GET'])
def show_products():
    response = product_controller.list_products()
    return response

#Obtiene un producto
@app.route('/product/<product_id>', methods=['GET'])
def show_product(product_id):
    response = product_controller.list_product(product_id)
    return response


