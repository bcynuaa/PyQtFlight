'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-30 00:03:48
 # @ description: config for widgets.CurvesPlotter
 '''

from src.config.LanguageConfig import *

curves_plotter_config_json_filename: str = os.path.join(config_path, "widgets", "curves_plotter_config.json")
curves_plotter_config_dict: dict = json.load(open(curves_plotter_config_json_filename, "r", encoding=encoding))

max_points: int = curves_plotter_config_dict["max points"]

pen_color_list: list = curves_plotter_config_dict["pen"]["color list"]["values"]
pen_width: float = curves_plotter_config_dict["pen"]["width"]

global_color: str = curves_plotter_config_dict["global color"]
global_font_family: str = curves_plotter_config_dict["global font-family"]
background_color: str = curves_plotter_config_dict["background color"]
axis_width: float = curves_plotter_config_dict["axis width"]
pixel_size: int = curves_plotter_config_dict["pixel size"]

enable_mouse: bool = curves_plotter_config_dict["enable mouse"]
enable_menu: bool = curves_plotter_config_dict["enable menu"]

bottom_label: str = curves_plotter_config_dict["bottom"]["label"]
bottom_units: str = curves_plotter_config_dict["bottom"]["units"]
bottom_unitPrefix: str = curves_plotter_config_dict["bottom"]["unitPrefix"]

left_label: str = curves_plotter_config_dict["left"]["label"]
left_units: str = curves_plotter_config_dict["left"]["units"]
left_unitPrefix: str = curves_plotter_config_dict["left"]["unitPrefix"]

grid_x: bool = curves_plotter_config_dict["grid"]["x"]
grid_y: bool = curves_plotter_config_dict["grid"]["y"]

y_ticks_limit_activated: bool = curves_plotter_config_dict["y ticks limit"]["activated"]
y_ticks_limit_y_min: float = curves_plotter_config_dict["y ticks limit"]["y min"]
y_ticks_limit_y_max: float = curves_plotter_config_dict["y ticks limit"]["y max"]

title_name: str = curves_plotter_config_dict["title"]["name"]
title_settings_dict: dict = curves_plotter_config_dict["title"]["settings"].copy()
title_settings_dict["font-family"] = global_font_family
title_settings_dict["color"] = global_color

label_dict: dict = curves_plotter_config_dict["label"].copy()
label_dict["font-family"] = global_font_family
label_dict["color"] = global_color

pen_default_dict: dict = curves_plotter_config_dict["pen"].copy()
pen_default_dict.pop("color list")
pen_default_dict["color"] = pen_color_list[0]

print("config.widgets: CurvesPlotterConfig.py is imported.")