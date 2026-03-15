import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Run 1: 61 generations 
run1_fitness = [
    1.667, 2.067, 3.867, 3.367, 3.867, 3.267, 2.067, 3.867, 3.367, 3.867, 
    3.267, 3.867, 3.367, 3.867, 3.267, 3.867, 3.267, 3.267, 3.167, 3.800, 
    4.200, 4.067, 4.200, 3.700, 3.600, 4.133, 4.100, 3.100, 4.633, 4.833, 
    5.200, 5.333, 4.733, 4.200, 4.300, 4.800, 4.400, 5.500, 4.700, 5.233, 
    5.333, 4.867, 4.600, 4.867, 5.200, 5.700, 4.600, 5.033, 3.667, 3.933, 
    5.000, 4.667, 5.133, 4.267, 4.700, 5.033, 4.767, 4.833, 5.300, 4.300, 5.633
]
gen_count_1 = len(run1_fitness) 

# Run 2: 22 generations 
run2_fitness = [
    0.833, 1.467, 1.500, 2.267, 2.333, 3.967, 4.433, 4.000, 4.500, 6.033, 
    4.767, 5.133, 4.300, 4.400, 4.633, 3.833, 4.533, 4.100, 4.300, 5.067, 
    4.433, 4.267
]
gen_count_2 = len(run2_fitness) 

#  Exporting for Excel 
max_len = max(gen_count_1, gen_count_2)
run2_padded = run2_fitness + [None] * (max_len - gen_count_2)

df = pd.DataFrame({
    'Generation': range(1, max_len + 1),
    'Run_1_Fitness': run1_fitness,
    'Run_2_Fitness': run2_padded
})
df.to_csv('run_comparison_final.csv', index=False)
print("Saved table to 'run_comparison_final.csv'")

# 2. Creating the Comparison Plot
plt.figure(figsize=(12, 7))

# Plot Run 1 
plt.plot(range(1, gen_count_1 + 1), run1_fitness, 
         label=f'Run 1: {gen_count_1} generations', color='#3498db', marker='o', markersize=3, alpha=0.7)

# Plot Run 2 
plt.plot(range(1, gen_count_2 + 1), run2_fitness, 
         label=f'Run 2: {gen_count_2} generations', color='#e67e22', linestyle='--', marker='s', markersize=3, alpha=0.9)

# Axis Styling
plt.title('Genetic Algorithm Performance: Comparison of Evolutionary History', fontsize=14, fontweight='bold')
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Average Fitness (Dots Collected)', fontsize=12)
plt.xticks(np.arange(0, 70, 5)) 
plt.ylim(0, 8) 
plt.grid(True, linestyle=':', alpha=0.6)

# Moving Legend to Upper Right
plt.legend(loc='upper right', fontsize=11, frameon=True, shadow=True)

# Save and Show
plt.savefig('comparison_graph_final.png', dpi=300)
print("Saved graph to 'comparison_graph_final.png'")
plt.show()