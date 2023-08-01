from services.image_service import check_image_profanity

def index():
    return {'status': 'OK'}

def verify_image():
    return check_image_profanity()