import json

def data_in_dictionary(sp):

    json_file_name = "General_" + sp + ".json"
    data_name = sp + "_data"
    datapoint_name = sp + "_datapoints"

    with open(json_file_name, 'r') as infile:
        data_name = json.load(infile)

    return data_name

def data_extraction(sp):

    json_file_name = "General_" + sp + ".json"
    data_name = sp + "_data"
    datapoint_name = sp + "_datapoints"

    with open(json_file_name, 'r') as infile:
        data_name = json.load(infile)

    datapoint_name = [d[sp] for d in data_name.values()]

    sp = []

    # make sure the data is of type float
    for n in datapoint_name:
        sp.append(float(n))

    return sp

def data_extraction_from_file(sp, file_name):

    field_name = sp + "med_4hours"

    with open(file_name, 'r') as infile:
        data = json.load(infile)

    datapoints = [d[field_name] for d in data.values()]

    sp_med = []

    # make sure the data is of type float
    for n in datapoints:
        sp_med.append(float(n))

    return sp_med


def data_without_outliers(data, low_w, high_w):

    data_without_outliers = []
    outliers = []

    if min(data) > high_w:
        print("The upper wisker is not realistic for the given data set!")
    elif max(data) < low_w:
        print("The lower wisker is not realistic for the given data set!")
    else:
        for v in data:
            if v >= low_w and v <= high_w:
                data_without_outliers.append(v)
            else:
                outliers.append(v)

    if len(data_without_outliers) == 0:
        print("There is no data within the proposed limits!")
    else:
        print("len data without outliers: ", len(data_without_outliers))
        print("max in data without outliers: ", max(data_without_outliers))
        print("min in data without outliers: ", min(data_without_outliers))

    return data_without_outliers, outliers

def find_outliers(input_dict, lower_value, upper_value):

    Outliers = {}

    for outer_key, inner_dict in input_dict.items():
        for inner_key, value in inner_dict.items():
            if float(value) > upper_value or float(value) < lower_value:
                Outliers[outer_key] = inner_dict.copy()
                break

    return Outliers

def upper_outliers_from_dictionary(sp, input_dict, upper_value):

    outliers = {}
    not_outliers = {}

    for key, inner_dict in input_dict.items():
        if float(inner_dict[sp]) > upper_value:
            outliers[key] = inner_dict
        else:
            not_outliers[key] = inner_dict

    if len(not_outliers) + len(outliers) == len(input_dict):
        print("--------- data valid split ------------")
    else:
        print("Check data split!")

    min_value = float("inf")
    max_value = float("-inf")

    print("Number of ",sp, "outliers: ", len(outliers))

    if len(outliers) > 0:
        for inner_dict in outliers.values():
            val = float(inner_dict[sp])
            min_value = min(min_value, val)
            max_value = max(max_value, val)

        print(f"new minimum value: {min_value}")
        print(f"new maximum value: {max_value}")
    else:
        print("Outlier dictionary empty")


    return outliers