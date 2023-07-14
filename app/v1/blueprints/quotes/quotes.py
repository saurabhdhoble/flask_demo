from flask import Blueprint, current_app
import requests
import random

quotes_blueprint = Blueprint(name='Quotes', import_name=__name__)

@quotes_blueprint.route('/quotes/<character_name>/quote')
def get_quote(character_name):
    '''
        GET handler to return a random quote for given character name
    '''
    quotes_api_key = current_app.config.get('QUOTES_API_KEY')
    headers = {
        'Authorization': f'Bearer {quotes_api_key}',
        'Accept': 'application/json'
    }
    character_request_url = f'https://the-one-api.dev/v2/character'

    # get the character ID first
    resp = requests.get(url=character_request_url, headers=headers)
    if resp.status_code != 200:
        return {
            'success': 'Failure',
            'message': f'Error when trying to fetch {character_name}'
        }, 500

    try:
        resp_json = resp.json()
    except Exception as e:
        return generate_exception_message(e), 500
        
    character = [chr for chr in resp_json['docs'] if chr['name'].lower()==character_name.lower()]

    if len(character) == 0:
        return {
            'success': 'Failure',
            'message': f'No character with name {character_name} was found.'
        }, 404

    quote_request_url = f'https://the-one-api.dev/v2/character/{character[0]["_id"]}/quote'

    resp_json = requests.get(url=quote_request_url, headers=headers).json()

    return {
        'success': 'Success',
        'quote': random.choice(resp_json['docs'])['dialog']
    }


def generate_exception_message(e):
    return {
            'success': 'Failure',
            'message': f'Error when trying to fetch resource - {e.Message}'
        }