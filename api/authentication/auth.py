import jwt
import datetime
from flask import request, make_response, jsonify
#from ..config import users
import os
import bcrypt

def verify_password(username):
    """
    Verify username with token
    :return: true if token is valid
    """
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        resp = decode_auth_token(auth_token)

        #if resp in users.registered_users:
         #   return True

    else:
        False


def user_exists(username, password):
    """
    Checks if username exists and password matches
    :return: true if users and password matches
    """
    if username in users.registered_users:

    	#BD CONNECT
        if bcrypt.checkpw(password.encode(),users.registered_users[username]):
            return True
    return False


def generate_token():
    """
    Creates a token  if username and password matches.
    :return: response with token
    """
    info = request.get_json()

    if "username" not in info or "password" not in info:
        responseObject = {
            'status': 'fail',
            'message': 'Unable to process credentials.'}
        return make_response(jsonify(responseObject)), 401
    username = info["username"]
    password = info["password"]

    if user_exists(username, password):
        encode_auth_token(username)
        responseObject = {
            'status': 'success',
            'token': encode_auth_token(username).decode()
        }

        return make_response(jsonify(responseObject)), 200
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid credentials.'
        }
        return make_response(jsonify(responseObject)), 401


def encode_auth_token(user):
    """
    Generates the Auth Token
    :return token: Bearer Token
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8),
            'iat': datetime.datetime.utcnow(),
            'sub': user
        }
        return jwt.encode(
            payload,
            os.getenv("SECRET_KEY"),
            algorithm='HS256'
        )
    except Exception as e:
        print(e)
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: username
    """
    try:
        payload = jwt.decode(auth_token, os.getenv("SECRET_KEY"))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'