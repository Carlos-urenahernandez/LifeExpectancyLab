# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request

import json
app = Flask(__name__, static_url_path='', static_folder='static')
with open('labs/LifeExpectancyLab/data/life_expectancy.json') as f:
        data = json.load(f)
minVal = min(list(data['Canada'].values()) + list(data['United States'].values()) + list(data['Mexico'].values()))
maxVal = max(list(data['Canada'].values()) + list(data['United States'].values()) + list(data['Mexico'].values()))

@app.route('/')
def index():
    print(data["Canada"].values())
    avg = (sum(list(data["Canada"].values())) + sum(list(data["United States"].values())) + sum(list(data["Mexico"].values()))) / (len(list(data["Canada"].values())) )    
    return render_template('index.html', caData = list(data['Canada'].values()), usData = list(data['United States'].values()), mxData = list(data['Mexico'].values()), average = avg)

@app.route('/year')
def year():
    currentYear = request.args.get('year')
   
    caColor = int((data['Canada'][currentYear]-minVal)/(maxVal-minVal)*100)
    usColor = int((data['United States'][currentYear]-minVal)/(maxVal-minVal)*100)
    mxColor = int((data['Mexico'][currentYear]-minVal)/(maxVal - minVal)*100)

    fiftyYears = (50-minVal) / (maxVal - minVal) * 100
    sixtyYears = (60-minVal) / (maxVal - minVal) * 100
    seventyYears = (70-minVal) / (maxVal - minVal) * 100
    eightyYears = (80-minVal) / (maxVal - minVal) * 100
    ninetyYears = (90-minVal) / (maxVal - minVal) * 100

    mxexpectancy = data['Mexico'][currentYear]
    usexpectancy = data['United States'][currentYear]
    caexpectancy = data['Canada'][currentYear]
    return render_template('year.html', year = currentYear, caSaturation = caColor, usSaturation = usColor, mxSaturation = mxColor, fifty = fiftyYears, sixty = sixtyYears, seventy = seventyYears, eighty = eightyYears, ninety = ninetyYears, usExpectancy = usexpectancy, caExpectancy = caexpectancy, mxExpectancy = mxexpectancy)

app.run(debug=True)
