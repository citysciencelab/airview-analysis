import unittest
import json
import pandas as pd

class TestCalculateStatistics(unittest.TestCase):

    def test_csv_reader(self):

        df = pd.read_csv('data/Hamburg_mobile_pivot_2023-03-27.csv')
        data = {}

        with open('General_NO2.json', 'r') as infile:
            dataIn = json.load(infile)

        for index, row in df.iterrows():
            if pd.notna(float(row[5])):  # check if the NO2 column has values
                # add the row to the dictionary
                key = row[2]  # use the GPS timestamp column as the key - because it is unique
                if key in data:
                    # test if the time stamps are unique
                    self.assertRaises("TIMESTAMP IS NOT UNIQUE", key)
                data[key] = {'NO2': float(row[5]), 'location': row[3]}
                if dataIn[key] != data[key]:
                    # test if the entries in the csv file match the json file entries
                    self.assertRaises("ENTRY DOES NOT MATCH", key, dataIn[key], data[key])


if __name__ == '__main__':
    unittest.main()