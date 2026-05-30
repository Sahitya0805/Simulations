# Law of Large Numbers Simulation

## Overview
This project demonstrates the Law of Large Numbers (LLN) through statistical simulations using Python, NumPy, and Matplotlib. It recreates key concepts from probability theory and shows how sample means converge to population means.

## Topics Covered
- **Running Sample Mean**: Shows how different distributions' sample means converge to their true values
- **Convergence Speed**: Demonstrates that standard deviation decreases as $\frac{\sigma}{\sqrt{n}}$
- **Confidence Bands**: Visualizes the 95% confidence interval shrinking as sample size increases
- **Outlier Effects**: Illustrates how a single extreme value impacts convergence
- **Cauchy Counterexample**: Shows a distribution where the LLN fails (included in running mean graph)

## Technologies
- Python 3.11+
- NumPy (numerical computing)
- Matplotlib (visualization)

## Project Structure
```
lln-project/
├── graphs/                      # Output directory for generated plots
├── running_mean.py              # Running mean convergence
├── convergence_speed.py         # SD reduction with sample size
├── confidence_band.py           # 95% confidence intervals
├── outlier_effect.py            # Impact of single extreme observation
├── requirements.txt             # Project dependencies
├── venv/                        # Virtual environment
└── README.md                    # This file
```

## Installation

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## How to Run

Run any of the simulation scripts:

```bash
# Activate virtual environment first
source venv/bin/activate

# Run simulations
python running_mean.py
python convergence_speed.py
python confidence_band.py
python outlier_effect.py
```

Each script will:
1. Generate random samples from different distributions
2. Calculate running sample means or other statistics
3. Create and save visualization to `graphs/` folder
4. Display the plot

## Key Findings

### Running Mean
- **Normal(0,1)**: Converges to 0
- **Exponential(1)**: Converges to 1
- **Uniform(0,1)**: Converges to 0.5 (fastest)
- **Cauchy(0,1)**: Never converges (no finite mean)

### Convergence Speed
Empirically verifies: $SD(\bar{X}_n) = \frac{\sigma}{\sqrt{n}}$

All distributions show the same convergence rate on log-log scale.

### Confidence Bands
95% confidence interval width shrinks according to: $\mu \pm \frac{1.96\sigma}{\sqrt{n}}$

### Outlier Effects
A single extreme value (like 1000) creates a temporary spike, but the effect diminishes as $\frac{1}{n}$.

## Dependencies

- `numpy==2.4.6` - Numerical computing
- `matplotlib==3.10.9` - Data visualization
- `pillow==12.2.0` - Image processing
- And associated dependencies

## Mathematical Background

The Law of Large Numbers states that as sample size increases, the sample mean $\bar{X}_n$ converges to the population mean $\mu$:

$$\lim_{n \to \infty} \bar{X}_n = \mu$$

This simulation demonstrates this convergence empirically across different probability distributions.

## Notes
- Random seeds are fixed for reproducibility
- Graphs are saved as high-resolution PNG files (300 dpi)
- Cauchy distribution demonstrates why finite mean is crucial for LLN
- Use log scale on x-axis to observe full convergence pattern
