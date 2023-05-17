import matplotlib.pyplot as plt
import measurement_list as ml
import numpy as np
import seaborn as sns

'''
NO_mes = ml.data_extraction("NO")
NO2_mes = ml.data_extraction("NO2")
O3_mes = ml.data_extraction("O3")
CO_mes = ml.data_extraction("CO")
CO2_mes = ml.data_extraction("CO2")
Pm25_mes = ml.data_extraction("Pm25")


print("------- general info about the data -----------")

print("Length of the NO measurement list:", len(NO_mes))
print("Maximum NO value", max(NO_mes))
print("Minimum NO value", min(NO_mes))
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

print("-------------------------------")


#--------------- Upper wiskets defined ------------------------

NO_lower_wisker = 15.6  # VOD in ppb
NO_upper_wisker = 3*100   # like NO2 (usually given as NOx)
NO2_lower_wisker = 4.6  # VOD in ppb
NO2_upper_wisker = 3*100  # https://www.epa.gov/no2-pollution/primary-national-ambient-air-quality-standards-naaqs-nitrogen-dioxide - 100 ppb
O3_lower_wisker = 3     # VOD in ppb
O3_upper_wisker = 70  # ppb from https://en.air-q.com/grenzwerte - alarming values for 1h (can be reduced to 70 https://www.epa.gov/sites/default/files/2016-04/documents/20151001basicsfs.pdf)
CO_lower_whisker = 0.028  # VOD in ppm
CO_upper_whisker = 9  # EPA.gov, 35/50 ppm https://www.cdc.gov/niosh/docs/81-123/pdfs/0105.pdf, https://www.co2meter.com/blogs/news/carbon-monoxide-levels-chart
CO2_lower_whisker = 2.4  # VOD in ppm
CO2_upper_whisker = 1000  # https://www.dhs.wisconsin.gov/chemical/carbondioxide.htm#:~:text=The%20levels%20of%20CO2,of%20drowsiness%20and%20poor%20air.
Pm25_lower_whisker = 1.6  # VOD in microg/m3
Pm25_upper_whisker = 300  # epa.vic.gov.au -75 bad for health - 300 extremely poor for 1h
'''

#----------------- Upper wiskers calculated ---------------

NO_lower_wisker = 15.6  # VOD in ppb
NO_upper_wisker = 300   # the value is irrelevant
NO2_lower_wisker = 4.6  # VOD in ppb
NO2_upper_wisker = 28.86
O3_lower_wisker = 3     # VOD in ppb
O3_upper_wisker = 29.36
CO_lower_whisker = 0.028  # VOD in ppm
CO_upper_whisker = 0.58
CO2_lower_whisker = 2.4  # VOD in ppm
CO2_upper_whisker = 487.1
Pm25_lower_whisker = 1.6  # VOD in microg/m3
Pm25_upper_whisker = 20.9

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
print("Info: NO2")
print("% of negative data: ", negative_per(NO2_mes))
print("% of under LOD data: ", under_LOD_per(NO2_mes, NO2_lower_wisker))
print("Info: O3")
print("% of negative data: ", negative_per(O3_mes))
print("% of under LOD data: ", under_LOD_per(O3_mes, O3_lower_wisker))
print("Info: CO")
print("% of negative data: ", negative_per(CO_mes))
print("% of under LOD data: ", under_LOD_per(CO_mes, CO_lower_whisker))
print("Info: CO2")
print("% of negative data: ", negative_per(CO2_mes))
print("% of under LOD data: ", under_LOD_per(CO2_mes, CO2_lower_whisker))
print("Info: PM2.5")
print("% of negative data: ", negative_per(Pm25_mes))
print("% of under LOD data: ", under_LOD_per(Pm25_mes, Pm25_lower_whisker))
#----------------------------------- BOX PLOTS -----------------------------------


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