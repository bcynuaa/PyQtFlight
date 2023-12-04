'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-01 00:10:33
 # @ description: config for widgets.GridPlotter
 '''

from src.config.LanguageConfig import *

grid_plotter_config_json_filename: str = os.path.join(config_path, "widgets", "grid_plotter_config.json")
grid_plotter_config_dict: dict = json.load(open(grid_plotter_config_json_filename, "r", encoding=encoding))

clim: list = grid_plotter_config_dict["clim"]

print("config.widgets: GridPlotterConfig.py is imported.")