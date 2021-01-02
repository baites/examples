"""Help to ploting space of dyads."""

from itertools import product
import matplotlib.pyplot as canvas


def apply_actions(action_ntuple, value):
    """Apply all action in a list by concatenation."""
    result = None
    for action in action_ntuple:
        if result is None:
            result = action(value)
        else:
            result = action(result)
    return result


def plot_dyad_orbichord(
    xlim,
    ylim,
    xlabel,
    ylabel,
    fundamental_domain,
    probes,
    actions=((lambda x1, x2: (x1, x2),),),
    id_lines=None,
):
    """Generate the plot for continuum dyad orbichord."""
    canvas.rc("text", usetex=True)
    # Adding the plot to the figure

    # Setting figure in canvas
    _, plot = canvas.subplots()

    # Set limits
    plot.set_xlim(*xlim)
    plot.set_ylim(*ylim)

    # Compute scale
    xscale = xlim[1] - xlim[0]
    yscale = ylim[1] - ylim[0]
    shift_label = 0.025

    # -- Set plot spines at 0
    for spine in ["left", "bottom"]:
        plot.spines[spine].set_position("zero")

    # Hide the other spines...
    for spine in ["right", "top"]:
        plot.spines[spine].set_color("none")

    # -- Decorate the spins
    arrow_length = 20  # In points

    # X-plot arrow
    plot.annotate(
        xlabel,
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
        ylabel,
        xy=(0, 1),
        xycoords=("data", "axes fraction"),
        xytext=(0, arrow_length),
        textcoords="offset points",
        fontsize=12,
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="<-", fc="black"),
    )

    plot.add_patch(fundamental_domain)

    # Annotation configuration
    annotation_config = {"fontsize": 12, "ha": "center"}

    # Create the product iterator for actions
    actions = list(product(*actions))

    # Plotting one point within the fundamental domain
    x_probes = []
    y_probes = []
    c_probes = []
    for probe in probes:
        x = probe['x']
        y = probe['y']
        color = probe['color']
        for action_ntuple in actions:
            acted_x, acted_y = apply_actions(action_ntuple, (x, y))
            x_probes.append(acted_x)
            y_probes.append(acted_y)
            c_probes.append(probe["color"])
    plot.scatter(x=x_probes, y=y_probes, c=c_probes)
    identity_action = True
    for action_ntuple in actions:
        for probe in probes:
            config = annotation_config
            config["color"] = probe["color"]
            acted_x, acted_y = apply_actions(action_ntuple, (probe["x"], probe["y"]))
            if identity_action:
                label = "${}$".format(probe["label"])
            else:
                label = "${}'$".format(probe["label"])
            plot.annotate(
                label,
                (acted_x + shift_label * xscale, acted_y + shift_label * xscale),
                **config
            )
        identity_action = False

    if id_lines is not None:
        for action_ntuple in actions:
            for id_line in id_lines:
                begin = id_line["begin"]
                end = id_line["end"]
                color = id_line["color"]
                acted_begin = apply_actions(action_ntuple, begin)
                acted_end = apply_actions(action_ntuple, end)
                plot.annotate(
                    "",
                    acted_end,
                    xytext=acted_begin,
                    arrowprops=dict(color=color, arrowstyle="-"),
                )
                arrowx = (acted_begin[0] + acted_end[0]) / 2
                arrowy = (acted_begin[1] + acted_end[1]) / 2
                plot.annotate(
                    "",
                    (arrowx, arrowy),
                    xytext=(acted_begin[0], acted_begin[1]),
                    arrowprops=dict(color=color, arrowstyle="->")
                )

    canvas.show()
