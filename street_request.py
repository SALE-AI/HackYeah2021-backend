from flask_cors.decorator import cross_origin
import requests
from requests import exceptions
from flask import Blueprint, request
from algorithm import getRatings
from const.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST

street_finder = Blueprint('street_finder', __name__ , url_prefix='/api/v2')

def clean_data(field: str) -> str:
    '''Returns string without trailing spaces nor ". Throws TypeError if null'''
    res = field
    if res is None:
        raise TypeError('None was found')
    while res.find('_') != -1 or res.find('-') != -1:
        res = res.replace('_', ' ')
    return res.strip('"').strip(' ')

def generate_out_response(in_data: dict, ratings=None, targets=None, errors=None):
    '''Returns dictionary which can be used to generate JSON output'''
    res = {
        'address': {
            'street': in_data['street'],
            'building_number': in_data['building_number'],
        },
    }
    if errors:
        res['errors'] = errors
    else:
        res['ratings'] = ratings
        res['targets'] = targets
        res['coordinates'] = get_coords(in_data)
    return res

def get_coords(address: list):
    url = 'http://api.positionstack.com/v1/forward?access_key=6d06186d70c6be5c5bc3a1c0ffe7dce0&query='
    url += f'{address["street"]} {address["building_number"]} Łódź Lodzkie Poland'
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        return {
            'latitude': data['data'][0]['latitude'],
            'longitude': data['data'][0]['longitude']
        }
    return {
        'latitude': None,
        'longitude': None
    }

def prepare_input_data(req):
    '''validate data and return prepared input data and errors'''
    in_data = {}
    errors = []
    try:
        temp = clean_data(req.args.get('address')).split()
        in_data['street'] = ' '.join(temp[:-1])
        in_data['building_number'] = temp[-1]
        if len(temp) < 2:
            in_data['street'] = ' '.join(temp)
            in_data['building_number'] = ''
            raise ValueError('Too few parameters')
        elif temp[-1].isalpha():
            raise TypeError('Invalid building number!')
    except (KeyError, TypeError, ValueError) as error:
        errors.append(str(error))
    return in_data, errors

# routing
@street_finder.route('/scores', methods=['GET'])
@cross_origin()
def scores():
    '''
    Gets the following parameters:
        address: str    - address, street name, the last word is building number
    If response is valid, returns response: {
        'address': {
            ... // input response parameters
        }
        '<object>': [ // category
            'score': <int>,             - the higher score, the better
            'reasons': <list of str>    - list of reasons how the score comes from
        ]
    }

    If response is not valid or could not process data further, returns response: {
        'address': {
            ... // input response parameters
        }
        'error': {
            // list of errors
        }
    }
    '''
    in_data, errors = prepare_input_data(request)
    if errors:
        return generate_out_response(in_data, errors=errors), HTTP_400_BAD_REQUEST

    try:
        #TODO: read data
        pass
    except (
        exceptions.HTTPError,
        exceptions.ConnectionError,
        exceptions.Timeout,
        exceptions.RequestException,
    ) as error:
        errors.append(error)

    if errors:
        return generate_out_response(in_data, errors=errors), HTTP_400_BAD_REQUEST

    targets, ratings = getRatings(in_data["street"], in_data["building_number"])
    return generate_out_response(in_data, ratings, targets), HTTP_200_OK
