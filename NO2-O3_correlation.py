import json

with open('NO2-O3.json', 'r') as infile:
    data = json.load(infile)

print(data)
