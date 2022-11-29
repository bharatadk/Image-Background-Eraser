from flask import Flask
from flask_restx import Api, Resource
import config
from flask_cors import CORS


# Blueprint-controllers
from controllers.RecipeResource_blueprint import recipe_bp
from controllers.RecipeResources_blueprint import recipes_bp
from controllers.signup_login_blueprint import signup_login_bp
from controllers.ImageUpload_bp import image_upload_bp


app = Flask(__name__)

#Register blueprints
app.register_blueprint(recipe_bp, url_prefix='/recipe')
app.register_blueprint(recipes_bp, url_prefix='/recipes')
app.register_blueprint(signup_login_bp,url_prefix="/auth")
app.register_blueprint(image_upload_bp,url_prefix="/upload")


CORS(app,supports_credentials=True)

# CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


# api = Api(app, doc = "/")


@app.route("/")
def gets():
	return "ram"
	return {"message":"hello world"}


if __name__ == "__main__":
	app.run(debug=True)

