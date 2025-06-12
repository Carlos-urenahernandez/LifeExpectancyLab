from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path='', static_folder='static')
with open("Data/data.json", "r") as f:
    data1 = json.load(f)
brooklynData = []
bronxData = []
manhattanData = []
queensData = []
statenIslandData = []
minVal = len(data1["BROOKLYN"]["2000"])
maxVal = 0
avg = 0
for years in range (2000, 2022):
    maxVal = max(maxVal, len(data1["BROOKLYN"][str(years)]), len(data1["BRONX"][str(years)]), len(data1["MANHATTAN"][str(years)]), len(data1["QUEENS"][str(years)]), len(data1["STATEN ISLAND"][str(years)]))
    minVal = min(minVal, len(data1["BROOKLYN"][str(years)]), len(data1["BRONX"][str(years)]), len(data1["MANHATTAN"][str(years)]), len(data1["QUEENS"][str(years)]), len(data1["STATEN ISLAND"][str(years)]))
    brooklynData.append(len(data1["BROOKLYN"][str(years)]))
    bronxData.append(len(data1["BRONX"][str(years)]))
    manhattanData.append(len(data1["MANHATTAN"][str(years)]))
    queensData.append(len(data1["QUEENS"][str(years)]))
    statenIslandData.append(len(data1["STATEN ISLAND"][str(years)]))
    avg+= (len(data1["BROOKLYN"][str(years)]) + len(data1["BRONX"][str(years)]) + len(data1["MANHATTAN"][str(years)]) + len(data1["QUEENS"][str(years)]) + len(data1["STATEN ISLAND"][str(years)]))
avg = avg/(21*5)
print(avg)
@app.route('/')
def home():
    return render_template("about.html") 
@app.route('/index')    
def index():
    return render_template("index.html")
@app.route('/macro')
def macro():
    return render_template("macro.html", average = avg, data = data1, bkData = brooklynData, bxData = bronxData, maData = manhattanData, quData = queensData, siData = statenIslandData)
@app.route('/micro')
def micro():
    year = request.args.get('year', default='2000', type=str)
    quColor = int(len(data1["QUEENS"][year])- minVal) / (maxVal - minVal) * 100
    bkColor = int(len(data1["BROOKLYN"][year])- minVal) / (maxVal - minVal) * 100
    bxColor = int(len(data1["BRONX"][year])- minVal) / (maxVal - minVal) * 100
    maColor = int(len(data1["MANHATTAN"][year])- minVal) / (maxVal - minVal) * 100
    siColor = int(len(data1["STATEN ISLAND"][year])- minVal) / (maxVal - minVal) * 100
    Eight = (8000- minVal) / (maxVal - minVal) * 100
    Sixteen = (16000- minVal) / (maxVal - minVal) * 100
    Twentyfour = (24000- minVal) / (maxVal - minVal) * 100
    Thirtytwo = (32000- minVal) / (maxVal - minVal) * 100
    Forty = (40000- minVal) / (maxVal - minVal) * 100
    average = (avg-minVal) / (maxVal - minVal) * 100
    tempList = ["Brooklyn", "Bronx", "Manhattan", "Queens", "Staten Island"]
    values = [len(data1["BROOKLYN"][year]), len(data1["BRONX"][year]), len(data1["MANHATTAN"][year]), len(data1["QUEENS"][year]), len(data1["STATEN ISLAND"][year])]
    minimum = tempList[values.index(min(values))]
    maximum = tempList[values.index(max(values))]
    maxdeviation = max(abs(len(data1["BROOKLYN"][year]) - avg), abs(len(data1["BRONX"][year]) - avg), abs(len(data1["MANHATTAN"][year]) - avg), abs(len(data1["QUEENS"][year]) - avg), abs(len(data1["STATEN ISLAND"][year]) - avg))
    maxB = tempList[[abs(len(data1["BROOKLYN"][year]) - avg), abs(len(data1["BRONX"][year]) - avg), abs(len(data1["MANHATTAN"][year]) - avg), abs(len(data1["QUEENS"][year]) - avg), abs(len(data1["STATEN ISLAND"][year]) - avg)].index(maxdeviation)]
    mindeviation  = min(abs(len(data1["BROOKLYN"][year]) - avg), abs(len(data1["BRONX"][year]) - avg), abs(len(data1["MANHATTAN"][year]) - avg), abs(len(data1["QUEENS"][year]) - avg), abs(len(data1["STATEN ISLAND"][year]) - avg))
    minB = tempList[[abs(len(data1["BROOKLYN"][year]) - avg), abs(len(data1["BRONX"][year]) - avg), abs(len(data1["MANHATTAN"][year]) - avg), abs(len(data1["QUEENS"][year]) - avg), abs(len(data1["STATEN ISLAND"][year]) - avg)].index(mindeviation)]
    return render_template("micro.html", lowB = minB,highB = maxB, maxDeviation = int(maxdeviation), minDeviation = int(mindeviation), avg= average, yr = year, min = minimum, max = maximum, quColor = quColor, bkColor = bkColor, bxColor = bxColor, maColor = maColor, siColor = siColor, eight = Eight, sixteen = Sixteen, twentyfour = Twentyfour, thirtytwo = Thirtytwo, forty = Forty)
    
if __name__ == "__main__":
    app.run(debug=True)
