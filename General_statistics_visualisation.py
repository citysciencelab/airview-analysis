import matplotlib.pyplot as plt
import measurement_list as ml

NO2_mes = ml.NO2

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

# Adjust the y-axis limits to focus on frequencies above 500
#min_freq = 0
#max_freq = 20000
#if max_freq > min_freq:
#    ax.set_ylim([min_freq, max_freq + 10])
#else:
#    ax.set_ylim([0, max_freq + 10])

# Display the plot
plt.show()
