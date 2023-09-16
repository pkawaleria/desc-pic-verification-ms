from flask import request, jsonify
from profanityfilter import ProfanityFilter
import os

file_path = os.path.join(os.path.dirname(_file_), '..', 'sources', 'banwords.txt')

with open(file_path, "r", encoding='utf-8') as f:
    custom_list = [l.replace("\n", "") for l in f.readlines()]

pf = ProfanityFilter(custom_censor_list=custom_list)

def check_description_profanity():
    try:
        text = request.json.get('text')
        is_clear = pf.is_clean(text)
        return jsonify({'has_inappropriate_content': not is_clear})
    except Exception as e:
        return jsonify({'error': str(e)}), 400