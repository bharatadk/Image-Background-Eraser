from flask import Blueprint
from flask import request, make_response
from flask_cors import CORS
from flask import send_file
import datetime
from flask import current_app
import os
from ml_miscs.ml_run_model import background_eraser
from ml_miscs.transparent import make_transparent
from ml_miscs.antialias import antialiasing_edges

from models.auth_model import auth_model


auth_model_decorator = auth_model()


image_upload_bp = Blueprint("image_upload_bp", __name__)
CORS(image_upload_bp, supports_credentials=True)


@image_upload_bp.route("/", methods=["POST"])
def user_get_avatar_controller():
    # return str(request.files)
    file = request.files["avatar"]
    file_extension = file.filename.split(".")[-1]
    unique_filename = str(datetime.datetime.now().timestamp()).replace(".", "")
    unique_filename += "." + "png"
    unique_filename_with_path = "temp_img/uploads/" + unique_filename
    file.save(unique_filename_with_path)

    background_eraser(unique_filename)
    make_transparent(unique_filename)
    antialiasing_edges(unique_filename, premium=False)
    return make_response(
        {
            "message": "erase-success",
            "image_returned": f"http://127.0.0.1:5000/static/{unique_filename}",
        }
    )


@image_upload_bp.route("/premium", methods=["POST"])
@auth_model_decorator.token_auth_model("")
def user_get_avatar_controller_premuim():
    # return str(request.files)
    file = request.files["avatar"]
    file_extension = file.filename.split(".")[-1]
    unique_filename = str(datetime.datetime.now().timestamp()).replace(".", "")
    unique_filename += "." + "png"
    unique_filename_with_path = "temp_img/uploads/" + unique_filename
    file.save(unique_filename_with_path)

    background_eraser(unique_filename)
    make_transparent(unique_filename)
    antialiasing_edges(unique_filename, premium=True)
    return make_response(
        {
            "message": "erase-success",
            "image_returned": f"http://127.0.0.1:5000/static/{unique_filename}",
        }
    )
