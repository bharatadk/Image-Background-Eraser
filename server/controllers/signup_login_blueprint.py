from flask import Blueprint
from flask import request
from flask import make_response
from flask import current_app

from models.Signup_login_model import Signup_login_model
from models.auth_model import auth_model
from flask import jsonify
from flask_cors import CORS

signup_login_model = Signup_login_model()
auth_model_decorator = auth_model()


signup_login_bp = Blueprint("signup_login_bp", __name__)
# CORS(signup_login_bp, resources={"*": {"origins": "http://localhost:3000"}})
CORS(signup_login_bp, supports_credentials=True)


# HTTP METHODS
all_methods = ["GET", "POST", "PUT"]


@signup_login_bp.route("/signup", methods=all_methods)
def signup_controller():
    method = request.method
    if method == "POST":
        json_data = request.json
        return signup_login_model.signup_model(json_data)
    else:
        pass


@signup_login_bp.route("/login", methods=all_methods)
def login():
    method = request.method
    if method == "POST":
        json_data = request.json
        if "body" in json_data.keys():
            json_data = json_data["body"]
        print("............json_data", json_data)
        acc_and_ref_token = signup_login_model.login_model(json_data).json
        # auth_model.access_token = acc_and_ref_token["access_token"]
        # auth_model.refresh_token = acc_and_ref_token["refresh_token"]
        return acc_and_ref_token

    else:
        pass


@signup_login_bp.route("/protected", methods=all_methods)
@auth_model_decorator.token_auth_model("")
def protected():
    method = request.method
    if method == "POST":
        return make_response({"message": "post bharta"})

    if method == "GET":
        return make_response({"message": " getbharatdsdfsdf"})
    return "protected data received"


@signup_login_bp.route("/refresh_token", methods=all_methods)
def refresh_token():
    if request.method == "GET":
        jwt_refresh_token = request.headers

        print(jwt_refresh_token)
        if "headers" in jwt_refresh_token.keys():
            jwt_refresh_token = jwt_refresh_token["headers"]
        print(jwt_refresh_token)
        jwt_refresh_token = jwt_refresh_token["Authorization"]

        # print("\n \n",jwt_refresh_token)
        obj = auth_model()
        obj.refresh_token = jwt_refresh_token
        obj.refresh_token_model()
        jwt_access_token = obj.access_token
        # del obj
        res = make_response({"access_token": jwt_access_token}, 200)
        res.headers.add("Access-Control-Allow-Origin", "*")
        res.headers.add("Access-Control-Allow-Headers", "*")
        res.headers.add("Access-Control-Allow-Methods", "*")
        return res

    return "something wrong"
