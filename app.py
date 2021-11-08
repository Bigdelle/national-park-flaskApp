from flask import Flask, render_template, request, redirect, url_for
from flask.templating import render_template_string
import requests
import json
import data


app = Flask(__name__)

@app.route("/")
def home():
    url = data.random_picture()
    return render_template('index.html', data = url)


@app.route("/index")
def index_home():
    url = data.random_picture()
    return render_template('index.html', data = url)


@app.route('/activities')
def index_activities():
    #req = requests.get('https://developer.nps.gov/api/v1/activities/parks?parkCode=&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV')
    #data = json.loads(req.content)
    return render_template('activities.html')


@app.route('/activities', methods=['POST'])
def activities_form():
    activity = str(request.form['park_code'])
    parks = dict(data.get_parks(activity))
    global park_data
    global values
    park_data = parks
    values = activity
    if len(park_data) == 0:
        values = 'There is no activity that matches the input'
    return redirect('/return')


@app.route('/return')
def index_return():
    return render_template('return.html', data = park_data, val=values)


@app.route('/return', methods=['POST'])
def park_id_form():
    global park_id
    park_id = request.form['park-but']
    park_id = park_id[park_id.rfind(' ')+1:]
    print(park_id)
    return redirect('/parkinfo')
    

@app.route('/parkinfo')
def index_parkinfo():
    park_name = data.get_name(park_id)
    description = data.get_description(park_id)
    img = data.get_image(park_id)
    lat_long = data.get_lat(park_id)
    state = data.get_state(park_id)
    url = data.get_url(park_id)
    dir, dirURL = data.get_directions(park_id)
    hours, hour_desc = data.get_hours(park_id)
    return render_template('parkinfo.html', data = park_name, desc = description, image = img, lat = lat_long, st = state, urls = url,
    directions = dir, directionsUrl = dirURL, hour=hours, hour_descrip = hour_desc)


@app.route('/state')
def index_state():
    return render_template('state.html')


@app.route('/state', methods=['POST'])
def form_state_code():
    state_code = str(request.form['state_code'])
    parks = dict(data.get_parks_state(state_code))
    global state_data
    global states_code
    state_data = parks
    states_code = state_code.upper()
    if len(state_data) == 0:
        states_code = 'No parks or invalid input'
    return redirect('/state_search')


@app.route('/state_search')
def index_state_sarch():
    return render_template('state_search.html', data = state_data, val=states_code)


@app.route('/state_search', methods=['POST'])
def form_state_search():
    global park_id
    park_id = request.form['park-but']
    park_id = park_id[park_id.rfind(' ')+1:]
    return redirect('/parkinfo')

@app.route('/webcams')
def index_webcams():
    return render_template('webcams.html')

@app.route('/webcams', methods=['POST'])
def webcame_form_state_code():
    global park_d
    park_d = str(request.form['park_code'])
    return redirect('/webcam_dynamic')


@app.route('/webcam_dynamic')
def index_webcam_dynamic():
    status, cam_url = data.get_webcam(park_d)
    return render_template('webcam_dynamic.html', data = park_d.upper(), url = cam_url, stat = status)
