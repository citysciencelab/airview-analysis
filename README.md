# Project Air View Hamburg

![Project Air View car](https://www.hcu-hamburg.de/fileadmin/_processed_/2/c/csm_AAA_google_841208530f.jpg)

## Project Description
Air pollution is considered one of the largest environmental health impacts, with outdoor air pollution causing more than 4.2 million premature deaths worldwide each year. Air quality can vary within city districts and even within street sections. Project Air View in Hamburg is a scientific project of Google and HafenCity University (HCU) / City Scienece Lab (CSL) to measure, map, and publish hyperlocal air quality data in Hamburg. Project Air View uses an all-electric vehicle equipped with air quality sensors to measure fine particulate matter (PM 2.5), nitric oxide(NO), nitrogen dioxide (NO2), carbon monoxide (CO), carbon dioxide (CO2), and ozone (O3), which are harmful to both our climate and human health. 


## Discussion Paper (german)
The [discussion paper](https://repos.hcu-hamburg.de/handle/hcu/976) (DOI: 10.34712/142.50) summarizes the research results of the City Science Lab (CSL) at HafenCity University on Project Air View Hamburg. It was prepared on the occasion of the presentation of the data collected by Google on air quality in Hamburg on June 13, 2023 in order to provide scientific information to the interested public. Central points of the discussion paper are the explanation of the project background and the research method, urban planning considerations based on the processed data, possible use case for urban and transportation planning as well as the identification of different potentials of the measurement method.

## Raw Data
It contains the [air quality data](https://repos.hcu-hamburg.de/handle/hcu/893) (DOI: 10.34712/042.1) measured by Google as part of Project Air View. According to Google, it contains 23 million data points from over 2 million measurement locations. The measured substances are CO, CO2, NO2, NO, O3, as well as six channels for particulate matter PM2.5. PM2.5 was also calculated as a total value. The data was subjected to a quality check by the manufacturer of the sensors, Aclima, after each sampling. The data is available as 1-second point data and as lines aggregated to 50 meter long road segments. Both formats are available as CSV and GeoJSON files and are specified in the measurement units ppb and μ/m³. The data contains information on the time of measurement and velocity, among other things. Further information and the description of the column name can be found in the .txt files. An additional metadata description can be found [here](https://aclima.docsend.com/view/e5jdrrkfnway7rj2). The CSV files can be converted into shape files using Python and the GeoPandas library, for example.

## airview-analysis
Working repository for the AirView project. 
To run the code above:
1. Have the csv data in the data folder. 
2. Running csv_reader.py will read in the NO2 measurements from the latest csv file provided by Google and write 
them out (along with their location and unique time stamp) to a json file. This json file will be used for the general 
statistic analysis. 
3. Running Unittests.py will test: the csv data (if the time stamps of each measurement are unique and if the entries 
in the csv file match the json file entries).

