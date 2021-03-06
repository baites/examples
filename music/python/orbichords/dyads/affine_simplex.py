"""Tool to generate 8va quotient continuum dyad."""

from dyad_helper import plot_dyad_orbichord


#pylint: disable=invalid-name
def simplex(x):
    """Implement 2D simplex transformation."""
    x1, x2 = sorted((x[0], x[1]))
    while x1+x2 >= 1:
        tmp = x1
        x2 -= 1
        x1 = x2
        x2 = tmp
    return x1, x2


def generate_plot():
    """Generate a plot showing T_2/S_2 orbichord
       after reducing fundamental domain into a simplex and
       applying affine transformation.
    """

    # Set plot limits
    limit = 2

    # Plotting fundamental domain
    fundamental_domain = (
        (0, 0), (0.48, 0.48), (0.98, 0.98), (0.5, 0.5)
    )

    # Probe points
    probes = (
        {"label": "A", "x": (0.25, 0.75), "color": "black"},
        {"label": "B", "x": (0.50, 0.75), "color": "darkslategray"},
        {"label": "C", "x": (0.00, 0.50), "color": "red"},
        {"label": "D", "x": (0.25, 0.50), "color": "green"},
    )

    # Actions over probes
    actions = (
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[0] + 0.5, x[1] + 0.5),
            lambda x: (x[0] - 0.5, x[1] - 0.5),
            lambda x: (x[0] - 1.0, x[1] - 1.0),
            lambda x: (x[0] - 0.5, x[1] + 0.5),
            lambda x: (x[0] - 0.5, x[1] + 0.5),
            lambda x: (x[0] - 1.0, x[1]),
            lambda x: (x[0], x[1] + 1.0),
            lambda x: (x[0] - 1.5, x[1] - 0.5),
        ),
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[1], x[0])
        ),
    )

    # Identification lines
    id_lines = (
        {"begin": [0, 0], "end": [0.48, 0.48], "color": "orange"},
        {"begin": [0.48, 0.48], "end": [0.96, 0], "color": "blue"},
        {"begin": [0.5, 0.5], "end": [0.98, 0.98], "color": "orange"},
        {"begin": [0.5, 0.5], "end": [1, 0], "color": "blue"},
    )

    # Affine transform
    transform = lambda x: (x[0]+x[1], x[1]-x[0])

    # execute only if run as a script
    plot_dyad_orbichord(
        x_lim=(-limit, limit),
        y_lim=(-limit, limit),
        x_label="$\\phi_1$",
        y_label="$\\phi_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        simplex=simplex,
        actions=actions,
        id_lines=id_lines,
        transform=transform
    )


if __name__ == "__main__":
    generate_plot()
