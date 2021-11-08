from logging import info
import urllib.request, json

def get_data(query, parkcode):
    urlData = 'https://developer.nps.gov/api/v1/' + query + '?parkCode=' + parkcode + '&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV'
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    return JSON_object


def get_data_max(query, limit, parkcode):
    #limit functionality
    urlData = 'https://developer.nps.gov/api/v1/' + query + '?limit=' + limit + 'parkCode=' + parkcode + '&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV'
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    return JSON_object


def get_parks(activity):
    park_data = get_data('activities/parks', '')
    total = park_data['total']
    dict = {}
    for x in range (0, int(total)):
        if park_data['data'][x].get('name').lower() == activity.lower():
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


def get_url(park_code):
    url_info = get_data('parks', park_code)
    url = url_info['data'][0]['url']
    return url


def get_directions(park_code):
    directions_info = get_data('parks', park_code)
    directions = directions_info['data'][0]['directionsInfo']
    directionsURL = directions_info['data'][0]['directionsUrl']
    return directions, directionsURL


def get_parks_state(state_code):
    park_data = get_data_max('parks', '464', '')
    dict = {}
    for x in range (0, 464):
        if park_data['data'][x].get('states').lower() == state_code.lower():
            dict[park_data['data'][x]['parkCode']] = park_data['data'][x]['fullName']
    return dict


def get_hours(park_code):
    hours_info = get_data('parks', park_code)
    days = ['Wednesday', 'Monday', 'Thursday', 'Sunday', 'Tuesday', 'Friday', 'Saturday']
    hours_dict = {}
    for x in range(0, 7):  
        hours_dict[days[x]] = hours_info['data'][0]['operatingHours'][0]['standardHours'][days[x].lower()]
    description = hours_info['data'][0]['operatingHours'][0]['description']
    return hours_dict, description

def get_webcame(park_code):
    returned = ''
    web_info = get_data('webcams', park_code)
    streaming_status = web_info['data'][0]['isStreaming']
    if streaming_status == False:
        returned = 'Not Streaming'
    return returned