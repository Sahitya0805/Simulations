import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os

# Create graphs directory if it doesn't exist
os.makedirs('graphs', exist_ok=True)

n = 10000
replications = 300

means = []

for seed in range(replications):

    np.random.seed(seed)

    x = np.random.normal(0, 1, n)

    running_mean = np.cumsum(x) / np.arange(1, n + 1)

    means.append(running_mean)

means = np.array(means)

# Empirical confidence bands
lower = np.percentile(means, 2.5, axis=0)
upper = np.percentile(means, 97.5, axis=0)

# Theoretical band
x_axis = np.arange(1, n + 1)

theory = 1.96 / np.sqrt(x_axis)

# Plot
plt.figure(figsize=(12, 6))

plt.fill_between(
    x_axis,
    lower,
    upper,
    alpha=0.3,
    label='Empirical 95% Band'
)

plt.plot(
    x_axis,
    theory,
    linestyle='--',
    label='+1.96/sqrt(n)'
)

plt.plot(
    x_axis,
    -theory,
    linestyle='--',
    label='-1.96/sqrt(n)'
)

plt.xscale('log')

plt.xlabel('Sample Size')
plt.ylabel('Running Mean')

plt.title('95% Confidence Band')

plt.legend()
plt.grid(True)

plt.savefig('graphs/confidence_band.png', dpi=300)

print("✓ Graph saved: graphs/confidence_band.png")
