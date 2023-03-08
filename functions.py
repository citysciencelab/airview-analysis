import numpy as np
import matplotlib.pyplot as plt


def calculate_statistics(dictionary_field):
    # Extract values from dictionary field
    values = list(dictionary_field.values())

    # Calculate mean, median, 25th percentile, and 75th percentile
    mean = np.mean(values)
    median = np.median(values)
    percentile25 = np.percentile(values, 25)
    percentile75 = np.percentile(values, 75)

    # Return results as a dictionary
    return {"mean": mean, "median": median, "25th percentile": percentile25, "75th percentile": percentile75}


def visualize_statistics(statistics):
    # Create a boxplot with error bars
    fig, ax = plt.subplots()
    data = [list(statistics.values())]
    ax.boxplot(data, widths=0.5, vert=False, showcaps=True, whis=(0,100), positions=[0])
    xerr = [[statistics['median']-statistics['25th percentile']], [statistics['75th percentile']-statistics['median']]]
    ax.errorbar(statistics.values(), [0]*len(statistics), xerr=xerr, fmt='none', color='black')
    ax.set_yticks([0])
    ax.set_yticklabels(['Statistics'])
    ax.set_title("Statistics")
    plt.show()


