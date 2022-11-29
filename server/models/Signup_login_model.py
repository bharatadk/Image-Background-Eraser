import mysql.connector
import json
from flask import make_response
import jwt
from config import dbconfig
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class Signup_login_model(object):
    def __init__(self):

        try:

            self.connect = mysql.connector.connect(
                host=dbconfig["host"],
                user=dbconfig["user"],
                password=dbconfig["password"],
                database=dbconfig["database"],
            )

            self.connect.autocommit = True
            self.cursor = self.connect.cursor(dictionary=True)
            print("\n ✅ MySQL(Signup_login_model.py) Connection is Successful !  \n")

        except:
            print("\n🐞 Whoops !!! Some Error in DATABASE Connection.")

    def signup_model(self, json_data):

        password_hash = generate_password_hash(json_data["password"])
        query = f"SELECT * FROM user WHERE username='{json_data['username']}'"
        self.cursor.execute(query)
        if self.cursor.fetchone():
            return make_response({"message": "User already exists "}, 201)

        query = f"""INSERT INTO user (username,email,password) VALUES 
		('{json_data['username']}','{json_data['email']}','{password_hash}') """

        self.cursor.execute(query)
        if self.cursor.rowcount > 0:
            res = make_response({"message": "Successful User created"}, 201)
            return res
        res = make_response({"message": "Issues creating user "}, 409)
        return res

    def login_model(self, json_data):

        query = f"SELECT * FROM user WHERE username='{json_data['username']}'"
        self.cursor.execute(query)
        payload = self.cursor.fetchone()

        if payload is None:
            return make_response({"message": "No such user exists empty"})

        if not check_password_hash(payload["password"], json_data["password"]):
            return make_response({"message": "Incorrect password"})

        # deleting password_hash for jwt token
        del payload["password"]

        acc_exp = int(
            (datetime.datetime.now() + datetime.timedelta(seconds=4000)).timestamp()
        )
        ref_exp = int(
            (datetime.datetime.now() + datetime.timedelta(days=1)).timestamp()
        )
        access_token = jwt.encode(
            {"payload": payload, "exp": acc_exp}, key="access", algorithm="HS256"
        )
        refresh_token = jwt.encode(
            {"payload": payload, "exp": ref_exp}, key="refresh", algorithm="HS256"
        )
        res = make_response(
            {
                "access_token": f"Bearer {access_token}",
                "refresh_token": f"Bearer {refresh_token}",
            },
            201,
        )
        return res
