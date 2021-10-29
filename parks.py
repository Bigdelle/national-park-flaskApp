import urllib.request, json

def get_data(query, parkcode):
    urlData = 'https://developer.nps.gov/api/v1/' + query + '?parkCode=' + parkcode + '&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV'
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    return JSON_object

def get_parks():
    park_data = get_data('parks', '')
    total = park_data['total']
    
    

