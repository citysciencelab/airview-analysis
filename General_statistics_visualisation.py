import matplotlib.pyplot as plt
import measurement_list as ml
import numpy as np

NO2_mes = ml.data_extraction("NO2")

print("------- info about the NO2 data -----------")
print("Length of the NO2 measurement list:", len(NO2_mes))
print("Maximum NO2 value", max(NO2_mes))
print("Minimum NO2 value", min(NO2_mes))


# Create a histogram with 50 bins and labeled x-axis ticks
fig, ax = plt.subplots()
n, bins, patches = ax.hist(NO2_mes, bins=40, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Measurement')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of NO2 Measurements')

# Label the x-axis ticks with the bin edges
bin_centers = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(bin_centers)
ax.set_xticklabels([f'{val:.2f}' for val in bin_centers], rotation=45, ha='right')

# Display the plot
plt.show()
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