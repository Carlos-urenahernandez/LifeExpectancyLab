import json

with open("Data/data_original.csv", "r") as f1:
    lines = f1.readlines()
data = {}
for line in lines:
    line = line.strip()
    borough = line.split(",")[0]
    date = line.split(",")[1]
    if borough not in data:
         data[borough] = {}
    if date[-4:] not in data[borough]:
        data[borough][str(date[-4:])] = []
    data[borough][str(date[-4:])].append(line)
for borough in data:
    for year in data[borough]:
        print(f"{borough} {year} {len(data[borough][year])} <- this vale is what u wanted ")
with open("Data/data.json", "w") as f2:
   json.dump(data, f2, indent=4)
