# airview-analysis
Working repository for the AirView project

1. Have the csv data in the data folder. 
2. Running csv_reader.py will read in the NO2 measurements from the latest csv file provided by Google and write 
them out (along with their location and unique time stamp) to a json file. This json file will be used for the general 
statistic analysis. 
3. Running Unittests.py will test: the csv data (if the time stamps of each measurement are unique and if the entries 
in the csv file match the json file entries).

