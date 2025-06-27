import matplotlib.pyplot as plt
import numpy as np

# Data (median and IQR)
data = {
    'Before service': {'median': 1, 'q1': 0, 'q3': 2},
    'During service': {'median': 0, 'q1': 0, 'q3': 1}
}

# Generate synthetic data matching the medians and IQRs
np.random.seed(42)  # For reproducibility
def generate_data(median, q1, q3, n=100):
    lower = np.random.uniform(q1, median, size=n//2) 
    upper = np.random.uniform(median, q3, size=n//2)
    return np.concatenate([lower, upper])

before_data = generate_data(data['Before service']['median'], 
                           data['Before service']['q1'], 
                           data['Before service']['q3'])
during_data = generate_data(data['During service']['median'], 
                           data['During service']['q1'], 
                           data['During service']['q3'])

# Create the boxplot
plt.figure(figsize=(8, 6))
boxplot = plt.boxplot(
    [before_data, during_data],
    labels=['Before service', 'During service'],
    patch_artist=True,
    widths=0.6,
    medianprops={'color': 'black', 'linewidth': 2},
    boxprops={'facecolor': 'lightgray', 'edgecolor': 'black', 'linewidth': 1.5},
    whiskerprops={'linestyle': '--', 'linewidth': 1.5},
    capprops={'linewidth': 1.5}
)

# Highlight medians and add labels
for i, service in enumerate(data.keys(), start=1):
    plt.text(i, data[service]['median'] + 0.1, 
             f"Median = {data[service]['median']}", 
             ha='center', va='bottom', color='black', fontweight='bold')

# Add p-value annotation (as in the original graph)
plt.text(1.5, plt.ylim()[1] - 0.5, "* p = 0.02", 
         ha='center', va='top', fontsize=12, fontweight='bold')

# Style adjustments
plt.title("Hospital Admissions Before vs. During Service", pad=20, fontweight='bold')
plt.ylabel("Number of Admissions (count)", labelpad=10)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()