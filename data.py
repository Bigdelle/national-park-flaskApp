from logging import info
import urllib.request, json

def get_data(query, parkcode):
    urlData = 'https://developer.nps.gov/api/v1/' + query + '?parkCode=' + parkcode + '&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV'
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    return JSON_object

def get_parks(activity):
    park_data = get_data('activities/parks', '')
    total = park_data['total']
    dict = {}
    for x in range (0, int(total)):
        if park_data['data'][x].get('name') == activity:
            tot = len(park_data['data'][x]['parks'])
            for y in range(0,tot):
                dict[park_data['data'][x]['parks'][y]['parkCode']] = park_data['data'][x]['parks'][y]['fullName']
    return dict

def get_name(park_code):
    name_info = get_data('parks', park_code)
    name = name_info['data'][0]['fullName'] + ': ' + name_info['data'][0]['parkCode']
    return name


def get_description(park_code):
    description_info = get_data('parks', park_code)
    description = description_info['data'][0]['description']
    return description

def get_image(park_code):
    image_info = get_data('parks', park_code)
    info = image_info['data'][0]['images'][0]['url']
    return info

def get_lat(park_code):
    lat_info = get_data('parks', park_code)
    lat = lat_info['data'][0]['latLong']
    return lat

def get_state(park_code):
    state_info = get_data('parks', park_code)
    state = state_info['data'][0]['states']
    return state


