import General_statistics as gs
import json_writer as jw
import measurement_list as ml
import json

#------------------------ from short json file, with test-----------------

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

#------------------------------- OUTLIERS with location and time stamp + test -----------------------


NO_dict = ml.data_in_dictionary("NO")
outl_NO = ml.upper_outliers_from_dictionary("NO", NO_dict, gs.NO_upper_wisker)
jw.write_out("NO", outl_NO)

NO2_dict = ml.data_in_dictionary("NO2")
outl_NO2 = ml.upper_outliers_from_dictionary("NO2", NO2_dict, gs.NO2_upper_wisker)
jw.write_out("NO2", outl_NO2)

O3_dict = ml.data_in_dictionary("O3")
outl_O3 = ml.upper_outliers_from_dictionary("O3", O3_dict, gs.O3_upper_wisker)
jw.write_out("O3", outl_O3)

CO_dict = ml.data_in_dictionary("CO")
outl_CO = ml.upper_outliers_from_dictionary("CO", CO_dict, gs.CO_upper_whisker)
jw.write_out("CO", outl_CO)

CO2_dict = ml.data_in_dictionary("CO2")
outl_CO2 = ml.upper_outliers_from_dictionary("CO2", CO2_dict, gs.CO2_upper_whisker)
jw.write_out("CO2", outl_CO2)

Pm25_dict = ml.data_in_dictionary("Pm25")
outl_Pm25 = ml.upper_outliers_from_dictionary("Pm25", Pm25_dict, gs.Pm25_upper_whisker)
jw.write_out("Pm25", outl_Pm25)

#TODO: possible hot spots

