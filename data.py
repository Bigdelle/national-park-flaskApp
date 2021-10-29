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
                dict[park_data['data'][x]['parks'][y]['parkCode']] = park_data['data'][x]['parks'][y]['designation']
    print(dict)



get_parks('Auto and ATV')
