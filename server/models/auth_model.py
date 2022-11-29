import mysql.connector
import jwt
import json
from flask import make_response,redirect
from flask import request
from functools import wraps
import re
from config import dbconfig
import datetime


class auth_model(object):
	def __init__(self):
		self.access_token = ""
		self.refresh_token = ""
		self.JWT_Refresh_time=0

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

	def refresh_token_model(self):

		
		jwt_refresh_token = self.refresh_token.split(" ")[1]

		jwt_decoded = jwt.decode(jwt_refresh_token, key="refresh", algorithms="HS256")

		json_data = jwt_decoded["payload"]
		decoded_username = json_data["username"]

		query = (
			f"SELECT id,email,username FROM user WHERE username='{decoded_username}'"
		)
		self.cursor.execute(query)
		payload = self.cursor.fetchone()

		acc_exp = int(
			(datetime.datetime.now() + datetime.timedelta(seconds=4000)).timestamp()
		)
		self.access_token = jwt.encode(
			{"payload": payload, "exp": acc_exp}, key="access", algorithm="HS256"
		)
		self.access_token = f"Bearer {self.access_token}"

		# self.token_verify_model()


	def token_verify_model(self):
		jwt_token=request.headers
		if "headers" in jwt_token.keys():
			jwt_token = jwt_token["headers"]
		print("\n\n ",jwt_token)

		jwt_token = jwt_token['Authorization']
		print("\n\n\njwt_token.........\n\n\n",jwt_token)

		# jwt decode
		# jwt_token = self.access_token

		if not jwt_token:
			return "no-JWT"


		# RegEx check
		if re.match("^Bearer *([^ ]+) *$", jwt_token, flags=0):

			jwt_token = jwt_token.split(" ")[1]
			try:
				jwt_decoded = jwt.decode(jwt_token, key="access", algorithms="HS256")

				decoded_username = jwt_decoded["payload"]["username"]

				# now check if the username from decoded value exist in database
				query = (
					f" SELECT username from user WHERE  username='{decoded_username}' "
				)

				self.cursor.execute(query)
				username_from_database = self.cursor.fetchone()
				username_from_database = username_from_database["username"]

				if decoded_username == username_from_database:

					return "Everything-OK"
				else:
					return "You don't have permission to visit this link"

			except jwt.ExpiredSignatureError:
				return 'JWT-expired'
			except jwt.InvalidSignatureError:
				return 'invalid'			
			except jwt.exceptions.DecodeError:
				return 'invalid'


		else:
			return 'invalid'

	def token_auth_model(self, sth=""):
		def outer_wrapper(func):
			@wraps(func)
			def inner_wrapper(*args, **kwargs):

				authorization_res = self.token_verify_model()

				if authorization_res == "Everything-OK":
					get_controller_func = func()
					return get_controller_func

				if authorization_res == "JWT-expired":
					return make_response({"message":"JWT-expired"})

				return make_response({"message":"invalid-JWT"})



			return inner_wrapper

		return outer_wrapper
