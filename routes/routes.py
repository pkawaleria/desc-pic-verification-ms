from flask import Blueprint
from controllers.imageController import index
from controllers.descriptionController import verify_description


image = Blueprint('user', __name__)
description = Blueprint('description', __name__)

image.route('/', methods=['GET'])(index)

description.route('/verify_text', methods=['POST'])(verify_description)
