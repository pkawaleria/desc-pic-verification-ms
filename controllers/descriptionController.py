from services.description_service import check_description_profanity
from flask import jsonify


def index():
    return {'status': 'OK'}


def verify_description():
    return check_description_profanity()
