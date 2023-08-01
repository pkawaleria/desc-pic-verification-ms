from flask import request, jsonify
from nsfw_detector import *
from nsfw_detector import predict
import os

path = os.path.abspath('./services/nsfw_mobilenet2.224x224.h5')

model = predict.load_model(path)

def check_image_profanity():
    image = request.files['image'].read()
    result = predict.classify(model, 'C:/Users/Radek/Desktop/logo.jpg')
    print(result)
    probability = result['C:/Users/Radek/Desktop/logo.jpg']['porn']
    threshold = 0.3
    if probability > threshold:
        return jsonify({'has_inappropriate_content': "True"})
    return jsonify({'has_inappropriate_content': "False"})