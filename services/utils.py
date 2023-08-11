import hashlib

def calculate_image_hash(image_data):
    image_hash = hashlib.sha256(image_data).hexdigest()
    return image_hash
