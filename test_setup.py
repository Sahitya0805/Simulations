import sys
sys.path.insert(0, '/Users/sahityasingh/Simulations/lln-project')

# Test imports and basic execution
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    
    # Quick test
    np.random.seed(42)
    n = 100
    normal = np.random.normal(0, 1, n)
    normal_mean = np.cumsum(normal) / np.arange(1, n + 1)
    
    print("✓ NumPy and Matplotlib imported successfully")
    print(f"✓ Generated {n} samples")
    print(f"✓ Sample mean converged to: {normal_mean[-1]:.4f} (expected ≈ 0)")
    print("\n✓ All dependencies working correctly!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
