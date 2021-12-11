from flask import Blueprint, request
from const.status_codes import HTTP_400_BAD_REQUEST

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
    errors = []
    
    # check which method was used
    in_data = dict()
    try:
        if request.method == 'POST':
            in_data['street'] = request.json['street']
        else: # request.method == 'GET'
            in_data['street'] = request.args.get('street')
            if in_data['street'] is None:
                raise ValueError
    except (KeyError, ValueError) as e:
        errors.append('Street is required')
        in_data['street'] = None

    KEYS = ['city', 'code', 'building_number']

    for key in KEYS:
        try:
            if request.method == 'POST':
                in_data[key] = request.json[key]
            else: # request.method == 'GET'
                in_data[key] = request.args.get(key)
        except KeyError:
            in_data[key] = None

    if errors:
        return {
            'address': {
                'code': in_data['code'],
                'city': in_data['city'],
                'street': in_data['street'],
                'building_number': in_data['building_number'],
            },
            'errors': [errors]
        }, HTTP_400_BAD_REQUEST

    try:
        #TODO: send request
        req = None
        api_data = []
    except ValueError: # or any other exceptions
        #TODO: exceptions: not found, bad request, no connection
        pass

    ratings = compute_ratings(in_data)

    return {
        'address': {
            'code': in_data['code'],
            'city': in_data['city'],
            'street': in_data['street'],
            'building_number': in_data['building_number'],
        },
        'results': ratings
    }