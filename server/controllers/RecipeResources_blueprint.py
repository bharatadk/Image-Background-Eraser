from flask import Blueprint
from flask import request
from models.RecipeResources_model import RecipeResources_model
from flask_cors import CORS


RecipeResources_model = RecipeResources_model()


recipes_bp = Blueprint("recipes_bp",__name__)
CORS(recipes_bp,supports_credentials=True)

# CORS(recipes_bp, resources={"*": {"origins": "http://localhost:3000"}})


#HTTP METHODS
all_methods=["GET","POST"]

@recipes_bp.route("/",methods=all_methods)
def get_controller():
	method = request.method
	if method == "POST":
		json_data = request.json
		return RecipeResources_model.post_model(json_data)
	else:
		return RecipeResources_model.get_model()