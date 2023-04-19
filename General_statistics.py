import matplotlib.pyplot as plt
import measurement_list as ml
import numpy as np
import seaborn as sns

NO2_mes = ml.data_extraction("NO2")
O3_mes = ml.data_extraction("O3")
CO_mes = ml.data_extraction("CO")
CO2_mes = ml.data_extraction("CO2")
Pm25_mes = ml.data_extraction("Pm25")

'''

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
#------------------------------- DATA POSTPROCESSING ----------------

#CO

CO_neg_count = 0 #counter for negative values

for v in CO_mes:
    if v < 0:
        CO_neg_count = CO_neg_count + 1

CO_negative_value_percentage = (CO_neg_count * 100)/len(CO_mes)

print("CO_neg_count: ", CO_neg_count)
print(len(CO_mes))
print("CO_negative_value_percentage: ", CO_negative_value_percentage)

#----------------------------------- BOX PLOTS -----------------------------------


'''
# Sample data
data = CO_mes

# Calculate quartiles
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# Calculate lower and upper bounds
lower_bound = 0.028 #q1 - k * iqr
upper_bound = 9 #q3 + k * iqr
'''

# Create some example data
data = CO_mes

# Calculate some summary statistics
mean = np.mean(data)
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
upper_whisker = 9
lower_whisker = 0.028

# Create the bee swarm plot
sns.swarmplot(data=data)

# Add a box plot
sns.boxplot(data=data, showcaps=False, whiskerprops={'linewidth':0}, showfliers=False)

# Add the mean, quartiles, and whiskers as lines
plt.axhline(mean, color='r', linestyle='--', label='Mean')
plt.axhline(q1, color='g', linestyle='--', label='First Quartile')
plt.axhline(q3, color='g', linestyle='--', label='Third Quartile')
plt.axhline(upper_whisker, color='k', linestyle='-', label='Upper Whisker')
plt.axhline(lower_whisker, color='k', linestyle='-', label='Lower Whisker')

# Set the plot title and axis labels
plt.title("Bee Swarm Plot with Box Plot")
plt.xlabel("Data Points")
plt.ylabel("Values")

# Add a legend
plt.legend()

# Display the plot
plt.show()
