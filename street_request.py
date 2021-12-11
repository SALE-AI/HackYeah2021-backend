from flask import Blueprint, request
from const.status_codes import HTTP_400_BAD_REQUEST

b1 = Blueprint('street_finder', __name__ , url_prefix='/api/v1')

def compute_ratings(data):
    ###TODO: implement an algorithm
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

@b1.route('/scores', methods=('POST'))
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
    data = request.get_json()
    errors = []
    if not data['street']:
        errors.append('Street is required')

    if errors:
        return {
            'address': {
                'code': '',
                'city': '',
                'street': '',
                'building_number': '',
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

    ratings = compute_ratings(api_data)

    return {
        'address': {
            'code': data['code'],
            'city': data['city'],
            'street': data['street'],
            'building_number': data['building_number'],
        },
        'results': ratings
    }