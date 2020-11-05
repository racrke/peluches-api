from models import user as repo
from flask import request, make_response, jsonify


def create_user():
	user = repo.User()
	data = request.get_json()

	user.ID = data["username"]
	user.set_password(data["password"])
	user.name = "('{0}','{1}'')".format(data["firstName"],data["lastName"])
	user.email = data["email"]

	result = user.insert()

	if result:
		response = make_response(jsonify(data))
		code = 200
	else:
		json = {"error":result}
		response = make_response(jsonify(json))
		code = 400
	return response, code