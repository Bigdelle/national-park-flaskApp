from flask import Flask, render_template, request, redirect, url_for
from flask.templating import render_template_string
import requests
import json
import data


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def home_index():
    return render_template('index.html')


@app.route('/activities')
def index():
    req = requests.get('https://developer.nps.gov/api/v1/activities/parks?parkCode=&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV')
    data = json.loads(req.content)
    return render_template('activities.html', data=data)

@app.route('/activities', methods=['POST'])
def my_newform_post():
    activity = str(request.form['park_code'])
    parks = dict(data.get_parks(activity))
    global data_stuff
    global values
    data_stuff = parks
    values = activity
    if len(data_stuff) == 0:
        values = 'There is no activity that matches the input'
    return redirect('/return')

@app.route('/return')
def index_render():
    return render_template('return.html', data = data_stuff, val=values)

@app.route('/return', methods=['POST'])
def get_info():
    global park_id
    park_id = request.form['park-but']
    park_id = park_id[park_id.rfind(' ')+1:]
    print(park_id)
    return redirect('/parkinfo')
    

@app.route('/parkinfo')
def parkinfo_index():
    park_name = data.get_name(park_id)
    description = data.get_description(park_id)
    img = data.get_image(park_id)
    lat_long = data.get_lat(park_id)
    state = data.get_state(park_id)
    return render_template('parkinfo.html', data = park_name, desc = description, image = img, lat = lat_long, st = state)