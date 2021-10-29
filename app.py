from flask import Flask, render_template, request
import requests
import json

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
    park_code = request.form['park_code']
    print(park_code)
    return 'bithc'
