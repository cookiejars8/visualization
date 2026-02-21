# Class 2 - Participation
# Data Visualization - Choosing the Right Visualization

import matplotlib.pyplot as plt
import numpy as np

# Create some example data
x = np.arange(1, 11)
y = np.random.randint(1, 20, 10)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(6, 4))

# Make a scatter plot
ax.scatter(x, y)

# Add labels and title
ax.set_title("Example Scatter Plot")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Show the plot
plt.show()