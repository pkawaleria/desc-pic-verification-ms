from flask import request, jsonify
import requests

def check_image_profanity():
    try:
        image_file = request.files['image']
        headers = {
            'Apikey': '4c09c577-a6fc-4b48-a162-6cfe53471d49',
            'Content-Type': 'multipart/form-data'
        }
        # Wyślij zapytanie POST do Cloudmersive Image API
        response = requests.post('https://api.cloudmersive.com/image/nsfw/classify', headers=headers, data =image_file)

        res = response.json()
        result = res['Score']
        threshold = 0.3
        if result > threshold:
            return jsonify({'has_inappropriate_content': "True"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'has_inappropriate_content': "False"})