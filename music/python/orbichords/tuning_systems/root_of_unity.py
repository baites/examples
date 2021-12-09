import numpy as np
import matplotlib.pyplot as canvas

canvas.rc("text", usetex=True)

_, plot = canvas.subplots(1)

angle = np.linspace( 0 , 2 * np.pi , 150)
radius = 1.0
x = radius * np.cos(angle)
y = radius * np.sin(angle)
plot.plot(x, y, '--', color='black', linewidth=0.9)

angle = np.linspace( 0 , 2 * np.pi * 11/12, 12)
radius = 1.0
xs = radius * np.cos(angle)
ys = radius * np.sin(angle)
plot.plot(xs, ys, 'o', color='black')
plot.set_aspect( 1 )

plot.set_xlabel('real')
plot.set_ylabel('imaginary')

config = {"fontsize": 12, "ha": "center"}

counter = 0
xs = 0.85 * radius * np.cos(angle)
ys = 0.85 * radius * np.sin(angle) - 0.035
for x, y in zip(xs, ys):
    plot.annotate(
        f'${counter}$',
        (x, y),
        **config
    )
    counter += 1

canvas.title('Roots of $z^{12} - 1$')
canvas.show()