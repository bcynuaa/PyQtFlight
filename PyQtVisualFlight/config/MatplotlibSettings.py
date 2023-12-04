# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to set the global theme of matplotlib

# ref: https://matplotlib.org/stable/tutorials/introductory/customizing.html

import matplotlib.pyplot as plt
import matplotlib

mpl_style = {
    # !  line settings
    'lines.linewidth': 1.0,
    # ! figure settings
    'figure.figsize': (7, 4.0),
    'figure.facecolor': "white",
    'figure.dpi': 100,
    'figure.labelsize': 10,
    'figure.autolayout': True,
    # ! font settings
    'font.size': 15,
    'font.family': 'Times New Roman',
    # ! ticks settings
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'axes.titlesize': 20,
    'axes.labelsize': 15,
    'axes.grid': True,
    # ! savefig settings
    'savefig.dpi': 100,
    'savefig.bbox': "tight",
    # ! legend settings
    'legend.loc': "center right",
    'legend.fontsize': 15
}

for item in mpl_style.keys():
    matplotlib.rcParams[item] = mpl_style[item]
    pass

# https://matplotlib.org/stable/tutorials/colors/colormaps.html

cmap_option_list: list = [
    "viridis",
    "plasma",
    "inferno",
    "magma",
    "cividis",
    "coolwarm",
    "bwr",
    "seismic",
    "spring",
    "summer",
    "autumn",
    "winter",
    "cool",
    "Wistia",
    "hot",
    "afmhot",
    "gist_heat",
    "copper",
    "twilight",
    "twilight_shifted",
    "hsv",
    "ocean",
    "gist_earth",
    "terrain",
    "gist_stern",
    "gnuplot",
    "gnuplot2",
    "CMRmap",
    "cubehelix",
    "brg",
    "gist_rainbow",
    "rainbow",
    "jet",
    "nipy_spectral",
    "gist_ncar"
    "turbo"
]

print("Successfully set the global theme of matplotlib.")

###################################################################################################