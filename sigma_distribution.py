import measurement_list as ml
import matplotlib.pyplot as plt
import numpy as np

NO2_mes = ml.data_extraction("NO2")
CO_mes = ml.data_extraction("CO")
CO2_mes = ml.data_extraction("CO2")
Pm25_mes = ml.data_extraction("Pm25")

NO2_lower_wisker = 4.6  # VOD in ppb
NO2_upper_wisker = 500  # https://www.epa.gov/no2-pollution/primary-national-ambient-air-quality-standards-naaqs-nitrogen-dioxide - 100 ppb
CO_lower_whisker = 0.028  # VOD in ppm
CO_upper_whisker = 50  # EPA.gov, https://www.cdc.gov/niosh/docs/81-123/pdfs/0105.pdf
CO2_lower_whisker = 2.4  # VOD in ppm
CO2_upper_whisker = 1800  # heimantech.com
Pm25_lower_whisker = 1.6  # VOD in microg/m3
Pm25_upper_whisker = 300  # epa.vic.gov.au -75 bad for health - 300 extremely poor for 1h

NO2_data_without_outliers = ml.data_without_outliers(NO2_mes, NO2_lower_wisker, NO2_upper_wisker)
CO2_data_without_outliers = ml.data_without_outliers(CO2_mes, CO2_lower_whisker, CO2_upper_whisker)
CO_data_without_outliers = ml.data_without_outliers(CO_mes, CO_lower_whisker, CO_upper_whisker)
Pm25_data_without_outliers = ml.data_without_outliers(Pm25_mes, Pm25_lower_whisker, Pm25_upper_whisker)

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_standard_deviation(data, mean):
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / (len(data) - 1)
    return np.sqrt(variance)

def calculate_mean_plus_minus_sigma(mean, std_dev):
    lower_bound = mean - std_dev
    upper_bound = mean + std_dev
    return lower_bound, upper_bound

data = Pm25_data_without_outliers

mean = calculate_mean(data)
std_dev = calculate_standard_deviation(data, mean)
lower_bound, upper_bound = calculate_mean_plus_minus_sigma(mean, std_dev)

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Mean ± Sigma Range:", lower_bound, "to", upper_bound)

# Create histogram
plt.hist(data, bins='auto', alpha=0.75, color='blue', edgecolor='black')
plt.xlabel('PM2.5 (\u03BCg/m3)')
plt.ylabel('Frequency')
plt.title('Histogram with Mean and ± Sigma Range')

# Add vertical lines for mean, lower_bound, and upper_bound
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(lower_bound, color='green', linestyle='dashed', linewidth=2, label='Mean - σ')
plt.axvline(upper_bound, color='orange', linestyle='dashed', linewidth=2, label='Mean + σ')

# Add legend
plt.legend(loc='upper right')

# Display plot
plt.show()
