import matplotlib.pyplot as plt
import csv

# 1. Your raw data from the log
raw_data = [
    0.721, 1.400, 0.539, 3.300, 0.534, 2.733, 0.445, 3.333, 0.358, 4.367, 
    0.263, 5.433, 0.320, 4.133, 0.386, 3.600, 0.277, 4.967, 0.197, 5.867, 
    0.232, 5.967, 0.162, 6.967, 0.233, 5.733, 0.240, 5.633, 0.244, 5.167, 
    0.237, 5.500, 0.235, 6.100, 0.220, 5.667, 0.261, 5.233, 0.224, 5.167, 
    0.232, 5.667, 0.259, 4.800, 0.211, 5.533, 0.214, 5.867, 0.259, 5.433, 
    0.240, 5.533, 0.180, 6.167, 0.268, 4.567, 0.254, 5.433, 0.252, 5.267, 
    0.304, 5.533, 0.160, 7.200, 0.229, 6.167, 0.187, 6.333, 0.197, 6.033, 
    0.247, 5.833, 0.231, 5.833, 0.209, 6.300, 0.169, 6.633, 0.184, 6.167, 
    0.172, 6.767, 0.222, 5.333, 0.159, 7.133, 0.221, 5.633, 0.188, 6.200, 
    0.230, 5.900, 0.221, 6.033, 0.235, 6.133, 0.194, 6.233, 0.216, 5.967, 
    0.193, 6.133, 0.166, 6.900, 0.185, 6.467, 0.181, 6.100, 0.180, 6.433, 
    0.207, 6.467, 0.181, 6.600, 0.196, 5.933, 0.245, 5.233, 0.193, 6.133, 
    0.190, 6.433, 0.187, 6.367, 0.191, 6.167, 0.212, 5.967, 0.234, 5.400, 
    0.201, 5.433, 0.231, 5.300, 0.214, 5.233, 0.275, 4.900, 0.238, 5.233, 
    0.263, 5.567, 0.199, 6.000, 0.246, 5.700, 0.217, 5.433, 0.203, 5.900, 
    0.245, 5.067, 0.297, 4.467, 0.290, 4.367, 0.241, 5.333, 0.254, 5.000, 
    0.336, 4.600, 0.197, 6.233, 0.257, 5.000, 0.206, 5.767, 0.203, 5.700, 
    0.244, 5.200, 0.279, 5.433, 0.187, 5.900, 0.231, 5.433, 0.239, 5.367, 
    0.204, 5.900, 0.225, 5.467, 0.179, 6.400, 0.221, 5.367, 0.213, 5.767, 
    0.208, 5.633, 0.227, 4.933, 0.200, 5.933, 0.212, 6.300, 0.217, 5.300, 
    0.198, 6.467, 0.194, 6.000, 0.304, 4.733, 0.236, 5.367, 0.191, 5.800, 0.215, 5.400
]

# 2. Extract separate lists (Interleaved data: Prey, Pred, Prey, Pred...)
prey_vals = raw_data[0::2]
pred_vals = raw_data[1::2]
gens = list(range(1, len(prey_vals) + 1))

# 3. Create the Plot
plt.figure(figsize=(10, 6))
plt.plot(gens, prey_vals, label='Prey Fitness', color='green', linewidth=1.5, marker='o', markersize=3)
plt.plot(gens, pred_vals, label='Predator Fitness', color='red', linewidth=1.5, marker='x', markersize=3)

plt.title('Chase Demo: Predator vs. Prey Co-evolution')
plt.xlabel('Generation Count')
plt.ylabel('Average Fitness')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# 4. Save the Graph and CSV in the same folder
plt.savefig('fitness_plot.png', dpi=300, bbox_inches='tight')
print("Graph saved as 'fitness_plot.png'")

with open('fitness_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Generation', 'Prey_Fitness', 'Predator_Fitness']) # Header
    for g, py, pd in zip(gens, prey_vals, pred_vals):
        writer.writerow([g, py, pd])
print("Data saved as 'fitness_data.csv'")

# 5. Display the plot
plt.show()