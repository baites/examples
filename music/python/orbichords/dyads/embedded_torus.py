"""Example of quotient T^2 dyads embedded 3D."""

from matplotlib import cm
import matplotlib.pyplot as canvas
import numpy as np

# Torus parameters
FIGURE_SIZE = 6
MINOR_RADIUS = 2
MAYOR_RADIUS = 4

# Ordered pitch pair coordinates
X1 = (0.25, 0.50, 0.00, 0.25)
X2 = (0.75, 0.75, 0.50, 0.50)
COLORS = ['black', 'darkslategray', 'red', 'green']

figure = canvas.figure(figsize=(FIGURE_SIZE,FIGURE_SIZE))
ax = figure.add_subplot(111, projection='3d')
ax.view_init(90, -90)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)

# Create the supporting torus
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 2*np.pi, 100)
u, v = np.meshgrid(u,v)
X = (MAYOR_RADIUS + MINOR_RADIUS*np.cos(u)) * np.cos(v)
Y = (MAYOR_RADIUS + MINOR_RADIUS*np.cos(u)) * np.sin(v)
Z = MINOR_RADIUS * np.sin(u)
ax.plot_surface(X, Y, Z, alpha=0.3, cmap=cm.viridis)

# Add pair points
u = 2*np.pi*np.array(X1)
v = 2*np.pi*np.array(X2)
X = (MAYOR_RADIUS + (MINOR_RADIUS+0.2)*np.cos(u)) * np.cos(v)
Y = (MAYOR_RADIUS + (MINOR_RADIUS+0.2)*np.cos(u)) * np.sin(v)
Z = (MINOR_RADIUS+0.2)*np.sin(u)
ax.scatter(X, Y, Z, c=COLORS)

# Save the picture
#figure.savefigure("torus.png", dpi=100, transparent = False)

# Plot the picture
canvas.show()
