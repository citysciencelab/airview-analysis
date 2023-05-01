import json

def write_out(sp, data):

    output_file = sp + "_outliers.json"

    # Write the dictionary of dictionaries to the JSON file
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
