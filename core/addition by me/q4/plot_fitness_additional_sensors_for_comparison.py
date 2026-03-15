import matplotlib.pyplot as plt

# 1. 3-6-2 Experimental Data (the 61-gen list you have out of 100)
# Here we use the first 61 generations to match the baseline's length for a direct comparison
experimental_data = [
    1.033, 1.967, 1.867, 2.167, 3.300, 2.567, 2.667, 3.433, 3.467, 4.500,
    4.433, 3.967, 3.900, 3.767, 4.333, 4.433, 4.333, 4.000, 3.800, 4.200,
    4.333, 4.000, 4.633, 3.933, 3.933, 4.900, 4.367, 5.033, 5.433, 4.200,
    4.400, 4.433, 4.700, 4.267, 4.533, 5.133, 4.867, 3.933, 4.433, 4.067,
    4.600, 4.433, 4.300, 4.867, 4.833, 4.200, 4.333, 4.033, 4.867, 5.000,
    5.100, 4.833, 4.600, 4.633, 4.700, 5.400, 4.700, 4.300, 4.833, 5.167,
    4.567
]

# 2. the 1-2 model
baseline_data = [1.667, 2.067, 3.867, 3.367, 3.867, 3.267, 2.067, 3.867, 3.367, 3.867, 
    3.267, 3.867, 3.367, 3.867, 3.267, 3.867, 3.267, 3.267, 3.167, 3.800, 
    4.200, 4.067, 4.200, 3.700, 3.600, 4.133, 4.100, 3.100, 4.633, 4.833, 
    5.200, 5.333, 4.733, 4.200, 4.300, 4.800, 4.400, 5.500, 4.700, 5.233, 
    5.333, 4.867, 4.600, 4.867, 5.200, 5.700, 4.600, 5.033, 3.667, 3.933, 
    5.000, 4.667, 5.133, 4.267, 4.700, 5.033, 4.767, 4.833, 5.300, 4.300, 5.633]

plt.figure(figsize=(10, 6))

# Plot both lines
plt.plot(range(1, len(baseline_data) + 1), baseline_data, label='Baseline (1-2 Arch)', color='grey', linestyle='--')
plt.plot(range(1, len(experimental_data) + 1), experimental_data, label='Experimental (3-6-2 Arch)', color='blue', linewidth=2)

plt.title('Performance Comparison: Architecture Evolution', fontsize=14)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Average Fitness', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig('architecture_comparison.png')
print("Comparison graph saved as architecture_comparison.png")
plt.show()