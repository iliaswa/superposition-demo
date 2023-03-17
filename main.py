import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the superposition function
def superposition(x, y):
    return np.exp(-(x**2 + y**2)) * (np.sin(x) + np.cos(y))

# Create the x and y coordinates for the 3D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = superposition(X, Y)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Probability amplitude')
ax.set_title('Quantum Superposition')

# Show the plot
plt.show()
