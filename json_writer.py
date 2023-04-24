import json
import Outliers as plo

output_file = "Pm25_outliers.json"

# Write the dictionary of dictionaries to the JSON file
with open(output_file, "w") as file:
    json.dump(plo.Pm25_outliers, file, indent=4)
