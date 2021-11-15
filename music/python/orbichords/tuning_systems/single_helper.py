"""Help to ploting space of dyads."""

from collections.abc import Callable
from itertools import product
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
def plot_single_orbichord(
    x_lim: tuple,
    x_label: str,
    probes: tuple,
    actions: tuple = ((lambda x: x,),),
    transform: Callable[tuple, tuple] = lambda x: x,
):
    """Generate the plot for continuum dyad orbichords.

    Parameters
    ----------
        x_lim : tuple
            Tuple with lower and upper x-axis limits.
        x_label : str
            Label of the x-axis.
        probes : tuple
            Points for probing the fundamental domain.
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
    plot.set_ylim(-4, 4)

    # Compute scale
    xscale = x_lim[1] - x_lim[0]
    shift_label = 0.025

    # Set plot spines at 0
    for spine in ["left", "bottom"]:
        plot.spines[spine].set_position("zero")

    # Hide the other spines...
    for spine in ["left", "right", "top"]:
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
            x = probe['x']
            color = probe["color"]
            acted_pair = apply_actions(action_ntuple, x)
            trans_x = transform(acted_pair)
            x_probes.append(trans_x)
            y_probes.append(0)
            c_probes.append(probe["color"])
    plot.scatter(x=x_probes, y=y_probes, c=c_probes)
    plot.set_yticks([])

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
            acted_pair = apply_actions(action_ntuple, probe['x'])
            trans_x = transform(acted_pair)
            plot.annotate(
                label,
                (trans_x + shift_label * xscale, shift_label * xscale),
                **config
            )
        identity_action = False

    canvas.show()
