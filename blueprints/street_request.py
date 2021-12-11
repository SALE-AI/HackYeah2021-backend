from flask import Blueprint, request
from const.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from bik_api.getters import getDemographic, getUczelnie
from requests import exceptions

street_finder = Blueprint('street_finder', __name__ , url_prefix='/api/v1')

def compute_ratings(data):
    #TODO: implement an algorithm
    res = {
        'office': {
            'score': 0.2245,
            'reasons': [
                'Close to main road',
                'Close to railway station',
                'Nearby tram',
                'Not so many offices nearby'
            ]
        },
        'convenience': {
            'score': 0.0003,
            'reasons': [
                'Too much conveniences nearby',
                'Many citizens',
                'No offices nearby',
                'No universities or public education nearby'
            ]
        }
    }
    return res

def generate_out_response(in_data: dict, out_data=None, errors=None):
    '''Returns dictionary which can be used to generate JSON output'''
    res = {
        'address': {
            'code': in_data['code'],
            'city': in_data['city'],
            'street': in_data['street'],
            'building_number': in_data['building_number'],
        },
    }

    if errors:
        res['errors'] = errors

    elif out_data:
        res['results'] = out_data
    
    return res

def clean_data(s):
    if s is None:
        raise TypeError('None was found')
    return s.strip('"').strip(' ')

def prepare_input_data(request):
    '''validate data and return prepared input data and errors'''
    in_data = dict()
    errors = []
    try:
        # check which method was used
        if request.method == 'POST':
            in_data['street'] = clean_data(request.json['street'])
        else: # request.method == 'GET'
            in_data['street'] = clean_data(request.args.get('street'))
            if in_data['street'] is None:
                raise TypeError
    except (KeyError, TypeError) as e:
        errors.append('Street is required')
        in_data['street'] = None
    
    KEYS = ['city', 'code', 'building_number']
    for key in KEYS:
        try:
            if request.method == 'POST':
                in_data[key] = clean_data(request.json[key])
            else: # request.method == 'GET'
                in_data[key] = clean_data(request.args.get(key))
        except (KeyError, TypeError) as e:
            in_data[key] = None

    return in_data, errors


@street_finder.route('/scores', methods=['GET', 'POST'])
def scores():
    '''
    Gets the following parameters:
    {
        code: str, NULL         - postal code
        city: str, NULL          - name of city, default is Łódź
        street: str             - street name
        building_number: str, NULL    - number of building
    }
    If response is valid, returns response: {
        'address': {
            ... // input response parameters
        }
        '<object>': [ // category
            'score': <int>,     - the higher score, the better
            'reasons': <list of str>,    - list of reasons how the score comes from
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
    ) as e:
        errors.append(e)
    
    if errors:
        return generate_out_response(in_data, errors=errors), HTTP_400_BAD_REQUEST

    ratings = compute_ratings(in_data)
    return generate_out_response(in_data, ratings), HTTP_200_OK
