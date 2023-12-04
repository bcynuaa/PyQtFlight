# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to set the global theme of pyvista

# ref: https://docs.pyvista.org/version/stable/api/plotting/theme.html

import pyvista

pyvista.set_plot_theme("document")

pyvista.global_theme.font.size = 20.0
pyvista.global_theme.font.title_size = 40.0
pyvista.global_theme.font.family = "times"

pyvista.global_theme.cmap = "jet"
pyvista.global_theme.opacity = 0.6
pyvista.global_theme.color = "white"

pyvista.global_theme.show_edges = False
pyvista.global_theme.axes.show = True
pyvista.global_theme.show_scalar_bar = True
pyvista.global_theme.axes.show = True

print("Successfully set the global theme of pyvista.")

###################################################################################################