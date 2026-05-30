import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os

# Create graphs directory if it doesn't exist
os.makedirs('graphs', exist_ok=True)

np.random.seed(42)

sample_sizes = [10, 50, 100, 500, 1000, 5000, 10000]

normal_sd = []
exp_sd = []
uniform_sd = []

replications = 300

for n in sample_sizes:

    normal_means = []
    exp_means = []
    uniform_means = []

    for _ in range(replications):

        normal = np.random.normal(0, 1, n)
        exp = np.random.exponential(1, n)
        uniform = np.random.uniform(0, 1, n)

        normal_means.append(np.mean(normal))
        exp_means.append(np.mean(exp))
        uniform_means.append(np.mean(uniform))

    normal_sd.append(np.std(normal_means))
    exp_sd.append(np.std(exp_means))
    uniform_sd.append(np.std(uniform_means))

# Plot
plt.figure(figsize=(10, 6))

plt.plot(sample_sizes, normal_sd, marker='o', label='Normal')
plt.plot(sample_sizes, exp_sd, marker='o', label='Exponential')
plt.plot(sample_sizes, uniform_sd, marker='o', label='Uniform')

# Log-log scale
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Sample Size')
plt.ylabel('SD of Sample Mean')

plt.title('Convergence Speed')

plt.legend()
plt.grid(True)

plt.savefig('graphs/convergence_speed.png', dpi=300)

print("✓ Graph saved: graphs/convergence_speed.png")
