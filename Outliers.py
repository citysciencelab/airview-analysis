import json
import measurement_list as ml

Pm25_lower_whisker = 1.6  # VOD in microg/m3
Pm25_upper_whisker = 300  # epa.vic.gov.au -75 bad for health - 300 extremely poor for 1h

with open("Pm25_short_data.json", 'r') as infile:
    Pm25_data = json.load(infile)

print(type(Pm25_data))
print("Total length of data: ", len(Pm25_data))

target_value = Pm25_upper_whisker

Pm25_outliers = ml.find_outliers(Pm25_data, Pm25_lower_whisker, Pm25_upper_whisker)

print("length of outliers", len(Pm25_outliers))

print("--------test: -----------------")

datapoints = [d['Pm25'] for d in Pm25_data.values()]
pm_list = []

# make sure the data is of type float
for n in datapoints:
    pm_list.append((float(n)))

test_data_no, test_data_o = ml.data_without_outliers(pm_list, Pm25_lower_whisker, Pm25_upper_whisker)

print(len(test_data_no), len(test_data_o))
