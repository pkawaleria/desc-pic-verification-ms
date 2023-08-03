import hashlib

def calculate_image_hash(image):
    image_hash = hashlib.sha256(image).hexdigest()
    return image_hash
