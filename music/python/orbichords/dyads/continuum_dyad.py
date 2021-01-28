"""Tool to generate continuum dyad."""

from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 3

    # Plotting fundamental domain
    fundamental_domain = (
        (0.02, 0.02), (0.02, limit), (limit, limit),
    )

    # Probe points
    probes = ({"label": "A", "x": 1, "y": 2, "color": "black"},)

    # Action over probes
    actions = (
    (
        lambda x: (x[0], x[1]),
        lambda x: (x[1], x[0])),
    )

    # Identification lines
    id_lines = ({"begin": [0.02, 0.02], "end": [limit, limit], "color": "blue"},)

    # Execute only if run as a script
    plot_dyad_orbichord(
        x_lim=[0, limit],
        y_lim=[0, limit],
        x_label="$x_1$",
        y_label="$x_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines
    )


if __name__ == "__main__":
    generate_plot()
