from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np


def set_temp_interval(ax: plt.Axes, interval_size=1.2, y_min=None):
    """
    Set temperature interval size.
    Parameters
    ----------
    y_min
    ax : plt.Axes
    interval_size : float

    Returns
    -------

    """
    if not y_min:
        y_min, _ = ax.get_ylim()
        y_min -= interval_size * .03
    ax.set_ylim(y_min, y_min + interval_size)


def plot_2_values(x: np.array, y1: np.array, y2: np.array, xlabel="t(s)", y1label="Druck(Pa)", y2label="T(Ohm)"
                  , figsize=None):
    """
    Plots 2 y values, both in relation to the value x.
    Parameters
    ----------
    figsize : list
    x : np.array of x-values
    y1 : np.array od y1 values
    y2 : np.array od y2 values
    xlabel : default "t(s)"
    y1label : default "Druck(Pa)"
    y2label : default "T(Ohm)"

    Returns
    -------
    plt.Figure : figure of plots
    plt.Axis : ax1 of y1 values
    plt.Axis : ax2 of y2 values
    """
    if figsize is None:
        figsize = (10, 5)
    mpl.rcParams.update({'font.size': 15})

    f, ax1 = plt.subplots(figsize=figsize)

    color = "tab:blue"
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(y1label, color=color)
    ax1.plot(x, y1, color=color)

    ax2 = ax1.twinx()

    color = "tab:orange"
    ax2.set_ylabel(y2label, color=color)
    ax2.plot(x, y2, color=color)

    ax1.grid()

    return f, ax1, ax2
