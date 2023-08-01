from flask import Blueprint
from controllers.imageController import verify_image
from controllers.descriptionController import verify_description


image = Blueprint('user', __name__)
description = Blueprint('description', __name__)

image.route('/verify_image', methods=['POST'])(verify_image)

description.route('/verify_text', methods=['POST'])(verify_description)
