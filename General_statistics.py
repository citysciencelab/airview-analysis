import matplotlib.pyplot as plt
import measurement_list as ml
import numpy as np
import seaborn as sns

NO_mes = ml.data_extraction("NO")
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

NO_lower_wisker = 15.6  # VOD in ppb
NO2_lower_wisker = 4.6  # VOD in ppb
NO2_upper_wisker = 500  # https://www.epa.gov/no2-pollution/primary-national-ambient-air-quality-standards-naaqs-nitrogen-dioxide - 100 ppb
CO_lower_whisker = 0.028  # VOD in ppm
CO_upper_whisker = 50  # EPA.gov, https://www.cdc.gov/niosh/docs/81-123/pdfs/0105.pdf
CO2_lower_whisker = 2.4  # VOD in ppm
CO2_upper_whisker = 1800  # heimantech.com
Pm25_lower_whisker = 1.6  # VOD in microg/m3
Pm25_upper_whisker = 300  # epa.vic.gov.au -75 bad for health - 300 extremely poor for 1h

'''
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

def negative_per(data):

    neg_count = 0 #counter for negative values

    for v in data:
        if v < 0:
            neg_count = neg_count + 1

    negative_value_percentage = (neg_count * 100)/len(data)
    return negative_value_percentage

def under_LOD_per(data, lod):

    uLOD_count = 0  # counter for negative values

    for v in data:
        if v < lod:
            uLOD_count = uLOD_count + 1

    uLOD_value_percentage = (uLOD_count * 100) / len(data)
    return uLOD_value_percentage

print("Info: NO")
print("Total length of data: ", len(NO_mes))
print("% of negative data: ", negative_per(NO_mes))
print("% of under LOD data: ", under_LOD_per(NO_mes, NO_lower_wisker))

#----------------------------------- BOX PLOTS -----------------------------------

'''
# Create some example data
data = CO_mes

data = np.random.choice(CO_mes, size=20000, replace=False)

# Calculate some summary statistics
mean = np.mean(data)
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
upper_whisker = 4
lower_whisker = 0.028

# Create the bee swarm plot
sns.swarmplot(data=data, size=1, color='k')

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
'''