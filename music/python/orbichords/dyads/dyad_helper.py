"""Help to ploting space of dyads."""

from collections.abc import Callable
from itertools import product
from matplotlib.patches import Polygon
import matplotlib.pyplot as canvas


def apply_actions(action_ntuple: tuple, value: float) -> float:
    """Apply all actions by concatenation.

    Parameters
    ----------
        action_ntuple : tuple
            Tuple with action to concatenate
        value : float
            Value to apply the concatenated actions

    Returns
    -------
        float
            Acted value
    """
    result = None
    for action in action_ntuple:
        if result is None:
            result = action(value)
        else:
            result = action(result)
    return result

#pylint: disable=too-many-arguments
#pylint: disable=too-many-locals
#pylint: disable=too-many-statements
def plot_dyad_orbichord(
    x_lim: tuple,
    y_lim: tuple,
    x_label: str,
    y_label: str,
    fundamental_domain: tuple,
    probes: tuple,
    simplex: Callable[tuple, tuple] = lambda x: x,
    id_lines: tuple = None,
    actions: tuple = ((lambda x: x,),),
    transform: Callable[tuple, tuple] = lambda x: x,
):
    """Generate the plot for continuum dyad orbichords.

    Parameters
    ----------
        x_lim : tuple
            Tuple with lower and upper x-axis limits.
        y_lim : tuple
            Tuple with lower and upper y-axis limits.
        x_label : str
            Label of the x-axis.
        y_label : str
            Label of the y-axis.
        fundamental_domain : tuple
            Points that forms fundamental domain polygon.
        probes : tuple
            Points for probing the fundamental domain.
        simplex : Callable[[float, float], tuple]
            Transforms to convert the fundamental domain into a simplex.
        id_lines:
            Identification lines to representing equivalent points.
        actions : tuple
            List of actions to be apply to probes and identification lines.
        transform : Callable[[float, float], tuple]
            Coordinate transformation common to all the objects.
    """

    # Enabling the use of latex in the canvas
    canvas.rc("text", usetex=True)

    # Setting figure in canvas
    _, plot = canvas.subplots()

    # Set limits
    plot.set_xlim(*x_lim)
    plot.set_ylim(*y_lim)

    # Compute scale
    xscale = x_lim[1] - x_lim[0]
    shift_label = 0.025

    # Set plot spines at 0
    for spine in ["left", "bottom"]:
        plot.spines[spine].set_position("zero")

    # Hide the other spines...
    for spine in ["right", "top"]:
        plot.spines[spine].set_color("none")

    # Decorate the spins
    arrow_length = 20  # In points

    # X-plot arrow
    plot.annotate(
        x_label,
        xy=(1, 0),
        xycoords=("axes fraction", "data"),
        xytext=(arrow_length, 0),
        textcoords="offset points",
        fontsize=12,
        ha="left",
        va="center",
        arrowprops=dict(arrowstyle="<-", fc="black"),
    )

    # Y-plot arrow
    plot.annotate(
        y_label,
        xy=(0, 1),
        xycoords=("data", "axes fraction"),
        xytext=(0, arrow_length),
        textcoords="offset points",
        fontsize=12,
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="<-", fc="black"),
    )

    # Plotting fundamental domain
    fundamental_domain = [transform(simplex(point)) for point in fundamental_domain]
    domain = Polygon(
        fundamental_domain,
        alpha=0.2,
        closed=True,
        fill=True,
        linewidth=0,
    )
    plot.add_patch(domain)

    # Annotation configuration
    annotation_config = {"fontsize": 12, "ha": "center"}

    # Create the product iterator for actions
    actions = list(product(*actions))

    # Add probes to plot
    x_probes = []
    y_probes = []
    c_probes = []
    for action_ntuple in actions:
        for probe in probes:
            x = probe["x"]
            color = probe["color"]
            acted_pair = apply_actions(action_ntuple, simplex(x))
            trans_x, trans_y = transform(acted_pair)
            x_probes.append(trans_x)
            y_probes.append(trans_y)
            c_probes.append(probe["color"])
    plot.scatter(x=x_probes, y=y_probes, c=c_probes)

    # Add probe's images after applying actions to plot
    identity_action = True
    for action_ntuple in actions:
        for probe in probes:
            config = annotation_config
            config["color"] = probe["color"]
            if identity_action:
                label = "${}$".format(probe["label"])
            else:
                label = "${}'$".format(probe["label"])
            acted_pair = apply_actions(action_ntuple, simplex(probe['x']))
            trans_x, trans_y = transform(acted_pair)
            plot.annotate(
                label,
                (trans_x + shift_label * xscale, trans_y + shift_label * xscale),
                **config
            )
        identity_action = False

    # Add identification lines to plots
    if id_lines is not None:
        for action_ntuple in actions:
            for id_line in id_lines:
                begin = id_line["begin"]
                end = id_line["end"]
                color = id_line["color"]
                begin = simplex(begin)
                end = simplex(end)
                acted_begin = apply_actions(action_ntuple, begin)
                acted_end = apply_actions(action_ntuple, end)
                trans_begin = transform(acted_begin)
                trans_end = transform(acted_end)
                plot.annotate(
                    "",
                    trans_end,
                    xytext=trans_begin,
                    arrowprops=dict(color=color, arrowstyle="-"),
                )
                arrowx = (trans_begin[0] + trans_end[0]) / 2
                arrowy = (trans_begin[1] + trans_end[1]) / 2
                plot.annotate(
                    "",
                    (arrowx, arrowy),
                    xytext=(trans_begin[0], trans_begin[1]),
                    arrowprops=dict(color=color, arrowstyle="->"),
                )
    canvas.show()
