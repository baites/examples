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


#pylint: disable=invalid-name
def simplex(x1, x2):
    """Implement 2D simplex transformation."""
    x1, x2 = sorted((x1, x2))
    while x1+x2 >= 1:
        tmp = x1
        x2 -= 1
        x1 = x2
        x2 = tmp
    return x1, x2


def affine(x1, x2):
    """Implement affine transformations."""
    return x1+x2, x2-x1


#pylint: disable=redefined-outer-name
def transform(X1, X2):
    """Implement the composition affine(simplex)."""
    dims = len(X1)
    phi1 = [0]*dims
    phi2 = [0]*dims
    for index in range(dims):
        phi1[index], phi2[index] = affine(*simplex(X1[index], X2[index]))
    return phi1, phi2


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
v = np.linspace(-1.0, 1.0, 100)
u, v = np.meshgrid(u, v)
X = (MAYOR_RADIUS + MINOR_RADIUS * v * np.cos(u/2.0)) * np.cos(u)
Y = (MAYOR_RADIUS + MINOR_RADIUS * v * np.cos(u/2.0)) * np.sin(u)
Z = MINOR_RADIUS * v * np.sin(u/2.0)
ax.plot_surface(X, Y, Z, alpha=0.3, cmap=cm.viridis)

# Add pair points
X1, X2 = transform(X1, X2)
u = 2 * np.pi * np.array(X1)
v = 2 * np.array(X2) - 1.0
X = (MAYOR_RADIUS + MINOR_RADIUS * v * np.cos(u/2.0)) * np.cos(u)
Y = (MAYOR_RADIUS + MINOR_RADIUS * v * np.cos(u/2.0)) * np.sin(u)
Z = MINOR_RADIUS * v * np.sin(u/2.0)
ax.scatter(X, Y, Z, c=COLORS)

# Save the picture
#figure.savefigure("torus.png", dpi=100, transparent = False)

# Plot the picture
canvas.show()
