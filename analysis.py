import json
import pandas as pd

data = {}

df = pd.read_csv('data/Hamburg_mobile_pivot_2022-09-22.csv')

for index, row in df.iterrows():
    if pd.notna(row[5]) and pd.notna(row[6]):  # check if both columns have values
        # add the row to the dictionary
        key = row[2]  # use the third column as the key
        data[key] = {'loc': row[3], 'NO2': row[5], 'O3': row[6]}

# write the dictionary to a JSON file
with open('NO2-O3.json', 'w') as outfile:
    json.dump(data, outfile)

