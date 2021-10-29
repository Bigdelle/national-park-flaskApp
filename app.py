from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    req = requests.get('https://developer.nps.gov/api/v1/activities/parks?parkCode=&api_key=3wguztEg5MM7UMGZI7jFbo2cBBhXvUq30k53GJHV')
    data = json.loads(req.content)
    return render_template('index.html', data=data)
