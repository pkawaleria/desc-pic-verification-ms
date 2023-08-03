from flask import request, jsonify
import requests
from models.data import db, ImageModel
from services.utils import calculate_image_hash

def check_image_profanity():
    try:
        image_file = request.files['image'].read()

        image_hash = calculate_image_hash(image_file)

        image_in_db = ImageModel.query.filter_by(image_hash=image_hash).first()
        if image_in_db:
            if image_in_db.is_ok:
                return jsonify({'has_inappropriate_content': "False"})
            else:
                return jsonify({'has_inappropriate_content': "True"})
        else:
            headers = {
                'Apikey': '4c09c577-a6fc-4b48-a162-6cfe53471d49',
                'Content-Type': 'multipart/form-data'
            }
            response = requests.post('https://api.cloudmersive.com/image/nsfw/classify', headers=headers, data=image_file)

            res = response.json()
            result = res['Score']
            threshold = 0.3
            if result > threshold:
                new_image = ImageModel(image_hash=image_hash, is_ok=False)
                db.session.add(new_image)
                db.session.commit()
                return jsonify({'has_inappropriate_content': "True"})
            else:
                new_image = ImageModel(image_hash=image_hash, is_ok=True)
                db.session.add(new_image)
                db.session.commit()
                return jsonify({'has_inappropriate_content': "False"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400