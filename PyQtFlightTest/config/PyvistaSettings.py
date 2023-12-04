'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-05 17:53:05
 # @ license: Mozilla Public License 2.0
 # @ description: this file contains the settings for pyvista in the program
 '''
 
# ref:
# - https://docs.pyvista.org/version/stable/api/plotting/theme.html

import pyvista

pyvista.set_plot_theme("document")

pyvista.global_theme.font.size = 20.0
pyvista.global_theme.font.title_size = 40.0
pyvista.global_theme.font.family = "times"

pyvista.global_theme.cmap = "jet"
pyvista.global_theme.opacity = 0.6
pyvista.global_theme.color = "white"

pyvista.global_theme.show_edges = True
pyvista.global_theme.axes.show = True
pyvista.global_theme.show_scalar_bar = True
pyvista.global_theme.axes.show = True

print("config: Pyvista settings have been finished.")