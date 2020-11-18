import jwt
import datetime
from flask import request, make_response, jsonify
#from ..config import users
import bcrypt, base64
from models import user as repo


def verify_token(token):
    """
    Verify email with token
    :return: true if token is valid
    """
    #auth_header = request.headers.get('Authorization')
    
    if token:
        resp = decode_auth_token(token)
        if repo.User().get_with_email(resp):
            return True

    else:
        False


def user_exists(email, password):
    """
    Checks if email exists and password matches
    :return: true if users and password matches
    """
    user = repo.User()
    exists = user.get(email)
    print(exists)
    if exists:

        #BD CONNECT
        bd_password = base64.b64decode(user.password)
        if bcrypt.checkpw(password.encode(),bd_password):
            return True
    return False


def generate_token():
    """
    Creates a token  if email and password matches.
    :return: response with token
    """
    info = request.get_json()

    if "email" not in info or "password" not in info:
        responseObject = {
            'status': 'fail',
            'message': 'Unable to process credentials.'}
        return make_response(jsonify(responseObject)), 401
    email = info["email"]
    password = info["password"]

    if user_exists(email, password):
        responseObject = {
            'status': 'success',
            'token': encode_auth_token(email).decode()
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
            "webProyect2020",
            algorithm='HS256'
        )
    except Exception as e:
        print("Encode_Auth::",e)
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: email
    """
    try:
        payload = jwt.decode(auth_token, "webProyect2020")
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
