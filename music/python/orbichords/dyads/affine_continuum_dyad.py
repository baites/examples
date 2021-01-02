"""Tool to generate continuum dyad."""

import math
from matplotlib.patches import Polygon

from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates

    limit = 2

    # Plotting fundamental domain
    fundamental_domain = Polygon(
        [[-limit, 0], [-limit, limit], [limit, limit], [limit, 0]],
        alpha=0.2,
        closed=True,
        fill=False,
        linewidth=0,
        hatch="\\\\",
    )

    # Probe points
    probes = [
        {
            "label": "A",
            "x": math.log(1, 2) + math.log(2, 2),
            "y": math.log(2, 2) - math.log(1, 2),
            "color": 'black'
        }
    ]

    # Action over probes
    actions = (
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[0], -x[1])
        ),
    )

    # Identification lines
    id_lines = [
        {
            "begin": [-limit, 0],
            "end": [limit, 0],
            "color": 'blue'
        }
    ]

    # execute only if run as a script
    plot_dyad_orbichord(
        [-limit, limit],
        [-limit, limit],
        xlabel='$\\phi_1$',
        ylabel='$\\phi_2$',
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines
    )


if __name__ == "__main__":
    generate_plot()
