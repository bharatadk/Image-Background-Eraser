from flask import Blueprint
from flask import request
from flask_cors import CORS
from models.RecipeResource_model import  RecipeResource_model

RecipeResource_model = RecipeResource_model()

recipe_bp= Blueprint('recipe_bp', __name__)

CORS(recipe_bp,supports_credentials=True)
# CORS(recipe_bp, resources={"*": {"origins": "http://localhost:3000"}})


#HTTP METHODS
all_methods=["GET","POST","PUT","DELETE"]


@recipe_bp.route('/<int:id>',methods=all_methods)
def get_controller(id):
    """Get a recipe by id """

    method = request.method
    if method == "POST":
        json_data = request.json
        return RecipeResource_model.post_model(id,json_data)

    elif method =="PUT":
        json_data = request.json
        return RecipeResource_model.put_model(id,json_data)

    elif method == "DELETE":
        return RecipeResource_model.delete_model(id)

    else:
        return RecipeResource_model.get_model(id)


