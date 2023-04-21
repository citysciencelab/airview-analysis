import json


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

def data_extraction(sp, file_name):

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

    if min(data) > high_w:
        print("The upper wisker is not realistic for the given data set!")
    elif max(data) < low_w:
        print("The lower wisker is not realistic for the given data set!")
    else:
        for v in data:
            if v >= low_w and v <= high_w:
                data_without_outliers.append(v)

    if len(data_without_outliers) == 0:
        print("There is no data within the proposed limits!")
    else:
        print("len data without outliers: ", len(data_without_outliers))
        print("max in data without outliers: ", max(data_without_outliers))
        print("min in data without outliers: ", min(data_without_outliers))

    return data_without_outliers








