from flask import request, jsonify
import requests
from models.data import db, ImageModel
from services.utils import calculate_image_hash
import json

def check_image_profanity():
    image_file = request.files['image']
    image_data = image_file.read()
    image_hash = calculate_image_hash(image_data)

    image_in_db = ImageModel.query.filter_by(image_hash=image_hash).first()
    if image_in_db:
        if image_in_db.is_ok:
            return jsonify({'has_inappropriate_content': "False"})
        else:
            return jsonify({'has_inappropriate_content': "True"})
    try:
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZTJjNzk2M2EtMzk1Ny00Y2I0LTg4NTQtNGVjZjIyYjcyN2FmIiwidHlwZSI6ImFwaV90b2tlbiJ9.UZz6R7-WM6j5YyTnGhhjg2_OJ3u1_ZBfU6MIH8og7eY"}
        url = "https://api.edenai.run/v2/image/explicit_content"
        data = {"providers": "google"}
        files = {'file': ('image.jpg', image_data, '')}

        response = requests.post(url, data=data, files=files, headers=headers)

        result = json.loads(response.text)
        result_2 = result['google']['items']
        is_above_threshold = any(item['likelihood'] >= 3 for item in result_2)


        if is_above_threshold:
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