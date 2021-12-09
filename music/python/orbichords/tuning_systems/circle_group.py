import numpy as np
import matplotlib.pyplot as canvas

canvas.rc("text", usetex=True)

_, plot = canvas.subplots(1)

angle = np.linspace( 0 , 2 * np.pi , 150)
radius = 1.0
x = radius * np.cos(angle)
y = radius * np.sin(angle)
plot.plot(x, y, color='black')
plot.set_aspect( 1 )

coordinate = np.log2(1.2)
x = radius * np.cos(coordinate * 2 * np.pi)
y = radius * np.sin(coordinate * 2 * np.pi)
plot.scatter(x=[x], y=[y], c='black')

plot.set_xlabel('real')
plot.set_ylabel('imaginary')

config = {"fontsize": 12, "ha": "center"}
plot.annotate(
    '$x$',
    (x + 0.05, y + 0.03),
    **config
)

canvas.title('Circle group')
canvas.show()