import pandas as pd

data = {}

df = pd.read_csv('data/Hamburg_mobile_pivot_2022-09-22.csv')

for index, row in df.iterrows():
    if pd.notna(row[5]) and pd.notna(row[6]):  # check if both columns have values
        # add the row to the dictionary
        key = row[2]  # use the third column as the key
        data[key] = {'column_4': row[3], 'column_6': row[5], 'column_7': row[6]}

# print the dictionary
print(df.size)

