
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
    return redirect('/return')

@app.route('/return')
def index_render():
    return render_template('return.html', data = data_stuff, val=values)


