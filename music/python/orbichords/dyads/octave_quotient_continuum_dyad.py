"""Tool to generate 8va quotient continuum dyad."""

from matplotlib.patches import Polygon
from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates

    limit = 2

    # Plotting fundamental domain
    fundamental_domain = Polygon(
        [[0, 0], [0, 1], [1, 1]],
        alpha=0.2,
        closed=True,
        fill=False,
        linewidth=0,
        hatch="\\\\",
    )

    # Probe points
    probes = [
        {"label": "A", "x": 0.25, "y": 0.75, "color": "black"},
        {"label": "B", "x": 0.50, "y": 0.75, "color": "red"},
        {"label": "C", "x": 0.25, "y": 0.50, "color": "green"},
    ]

    # Actions over probes
    actions = (
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[0] + 1, x[1]),
            lambda x: (x[0], x[1] + 1),
            lambda x: (x[0] + 1, x[1] + 1),
        ),
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[1], x[0])
        ),
    )

    # Identification lines
    id_lines = [
        {"begin": [0, 0], "end": [0, 1], "color": "blue"},
        {"begin": [1, 0], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 0], "color": "blue"},
        {"begin": [0, 1], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 1], "color": "orange"}
    ]

    # execute only if run as a script
    plot_dyad_orbichord(
        [0, limit],
        [0, limit],
        xlabel="$y_1$",
        ylabel="$y_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
    )


if __name__ == "__main__":
    generate_plot()
