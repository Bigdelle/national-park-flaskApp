from logging import info
import urllib.request, json
import random

def random_picture():
    images = ['https://afar-production.imgix.net/uploads/images/afar_post_headers/images/iDlkx4v5ic/original_Rocky_20Mountain_20National_20Park.jpg?auto=compress,format&fit=crop&crop=top&lossless=true&w=1600&h=700',
    'https://cdn.cheapism.com/images/National_Park_Photos.2e16d0ba.fill-1440x605.png', 'https://www.nps.gov/articles/images/GRSA_NPSphoto_960w.jpg?maxwidth=1200&maxheight=1200&autorotate=false',
    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/hiker-in-north-window-arch-royalty-free-image-1588786762.jpg?crop=1.00xw:0.752xh;0,0.103xh&resize=1200:*',
    'https://www.fodors.com/wp-content/uploads/2020/11/gert-boers-qQC8tyG_JVA-1920-unsplash-800-crop.jpg', 'https://www.visitarizona.com/imager/s3_us-west-1_amazonaws_com/aot-2020/images/landmarks/cpebdgynftnhaigpec7f_b2b0b89039603b931027eb2900b66531.jpg']
    return random.choice(images)

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

def get_webcam(park_code):
    status = 'Actively Streaming :)'
    web_info = get_data('webcams', park_code)
    try:
        streaming_status = web_info['data'][0]['status']
        if streaming_status == 'Inactive':
          status = 'Not actively streaming :('
          url = ''
          return status, url
        elif streaming_status == 'Active':
            return status, web_info['data'][0]['url']
    except:
        status = 'There is no park with that code!'
        url = ''
        return status, url
    status = 'That park is not streaming actively'
    url = ''
    return status, url
    