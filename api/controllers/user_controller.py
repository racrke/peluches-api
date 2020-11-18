from models import user as repo
from flask import request, make_response, jsonify


def create_user():
    user = repo.User()
    data = request.get_json()

    user.ID = data["username"]
    user.set_password(data["password"])
    user.name = "('{0}','{1}'')".format(data["firstName"],data["lastName"])
    user.mail = data["email"]
    user.u_type = "Client"

    result = user.insert()

    if result:
        response = make_response(jsonify(data))
        code = 200
    else:
        json = {"error":result}
        response = make_response(jsonify(json))
        code = 400
    return response, code

def get_user(mail):
    print("MIAILL",mail)
    user = repo.User()
    user.get_with_email(mail)
    response = user.to_json()
    return make_response(jsonify(response)), 200

