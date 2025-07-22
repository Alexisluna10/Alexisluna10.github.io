from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/") 
def home(): 
    return render_template("home.html")

@app.route("/procesar", methods=['POST'])
def procesar():
    api = "YOUR_API_KEY"
    name = request.form.get("name")
    url = "https://fortnite-api.com/v2/stats/br/v2"
    params = {
        "name": name
    }
    headers = {
        "Authorization": api
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    minutos = data['data']['stats']['all']['overall']['minutesPlayed']

    if minutos < 1440:
        tiempo = round(minutos / 60, 2)
    else:
        tiempo = round(minutos / 1440, 2)

    return render_template("response.html", name=name, datos=data, tiempo=tiempo )

app.run()