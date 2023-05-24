import datetime
import json
import matplotlib.pyplot as plt

with open("qID_CO.json", 'r') as infile:
    qID_CO_data = json.load(infile)

with open("qID_CO2.json", 'r') as infile:
    qID_CO2_data = json.load(infile)

with open("qID_NO.json", 'r') as infile:
    qID_NO_data = json.load(infile)

with open("qID_NO2.json", 'r') as infile:
    qID_NO2_data = json.load(infile)

with open("qID_O3.json", 'r') as infile:
    qID_O3_data = json.load(infile)

with open("qID_NO2.json", 'r') as infile:
    qID_Pm25_data = json.load(infile)

valid_IDs = [510, 511, 544, 676]

def get_keys_above_value(dictionary, qID, threshold):
    keys_above_value = []
    for key, value in dictionary.items():
        if "qID" in value and "value" in value:
            if value["qID"] == qID and value["value"] > threshold:
                keys_above_value.append(key)
    return keys_above_value

qID = 676

co_3s_limit = 0.55
co2_3s_limit = 506.73
no_3s_limit = 0.55
no2_3s_limit = 33.2
o3_3s_limit = 36.97
pm25_3s_limit = 24.01

CO_date_string = get_keys_above_value(qID_CO_data, qID, co_3s_limit)
CO2_date_string = get_keys_above_value(qID_CO2_data, qID, co2_3s_limit)
NO_date_string = get_keys_above_value(qID_NO_data, qID, no_3s_limit)
NO2_date_string = get_keys_above_value(qID_NO2_data, qID, no2_3s_limit)
O3_date_string = get_keys_above_value(qID_O3_data, qID, o3_3s_limit)
Pm25_date_string = get_keys_above_value(qID_Pm25_data, qID, pm25_3s_limit)

# Extract date part from strings
CO_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in CO_date_string]
CO_unique_dates = list(set(CO_dates))

CO2_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in CO2_date_string]
CO2_unique_dates = list(set(CO2_dates))

NO_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in NO_date_string]
NO_unique_dates = list(set(NO_dates))

NO2_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in NO2_date_string]
NO2_unique_dates = list(set(NO2_dates))

O3_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in O3_date_string]
O3_unique_dates = list(set(O3_dates))

Pm25_dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %Z").date() for date_string in Pm25_date_string]
Pm25_unique_dates = list(set(Pm25_dates))

# Sort dates in ascending order
CO_unique_dates.sort()
CO2_unique_dates.sort()
NO_unique_dates.sort()
NO2_unique_dates.sort()
O3_unique_dates.sort()
Pm25_unique_dates.sort()

fig, ax = plt.subplots(figsize=(8, 6))

# Plotting
ax.plot(CO_unique_dates, [1] * len(CO_unique_dates), 'bo', label='CO mes.')
ax.plot(CO2_unique_dates, [1.1] * len(CO2_unique_dates), 'ro', label='CO2 mes.')
ax.plot(NO_unique_dates, [1.2] * len(NO_unique_dates), 'go', label='NO mes.')
ax.plot(NO2_unique_dates, [1.3] * len(NO2_unique_dates), 'co', label='NO2 mes.')
ax.plot(O3_unique_dates, [1.4] * len(O3_unique_dates), 'yo', label='O3 mes.')
ax.plot(Pm25_unique_dates, [1.5] * len(Pm25_unique_dates), 'mo', label='Pm25 mes.')

plt.yticks([])
plt.xlabel('Date')
plt.title('Calendar Plot for Area ' + str(qID))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.subplots_adjust(right=0.8)
plt.show()