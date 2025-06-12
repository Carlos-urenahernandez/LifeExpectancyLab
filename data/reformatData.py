import json

with open("Life_Expectancy_Data_cleansed.csv", "r") as f1:
    lines = f1.readlines()
countries = {}
years = [str(year) for year in range(1960, 2023)]

for line in lines:
    currentLine = line.split(",")
    countries[currentLine[0]] = {}
    for i in range(len(years)):
        countries[currentLine[0]][years[i]] = float(currentLine[i+1])

with open("life_expectancy.json", "w") as f2:
    json.dump(countries, f2, indent=4)