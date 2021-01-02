"""Tool to generate continuum dyad."""

from matplotlib.patches import Polygon

from dyad_helper import plot_dyad_orbichord


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 3

    # Plotting fundamental domain
    fundamental_domain = Polygon(
        [[0.02, 0.02], [0.02, limit], [limit, limit]],
        alpha=0.3,
        closed=True,
        fill=False,
        linewidth=0,
        hatch="\\\\",
    )

    # Probe points
    probes = [{"label": "A", "x": 1, "y": 2, "color": "black"}]

    # Action over probes
    actions = ((lambda x: (x[0], x[1]), lambda x: (x[1], x[0])),)

    # Identification lines
    id_lines = [{"begin": [0.02, 0.02], "end": [limit, limit], "color": "blue"}]

    # Execute only if run as a script
    plot_dyad_orbichord(
        [0, limit],
        [0, limit],
        xlabel="$x_1$",
        ylabel="$x_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
    )


if __name__ == "__main__":
    generate_plot()
