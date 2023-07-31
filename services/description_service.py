from flask import request, jsonify
import jwt
from profanityfilter import ProfanityFilter
import os

file_path = os.path.abspath('./sources/banwords.txt')

with open(file_path, "r", encoding='utf-8') as f:
    custom_list = [l.replace("\n", "") for l in f.readlines()]

pf = ProfanityFilter(custom_censor_list=custom_list)

def check_description_profanity():
    try:
        text = request.json.get('description')
        is_clear = pf.is_clean(text)
        return jsonify({'is_clear':is_clear})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

