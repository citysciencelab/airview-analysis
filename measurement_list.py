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








