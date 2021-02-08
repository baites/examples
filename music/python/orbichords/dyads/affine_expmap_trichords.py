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
        (0, 0, 0),
        (0, 0, limit),
        (-limit, 0, limit),
        (0, limit, limit),
    )

    # Probe points
    probes = (
        {
            "label": "A",
            "x": (
                0.5,
                1.0,
                2.0
            ),
            "color": "black",
        },
    )

    # Action over probes
    actions = ((
        lambda x: (x[0], x[1], x[2]),
        lambda x: (x[1], x[0], x[2]),
        lambda x: (x[0], x[2], x[1]),
        lambda x: (x[2], x[1], x[0]),
        lambda x: (x[2], x[0], x[1]),
        lambda x: (x[1], x[2], x[0]),                        
    ),)

    # Identification lines
    id_lines = ({"begin": [-limit, 0], "end": [limit, 0], "color": "blue"},)

    # Identification lines
    transform = lambda x: (x[1]-x[0], x[2]-x[1])

    # execute only if run as a script
    plot_dyad_orbichord(
        x_lim=(-limit, limit),
        y_lim=(-limit, limit),
        x_label="$\\phi_2$",
        y_label="$\\phi_3$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        #id_lines=id_lines,
        actions=actions,
        transform=transform
    )


if __name__ == "__main__":
    generate_plot()
