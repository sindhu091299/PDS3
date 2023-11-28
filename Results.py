import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(234)

# Read the diabetes dataset
#file_path = "C:\\PDS\\Assignment3\\diabetes.csv"
data = pd.read_csv("C:\\PDS\\Assignment3\\diabetes.csv")

# Take a random sample of 25 observations
sample = data.sample(n=25)

# Calculate mean and max glucose for sample and population
sample_mean_glucose = np.mean(sample["Glucose"])
sample_max_glucose = np.max(sample["Glucose"])
pop_mean_glucose = np.mean(data["Glucose"])
pop_max_glucose = np.max(data["Glucose"])

# Create bar chart comparing mean and max glucose between sample and population
fig, ax = plt.subplots()
x = np.arange(2)
width = 0.35
ax.bar(x, [pop_mean_glucose, sample_mean_glucose], width, label='Mean Glucose')
ax.bar(x + width, [pop_max_glucose, sample_max_glucose], width, label='Max Glucose')
ax.set_ylabel('Glucose')
ax.set_title('Comparison of Glucose between Population and Sample')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(['Population', 'Sample'])
ax.legend()

plt.show()

sample_98_percentile = np.percentile(data["BMI"].sample(n=25), 98)
pop_98_percentile = np.percentile(data["BMI"], 98)

fig, ax = plt.subplots()
ax.bar(["Population", "Sample"], [pop_98_percentile, sample_98_percentile], label="98th Percentile BMI")
ax.set_ylabel("BMI")
ax.set_title("Comparison of 98th Percentile BMI between Population and Sample")
ax.legend()
plt.show()

n_samples = 500
sample_size = 150

sample_means = np.zeros(n_samples)
sample_stds = np.zeros(n_samples)
sample_percentiles = np.zeros(n_samples)

def bootstrap_sample(data):
    return data.sample(n=len(data), replace=True)

for i in range(n_samples):
    sample = bootstrap_sample(data["BloodPressure"]).sample(n=sample_size, replace=True)
    sample_means[i] = sample.mean()
    sample_stds[i] = sample.std()
    sample_percentiles[i] = np.percentile(sample, 75)

pop_mean_bp = data["BloodPressure"].mean()
pop_std_bp = data["BloodPressure"].std()
pop_percentile_bp = np.percentile(data["BloodPressure"], 75)

fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].hist(sample_means, bins=20)
axes[0].axvline(pop_mean_bp, color="red", linestyle="--", label="Population Mean")
axes[0].set_xlabel("Mean BloodPressure")
axes[0].set_ylabel("Frequency")
axes[0].legend()

axes[1].hist(sample_stds, bins=20)
axes[1].axvline(pop_std_bp, color="red", linestyle="--", label="Population Std")
axes[1].set_xlabel("Std BloodPressure")
axes[1].set_ylabel("Frequency")
axes[1].legend()

axes[2].hist(sample_percentiles, bins=20)
axes[2].axvline(pop_percentile_bp, color="red", linestyle="--", label="Population 75th Percentile")
axes[2].set_xlabel("75th Percentile BloodPressure")
axes[2].set_ylabel("Frequency")
axes[2].legend()

plt.tight_layout()
plt.show()

