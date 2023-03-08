import json
import functions as fn

with open('NO2-O3.json', 'r') as infile:
    data = json.load(infile)


NO2_at_timestamp = {k: v["NO2"] for k, v in data.items()}

print(NO2_at_timestamp["2021-10-26 09:27:10 UTC"])

statistics = fn.calculate_statistics(NO2_at_timestamp)
fn.visualize_statistics(statistics)
