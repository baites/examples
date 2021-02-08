"""Tool to generate 8va quotient continuum dyad."""

from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates

    limit = 4

    # Plotting fundamental domain
    fundamental_domain = (
        [0, 0], [0, 1], [1, 1],
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
            lambda x: (x[0] + 1, x[1]),
            lambda x: (x[0], x[1] + 1),
            lambda x: (x[0] + 1, x[1] + 1),
            lambda x: (x[0] - 1, x[1]),
            lambda x: (x[0] - 1, x[1] + 1),
            lambda x: (x[0] - 1, x[1] - 1),
            lambda x: (x[0], x[1] - 1),
            lambda x: (x[0] + 1, x[1] - 1),
        ),
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[1], x[0])
        ),
    )

    # Identification lines
    id_lines = (
        {"begin": [0, 0], "end": [0, 1], "color": "blue"},
        {"begin": [1, 0], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 0], "color": "blue"},
        {"begin": [0, 1], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 1], "color": "orange"}
    )

    transform = lambda x: (x[0]+x[1], x[1]-x[0])

    # execute only if run as a script
    plot_dyad_orbichord(
        x_lim=[-limit/2, limit],
        y_lim=[-limit+1, limit-1],
        x_label="$\\phi_1$",
        y_label="$\\phi_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
        transform=transform
    )


if __name__ == "__main__":
    generate_plot()
