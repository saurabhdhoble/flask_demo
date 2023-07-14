from flask import Blueprint, current_app
import requests

character_blueprint = Blueprint(name='Character', import_name=__name__)

@character_blueprint.route('/character/<character_name>')
def get_character(character_name):
    quotes_api_key = current_app.config.get('QUOTES_API_KEY')
    headers = {
        'Authorization': f'Bearer {quotes_api_key}',
        'Accept': 'application/json'
    }
    request_url = f'https://the-one-api.dev/v2/character'
    resp_json = requests.get(url=request_url, headers=headers).json()
    
    character = [chr for chr in resp_json['docs'] if chr['name'].lower()==character_name.lower()]

    return character