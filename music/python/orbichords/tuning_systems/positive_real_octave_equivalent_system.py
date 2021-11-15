"""Tool to generate positive real system."""

from single_helper import plot_single_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 10

    # Probe points
    probes = ({"label": "A", "x": 1.2, "color": "black"},)

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
        x_lim=[0, limit],
        x_label="$x$",
        probes=probes,
        actions=actions
    )


if __name__ == "__main__":
    generate_plot()
