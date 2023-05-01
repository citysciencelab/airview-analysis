import General_statistics as gs
import measurement_list as ml
import matplotlib.pyplot as plt
import numpy as np

NO2_mes = ml.data_extraction("NO2")
CO_mes = ml.data_extraction("CO")
CO2_mes = ml.data_extraction("CO2")
Pm25_mes = ml.data_extraction("Pm25")

#NO2_data_without_outliers = ml.data_without_outliers(NO2_mes, gs.NO2_lower_wisker, gs.NO2_upper_wisker)[0]
#CO2_data_without_outliers = ml.data_without_outliers(CO2_mes, gs.CO2_lower_whisker, gs.CO2_upper_whisker)[0]
#CO_data_without_outliers = ml.data_without_outliers(CO_mes, gs.CO_lower_whisker, gs.CO_upper_whisker)[0]
Pm25_data_without_outliers = ml.data_without_outliers(Pm25_mes, gs.Pm25_lower_whisker, gs.Pm25_upper_whisker)[0]
print("length data without outliers: ", len(Pm25_data_without_outliers))

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
