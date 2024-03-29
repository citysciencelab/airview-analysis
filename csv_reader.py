import json
import pandas as pd

data_NO = {}
data_NO2 = {}
data_O3 = {}
data_CO = {}
data_CO2 = {}
data_Pm25 = {}

df = pd.read_csv('data/Hamburg_mobile_pivot_2023-03-27.csv')

for index, row in df.iterrows():
    if pd.notna(float(row[4])):  # check if the NO column has values
        key = row[2]  # use the GPS timestamp column as the key - because it is unique
        data_NO[key] = {'NO': float(row[4]), 'location': row[3]}
    if pd.notna(float(row[5])):  # check if the NO2 column has values
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

# write the NO dictionary to a JSON file
with open('General_NO.json', 'w') as outfile:
    json.dump(data_NO, outfile)

# write the NO2 dictionary to a JSON file
with open('General_NO2.json', 'w') as outfile:
    json.dump(data_NO2, outfile)

# write the O3 dictionary to a JSON file
with open('General_O3.json', 'w') as outfile:
    json.dump(data_O3, outfile)

# write the CO dictionary to a JSON file
with open('General_CO.json', 'w') as outfile:
    json.dump(data_CO, outfile)

# write the CO2 dictionary to a JSON file
with open('General_CO2.json', 'w') as outfile:
    json.dump(data_CO2, outfile)

# write the PM2.5 dictionary to a JSON file
with open('General_Pm25.json', 'w') as outfile:
    json.dump(data_Pm25, outfile)

#--------------- for short outlier overview ----------------------------------------
df = pd.read_csv('data/Hamburg_mobile_pivot_2023-03-27.csv')

Pm25_short_data = {}

for index, row in df.iterrows():
    if pd.notna(float(row[15])):  # check if the PM2.5 column has values
        key = row[3]  # use the GPS timestamp column as the key - because it is unique
        Pm25_short_data[key] = {'Pm25': float(row[15])}

with open('Pm25_short_data.json', 'w') as outfile:
    json.dump(Pm25_short_data, outfile)

#--------------- Reading road segments in ----------------------------------------

df_split = pd.read_csv('data/ham_roads_split50flt_data_2023-03-27.csv')

Pm25_segments = {}

for index, row in df_split.iterrows():
    if pd.notna(float(row[136])) and float(row[139]) >= 6:  # check if the PM2.5 column has values and if the segment was visited more than 6 times
        key = row[2]  # use the coordinate column as the key - because it is unique
        Pm25_segments[key] = {'Pm25med_4hours': float(row[144])}

with open('Pm25_segments.json', 'w') as outfile:
    json.dump(Pm25_segments, outfile)

#------------------------------ Grid segment IDs --------------------------------

qID_NO = {}
qID_NO2 = {}
qID_O3 = {}
qID_CO = {}
qID_CO2 = {}
qID_Pm25 = {}

df = pd.read_csv('data/output_500m_pm25.csv')

for index, row in df.iterrows():
    key = row[3]  # use the GPS timestamp column as the key - because it is unique
    qID_Pm25[key] = {'qID': float(row[0]), 'value': float(row[2])}

# write the PM2.5 dictionary with qID to a JSON file
with open('qID_Pm25.json', 'w') as outfile:
    json.dump(qID_Pm25, outfile)

print(len(qID_Pm25))