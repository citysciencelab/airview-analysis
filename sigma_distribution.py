import measurement_list as ml
import matplotlib.pyplot as plt
import numpy as np

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

data = ml.data_extraction('CO')

data_short = []

for v in data:
    if v <= 1:
        data_short.append(v)

mean = calculate_mean(data_short)
std_dev = calculate_standard_deviation(data_short, mean)
lower_bound, upper_bound = calculate_mean_plus_minus_sigma(mean, std_dev)

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Mean ± Sigma Range:", lower_bound, "to", upper_bound)


# Create histogram
plt.hist(data_short, bins='auto', alpha=0.75, color='blue', edgecolor='black')
plt.xlabel('Value')
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
