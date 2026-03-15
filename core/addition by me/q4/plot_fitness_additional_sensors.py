import matplotlib.pyplot as plt

# Your 100-generation fitness data
fitness_data = [
    1.033, 1.967, 1.867, 2.167, 3.300, 2.567, 2.667, 3.433, 3.467, 4.500,
    4.433, 3.967, 3.900, 3.767, 4.333, 4.433, 4.333, 4.000, 3.800, 4.200,
    4.333, 4.000, 4.633, 3.933, 3.933, 4.900, 4.367, 5.033, 5.433, 4.200,
    4.400, 4.433, 4.700, 4.267, 4.533, 5.133, 4.867, 3.933, 4.433, 4.067,
    4.600, 4.433, 4.300, 4.867, 4.833, 4.200, 4.333, 4.033, 4.867, 5.000,
    5.100, 4.833, 4.600, 4.633, 4.700, 5.400, 4.700, 4.300, 4.833, 5.167,
    4.567, 4.900, 4.933, 4.467, 4.667, 4.700, 4.900, 4.967, 5.000, 5.167,
    4.500, 4.967, 4.733, 4.533, 5.467, 4.767, 4.233, 5.233, 4.200, 4.733,
    5.367, 4.867, 4.933, 5.033, 4.367, 4.867, 5.133, 5.167, 4.900, 4.500,
    4.633, 4.533, 4.967, 4.367, 4.233, 4.633, 4.933, 3.833, 4.467, 4.767
]

plt.figure(figsize=(10, 6))
plt.plot(range(1, 101), fitness_data, color='blue', linewidth=2, label='Average Fitness')
plt.axhline(y=sum(fitness_data)/100, color='red', linestyle='--', label='Mean Performance')

plt.title('Evolutionary Performance: Tri-Sensor 3-6-2 Architecture', fontsize=14)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Average Fitness (Cheese Found)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Save the plot for the report
plt.savefig('fitness_graph.png')
print("Graph saved as fitness_graph.png - include this in your report!")
plt.show()