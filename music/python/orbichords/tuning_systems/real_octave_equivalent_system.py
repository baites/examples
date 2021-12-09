"""Tool to generate real system."""

import numpy as np
from single_helper import plot_single_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 4

    # Probe points
    probes = ({"label": "x", "x": 1.2, "color": "black"},)

    # Action over probes
    actions = (
        (
            lambda x: x,
            lambda x: 0.125*x,
            lambda x: 0.25*x,
            lambda x: 0.5*x,
            lambda x: 2*x,
            lambda x: 4*x,
            lambda x: 8*x
        ),
    )

    # Execute only if run as a script
    plot_single_orbichord(
        x_lim=[-limit, limit],
        x_label="$\log_2(x)$",
        probes=probes,
        actions=actions,
        transform = lambda x: np.log2(x)
    )


if __name__ == "__main__":
    generate_plot()
