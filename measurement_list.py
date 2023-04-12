import json


# read the data from the general Json file
with open('General_NO2.json', 'r') as infile:
    NO2_data = json.load(infile)

# Extract the 'NO2' field from each dictionary and save them in a NumPy array
NO2_datapoints = [d['NO2'] for d in NO2_data.values()]

NO2 = []

# make sure the data is of type float
for n in NO2_datapoints:
    NO2.append(float(n))








