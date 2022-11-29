import mysql.connector
import json
from flask import make_response
import jwt
from config import dbconfig


class RecipeResource_model(object):
	def __init__(self):

		try:

			self.try_connect = mysql.connector.connect(
				host=dbconfig["host"],
				user=dbconfig["user"],
				password=dbconfig["password"]
			)

			database_cursor = self.try_connect.cursor()
			database_cursor.execute("SHOW DATABASES")
			all_db= database_cursor.fetchall()
			all_db_list = []
			for i in all_db:
				all_db_list.append(i[0])

			if dbconfig["database"] not in all_db_list:
				database_cursor.execute(f"""CREATE DATABASE {dbconfig["database"]}""")
				database_cursor.execute(f"""USE {dbconfig["database"]}""")
				database_cursor.execute(f"""CREATE TABLE user (
					id int not null primary key AUTO_INCREMENT,
					username varchar(30) unique,
					email varchar(30),
					password varchar(200)
					);  """)
				database_cursor.close()
				print('table creae......')
				self.connect = mysql.connector.connect(
					host=dbconfig["host"],
					user=dbconfig["user"],
					password=dbconfig["password"],
					database = dbconfig["database"]
				)
			else:
				self.connect = mysql.connector.connect(
					host=dbconfig["host"],
					user=dbconfig["user"],
					password=dbconfig["password"],
					database = dbconfig["database"]
				)
			
			self.connect.autocommit = True
			self.cursor = self.connect.cursor(dictionary=True)
			print("\n ✅ MySQL(RecipeResource_model.py) Connection is Successful !  \n")

		except:
			print("\n🐞 Whoops !!! Some Error in DATABASE Connection.")

	def get_model(self, id):
		query = f"SELECT * FROM recipe WHERE id={id}"
		self.cursor.execute(query)
		payload = self.cursor.fetchone()

		if self.cursor.rowcount > 0:
			res = make_response({"payload": payload}, 200)
			return res
		res = make_response({"message": "data not found"}, 404)
		return res

	def put_model(self, id, json_data):

		query = f"""UPDATE recipe SET title='{json_data['title']}' , description ='{json_data['description']}' WHERE id = {id} """
		self.cursor.execute(query)
		if self.cursor.rowcount > 0:
			res = make_response({"message": "Successful updated"}, 200)
			return res
		res = make_response({"message": "cannot insert"}, 409)
		return res

	def delete_model(self, id):
		query = f"DELETE FROM recipe WHERE id = {id}"
		self.cursor.execute(query)
		if self.cursor.rowcount > 0:
			res = make_response({"message": "Successful deleted"}, 202)
			return res
		res = make_response({"message": "not found"}, 404)
		return rs
