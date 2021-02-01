"""Tool to generate continuum dyad."""

from math import log
from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showing expmap orbichord
    after applying affine transformation.
    """
    # Size of the coordinates
    limit = 2

    # Plotting fundamental domain
    fundamental_domain = (
        (-limit, 0),
        (-limit, limit),
        (limit, limit),
        (limit, 0),
    )

    # Probe points
    probes = (
        {
            "label": "A",
            "x": log(1, 2) + log(2, 2),
            "y": log(2, 2) - log(1, 2),
            "color": "black",
        },
    )

    # Action over probes
    actions = ((lambda x: (x[0], x[1]), lambda x: (x[0], -x[1])),)

    # Identification lines
    id_lines = ({"begin": [-limit, 0], "end": [limit, 0], "color": "blue"},)

    # execute only if run as a script
    plot_dyad_orbichord(
        x_lim=(-limit, limit),
        y_lim=(-limit, limit),
        x_label="$\\phi_1$",
        y_label="$\\phi_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        id_lines=id_lines,
        actions=actions,
    )


if __name__ == "__main__":
    generate_plot()
