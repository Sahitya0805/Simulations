import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os

# Create graphs directory if it doesn't exist
os.makedirs('graphs', exist_ok=True)

# Fixed seed from report
np.random.seed(42)

# Number of observations
n = 10000

# Generate distributions
normal = np.random.normal(0, 1, n)
exponential = np.random.exponential(1, n)
uniform = np.random.uniform(0, 1, n)
cauchy = np.random.standard_cauchy(n)

# Running means
normal_mean = np.cumsum(normal) / np.arange(1, n + 1)
exp_mean = np.cumsum(exponential) / np.arange(1, n + 1)
uniform_mean = np.cumsum(uniform) / np.arange(1, n + 1)
cauchy_mean = np.cumsum(cauchy) / np.arange(1, n + 1)

# Plot
plt.figure(figsize=(12, 6))

plt.plot(normal_mean, label='Normal(0,1)')
plt.plot(exp_mean, label='Exponential(1)')
plt.plot(uniform_mean, label='Uniform(0,1)')
plt.plot(cauchy_mean, label='Cauchy(0,1)')

# True means
plt.axhline(0, linestyle='--')
plt.axhline(1, linestyle='--')
plt.axhline(0.5, linestyle='--')

# Logarithmic scale
plt.xscale('log')

plt.xlabel('Sample Size (log scale)')
plt.ylabel('Running Sample Mean')

plt.title('Law of Large Numbers')

plt.legend()
plt.grid(True)

# Save graph
plt.savefig('graphs/running_mean.png', dpi=300)
print("✓ Graph saved: graphs/running_mean.png")
