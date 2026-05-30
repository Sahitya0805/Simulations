import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os

# Create graphs directory if it doesn't exist
os.makedirs('graphs', exist_ok=True)

np.random.seed(42)

n = 10000

# Normal data
x = np.random.normal(0, 1, n)

# Insert huge outlier
x[500] = 1000

running_mean = np.cumsum(x) / np.arange(1, n + 1)

# Plot
plt.figure(figsize=(12, 6))

plt.plot(running_mean)

plt.xscale('log')

plt.xlabel('Sample Size')
plt.ylabel('Running Mean')

plt.title('Effect of a Single Extreme Draw')

plt.grid(True)

plt.savefig('graphs/outlier_effect.png', dpi=300)

print("✓ Graph saved: graphs/outlier_effect.png")
