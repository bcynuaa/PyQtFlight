'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-02 19:56:53
 # @ description: config for widgets.WidgetsManager
 '''

import numpy as np
from src.config.LanguageConfig import *

widgets_manager_config_json_filename: str = os.path.join(config_path, "widgets", "widgets_manager_config.json")
widgets_manager_config_dict: dict = json.load(open(widgets_manager_config_json_filename, "r", encoding=encoding))

base_size: float = widgets_manager_config_dict["base size"]

relative_size_dict: dict = widgets_manager_config_dict["relative size"].copy()

relative_total_width: float = 0.0
relative_total_width += relative_size_dict["parameters browser"]["width"]
relative_total_width += relative_size_dict["bars plotter"]["width"]

total_width: float = relative_total_width * base_size

def getSize(local_total_width: float) -> tuple:
    local_base_size: float = local_total_width / total_width * base_size
    parameters_browser_width: float = local_base_size * relative_size_dict["parameters browser"]["width"]
    parameters_browser_height: float = local_base_size * relative_size_dict["parameters browser"]["height"]
    font_size: float = local_base_size / base_size * relative_size_dict["parameters browser"]["font size"]
    plotter_height: float = local_base_size * relative_size_dict["bars plotter"]["height"]
    return (int(np.floor(parameters_browser_width)), int(np.floor(parameters_browser_height)), \
        int(np.floor(font_size)), int(np.floor(plotter_height)))
    pass

print("config.widgets: WidgetsManagerConfig.py is imported.")