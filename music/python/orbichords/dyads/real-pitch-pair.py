"""Tool to generate continuum dyad."""

import math
from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 2

    # Plotting fundamental domain
    fundamental_domain = (
        (-limit, -limit),
        (-limit,  limit),
        ( limit,  limit),
        ( limit, -limit),        
    )

    # Probe points
    probes = (
        {
            "label": "A",
            "x": (0.25, 0.75),
            "color": "black"
        },
    )

    # Action over probes
    actions = ((
        lambda x: (x[0], x[1]),
    ),)

    # Identification lines
    id_lines = ()

    # execute only if run as a script
    plot_dyad_orbichord(
        x_lim=[-limit, limit],
        y_lim=[-limit, limit],
        x_label="$g_1$",
        y_label="$g_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
    )


if __name__ == "__main__":
    generate_plot()
