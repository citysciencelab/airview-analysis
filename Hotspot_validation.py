import json
import matplotlib.pyplot as plt
import numpy as np

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

dummy_data = {"2021-10-05 08:54:51 UTC": {"qID": 1, "value": 0.3},
              "2021-10-05 09:00:02 UTC": {"qID": 2, "value": 0},
              "2021-10-05 08:54:57 UTC": {"qID": 1, "value": 4},
              "2021-10-05 08:56:23 UTC": {"qID": 3, "value": 3},
              "2021-10-05 08:57:38 UTC": {"qID": 2, "value": 1},
              "2021-10-05 09:01:02 UTC": {"qID": 4, "value": -7},
              "2021-10-05 08:59:48 UTC": {"qID": 2, "value": 2.001},
              "2021-10-05 09:03:54 UTC": {"qID": 3, "value": 5},
              "2021-10-05 08:54:37 UTC": {"qID": 4, "value": 0}}

co_3s_limit = 0.55
co2_3s_limit = 506.73
no_3s_limit = 0.55
no2_3s_limit = 33.2
o3_3s_limit = 36.97
pm25_3s_limit = 24.01
dummy_limit = 2

def qID_counts(data, three_sigma_limit):
    counts = {}

    for entry in data.values():
        qID = entry["qID"]
        value = entry["value"]

        if qID not in counts:
            counts[qID] = {"above": 0, "below": 0}

        if value > three_sigma_limit:
            counts[qID]["above"] += 1
        else:
            counts[qID]["below"] += 1

    return counts

CO_counts = qID_counts(qID_CO_data, co_3s_limit)
CO2_counts = qID_counts(qID_CO2_data, co2_3s_limit)
NO2_counts = qID_counts(qID_NO2_data, no2_3s_limit)
O3_counts = qID_counts(qID_O3_data, o3_3s_limit)
Pm25_counts = qID_counts(qID_Pm25_data, pm25_3s_limit)
dummy_counts = qID_counts(dummy_data, dummy_limit)
#print(dummy_counts)

def above_three_sigma_ercentages(counts):
    percentages = {}
    totals = {}

    for qID, count in counts.items():
        total = count["above"] + count["below"]
        totals[qID] = total
        above_percentage = (count["above"] / total) * 100
        percentages[qID] = above_percentage

    return percentages, totals

CO_percentages_id, CO_totals = above_three_sigma_ercentages(CO_counts)
CO2_percentages_id, CO2_totals = above_three_sigma_ercentages(CO2_counts)
NO2_percentages_id, NO2_totals = above_three_sigma_ercentages(NO2_counts)
O3_percentages_id, O3_totals = above_three_sigma_ercentages(O3_counts)
Pm25_percentages_id, Pm25_totals = above_three_sigma_ercentages(Pm25_counts)
dummy_percentage_id, dummy_totals = above_three_sigma_ercentages(dummy_counts)
#print(dummy_percentage_id)
#print(dummy_totals)

def apply_limits_on_measurement_counts_and_outlier_percentages(dict_counts, dict_per, count_limit, per_limit):
    qID_above_countlimit_percentagelimit = [key for key, value in dict_per.items() if value >= per_limit and dict_counts.get(key, 0) >= count_limit]
    return qID_above_countlimit_percentagelimit

count_limit_per_ID = 10000
percentage_per_ID = 12

CO_qIDs = apply_limits_on_measurement_counts_and_outlier_percentages(CO_totals, CO_percentages_id, count_limit_per_ID, percentage_per_ID)
print(CO_qIDs)
CO2_qIDs = apply_limits_on_measurement_counts_and_outlier_percentages(CO2_totals, CO2_percentages_id, count_limit_per_ID, percentage_per_ID)
print(CO2_qIDs)
NO2_qIDs = apply_limits_on_measurement_counts_and_outlier_percentages(NO2_totals, NO2_percentages_id, count_limit_per_ID, percentage_per_ID)
print(NO2_qIDs)
Pm25_qIDs = apply_limits_on_measurement_counts_and_outlier_percentages(Pm25_totals, Pm25_percentages_id, count_limit_per_ID, percentage_per_ID)
print(Pm25_qIDs)

'''
def hystogram(percentages, sp):
    sorted_qIDs = sorted(percentages.keys())  # Sort qIDs in ascending order
    sorted_percentages = [percentages[qID] for qID in sorted_qIDs]  # Get corresponding percentages

    plt.bar(sorted_qIDs, sorted_percentages)
    plt.xlabel('qIDs')
    plt.ylabel(sp + ' Percentage above 3 sigma')
    plt.title(sp + ' Percentage of Values Above 3 sigma for Each qID')
    return plt

#hystogram(C0_percentages_id, "CO").savefig("CO_qID_hystogram")
#hystogram(C02_percentages_id, "CO2").savefig("CO2_qID_hystogram")
#hystogram(NO2_percentages_id, "NO2").savefig("NO2_qID_hystogram")
#hystogram(O3_percentages_id, "O3").savefig("O3_qID_hystogram")
#hystogram(Pm25_percentages_id, "PM2.5").savefig("PM25_qID_hystogram")


def qID_with_percentages_above_limit(data, limit):
    keys_above_limit = [key for key, value in data.items() if value >= limit]
    return keys_above_limit


CO_array = qID_with_percentages_above_limit(CO_percentages_id, 33.33)
CO2_array = qID_with_percentages_above_limit(CO2_percentages_id, 33.33)
NO2_array = qID_with_percentages_above_limit(NO2_percentages_id, 33.33)
O3_array = qID_with_percentages_above_limit(O3_percentages_id, 33.33)
Pm25_array = qID_with_percentages_above_limit(Pm25_percentages_id, 33.33)
'''
def find_common_items(arrays):
    common_items = set(arrays[0])

    for array in arrays[1:]:
        common_items = common_items.intersection(array)

    return list(common_items)


arrays = [CO_qIDs, CO2_qIDs, NO2_qIDs, Pm25_qIDs]

common_items = find_common_items(arrays)
print("Common items: ", common_items)

'''
measurements = list(Pm25_totals.values())

bin_edges = np.arange(0, 20000 + 101, 100)

plt.hist(measurements, bins=bin_edges)
plt.xlabel('Number of Measurements')
plt.ylabel('Frequency')
plt.title('Distribution of Measurements')
plt.show()

'''