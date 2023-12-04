'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: config for libs.Pyvista
 '''

import pyvista

from src.config.LanguageConfig import *

pyvista_settings_json_filename: str = os.path.join(config_path, "libs", "pyvista_config.json")
pyvista_settings_dict: dict = json.load(open(pyvista_settings_json_filename, "r", encoding=encoding))

pyvista.set_plot_theme(pyvista_settings_dict["plot theme"]["value"])

pyvista.global_theme.font.size = pyvista_settings_dict["font"]["size"]
pyvista.global_theme.font.title_size = pyvista_settings_dict["font"]["title size"]
pyvista.global_theme.font.label_size = pyvista_settings_dict["font"]["label size"]
pyvista.global_theme.font.family = pyvista_settings_dict["font"]["family"]
pyvista.global_theme.font.color = pyvista_settings_dict["font"]["color"]
pyvista.global_theme.font.fmt = pyvista_settings_dict["font"]["fmt"]

pyvista.global_theme.cmap = pyvista_settings_dict["color"]["cmap"]
pyvista.global_theme.opacity = pyvista_settings_dict["color"]["opacity"]
pyvista.global_theme.color = pyvista_settings_dict["color"]["color"]
pyvista.global_theme.edge_color = pyvista_settings_dict["color"]["edge color"]
pyvista.global_theme.colorbar_horizontal.height = pyvista_settings_dict["color"]["colorbar horizontal height"]
pyvista.global_theme.colorbar_horizontal.width = pyvista_settings_dict["color"]["colorbar horizontal width"]

pyvista.global_theme.show_edges = pyvista_settings_dict["plot"]["show edges"]
pyvista.global_theme.axes.show = pyvista_settings_dict["plot"]["axes show"]
pyvista.global_theme.show_scalar_bar = pyvista_settings_dict["plot"]["show scalar bar"]

print("config.libs: PyvistaConfig.py is imported.")