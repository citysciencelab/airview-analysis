import json
import pandas as pd

data_NO2 = {}
data_O3 = {}
data_CO = {}
data_CO2 = {}
data_Pm25 = {}


df = pd.read_csv('data/Hamburg_mobile_pivot_2023-03-27.csv')

for index, row in df.iterrows():
    if pd.notna(float(row[5])):  # check if the NO2 column has values
        # add the row to the dictionary
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_NO2[key] = {'NO2': float(row[5]), 'location': row[3]}
    if pd.notna(float(row[6])):  # check if the O3 column has values
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_O3[key] = {'O3': float(row[6]), 'location': row[3]}
    if pd.notna(float(row[7])):  # check if the CO column has values
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_CO[key] = {'CO': float(row[7]), 'location': row[3]}
    if pd.notna(float(row[8])):  # check if the CO2 column has values
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_CO2[key] = {'CO2': float(row[8]), 'location': row[3]}
    if pd.notna(float(row[15])):  # check if the PM2.5 column has values
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_Pm25[key] = {'Pm25': float(row[15]), 'location': row[3]}

# write the NO2 dictionary to a JSON file
with open('General_NO2.json', 'w') as outfile:
    json.dump(data_NO2, outfile)

# write the CO dictionary to a JSON file
with open('General_O3.json', 'w') as outfile:
    json.dump(data_O3, outfile)

# write the CO dictionary to a JSON file
with open('General_CO.json', 'w') as outfile:
    json.dump(data_CO, outfile)

# write the CO dictionary to a JSON file
with open('General_CO2.json', 'w') as outfile:
    json.dump(data_CO2, outfile)

# write the CO dictionary to a JSON file
with open('General_Pm25.json', 'w') as outfile:
    json.dump(data_Pm25, outfile)
