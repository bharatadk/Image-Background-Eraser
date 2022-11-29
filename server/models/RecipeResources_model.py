import mysql.connector
import json
from flask import make_response
import jwt
from config import dbconfig


class RecipeResources_model(object):
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
            print("\n ✅ MySQL(RecipeResources_model.py) Connection is Successful !  \n")

        except:
            print("\n🐞 Whoops !!! Some Error in DATABASE Connection.")

    def get_model(self):
        """Get all recipes from database"""

        query = f"SELECT * FROM recipe"
        self.cursor.execute(query)
        payload = self.cursor.fetchall()
        return make_response({"payload": payload}, 200)

    def post_model(self, form_data):
        """Create a new recipe to database"""

        query = f"""INSERT INTO recipe (title,description) VALUES
		('{form_data['title']}','{form_data['description']}') """

        self.cursor.execute(query)
        if self.cursor.rowcount > 0:
            res = make_response({"message": "Successful inserted"}, 201)
            return res
        res = make_response({"message": "cannot insert"}, 409)
        return res
