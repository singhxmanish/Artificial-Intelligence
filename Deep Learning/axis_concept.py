# Concept of axis - work along a direction - axis_0 = operation alomg axis, axis_1 = operation along row
import numpy as np
import matplotlib.pyplot as plt

# Create a 2D NumPy array
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print("Original Data:")
print(data)

# Calculate the mean along axis=0 (down the columns)
mean_axis_0 = np.mean(data, axis=0)

# Plotting the result
plt.figure(figsize=(8, 5))
plt.bar(range(len(mean_axis_0)), mean_axis_0, color='skyblue')
plt.title('Mean of Each Column (Axis=0)')
plt.xlabel('Column Index')
plt.ylabel('Mean Value')
plt.xticks(range(len(mean_axis_0)), ['Col 0', 'Col 1', 'Col 2'])
plt.grid(axis='y', linestyle='--')
plt.show()

print("\nMean along axis=0:", mean_axis_0)

# Calculate the mean along axis=1 (across the rows)
mean_axis_1 = np.mean(data, axis=1)

# Plotting the result
plt.figure(figsize=(8, 5))
plt.bar(range(len(mean_axis_1)), mean_axis_1, color='lightgreen')
plt.title('Mean of Each Row (Axis=1)')
plt.xlabel('Row Index')
plt.ylabel('Mean Value')
plt.xticks(range(len(mean_axis_1)), ['Row 0', 'Row 1', 'Row 2'])
plt.grid(axis='y', linestyle='--')
plt.show()

print("\nMean along axis=1:", mean_axis_1)