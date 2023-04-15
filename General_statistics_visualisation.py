import matplotlib.pyplot as plt
import measurement_list as ml
import numpy as np

NO2_mes = ml.data_extraction("NO2")
O3_mes = ml.data_extraction("O3")
CO_mes = ml.data_extraction("CO")
CO2_mes = ml.data_extraction("CO2")
Pm25_mes = ml.data_extraction("Pm25")

print("------- general info about the data -----------")
print("Length of the NO2 measurement list:", len(NO2_mes))
print("Maximum NO2 value", max(NO2_mes))
print("Minimum NO2 value", min(NO2_mes))
print("Length of the O3 measurement list:", len(O3_mes))
print("Maximum O3 value", max(O3_mes))
print("Minimum O3 value", min(O3_mes))
print("Length of the CO measurement list:", len(CO_mes))
print("Maximum CO value", max(CO_mes))
print("Minimum CO value", min(CO_mes))
print("Length of the CO2 measurement list:", len(CO2_mes))
print("Maximum CO2 value", max(CO2_mes))
print("Minimum CO2 value", min(CO2_mes))
print("Length of the Pm25 measurement list:", len(Pm25_mes))
print("Maximum Pm25 value", max(Pm25_mes))
print("Minimum Pm25 value", min(Pm25_mes))

# ------------------------------ HISTOGRAMS -----------------------------------------
# NO2

fig, ax = plt.subplots()
n, bins, patches = ax.hist(NO2_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of NO2 Measurements (ppb)')

bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

fig.savefig('Plots/NO2_histogram.png')

# O3
fig, ax = plt.subplots()
n, bins, patches = ax.hist(O3_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of O3 Measurements (ppb)')

bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

fig.savefig('Plots/O3_histogram.png')

# CO
fig, ax = plt.subplots()
n, bins, patches = ax.hist(CO_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of CO Measurements (ppm)')

bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

fig.savefig('Plots/CO_histogram.png')

# CO2

fig, ax = plt.subplots()
n, bins, patches = ax.hist(CO2_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of CO2 Measurements (ppm)')

bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

fig.savefig('Plots/CO2_histogram.png')

# PM2.5

fig, ax = plt.subplots()
n, bins, patches = ax.hist(Pm25_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of PM2.5 Measurements (\u03BCg/m3)')

bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

fig.savefig('Plots/PM2.5_histogram.png')
'''

def find_outliers(data, multiplier=3):
    q1 = np.percentile(data, 25)
    print(q1)
    q3 = np.percentile(data, 75)
    print(q3)
    iqr = q3 - q1

    lower_bound = q1 - multiplier * iqr
    print(lower_bound)
    upper_bound = q3 + multiplier * iqr
    print(upper_bound)

    outliers = [x for x in data if x < lower_bound or x > upper_bound]

    return outliers, lower_bound, upper_bound


measurements = NO2_mes
outliers, lower_bound, upper_bound = find_outliers(measurements)

#print("Outliers:", outliers)

# Plot the box plot
plt.boxplot(measurements)
plt.title('Box plot of measurements')
plt.ylabel('Value')

# Mark the outliers with red circles
for outlier in outliers:
    plt.plot(1, outlier, 'r', ms=2)

plt.show()
'''