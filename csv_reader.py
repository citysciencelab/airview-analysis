import json
import pandas as pd

data = {}

df = pd.read_csv('data/Hamburg_mobile_pivot_2023-03-27.csv')

for index, row in df.iterrows():
    if pd.notna(float(row[5])):  # check if the NO2 column has values
        # add the row to the dictionary
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data[key] = {'NO2': float(row[5]), 'location': row[3]}

# write the dictionary to a JSON file
with open('General_NO2.json', 'w') as outfile:
    json.dump(data, outfile)

