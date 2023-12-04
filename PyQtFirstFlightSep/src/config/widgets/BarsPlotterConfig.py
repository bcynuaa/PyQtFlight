'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-31 16:15:31
 # @ description: config for widgets.BarsPlotter
 '''

from src.config.LanguageConfig import *

bars_plotter_config_json_filename: str = os.path.join(config_path, "widgets", "bars_plotter_config.json")
bars_plotter_config_dict: dict = json.load(open(bars_plotter_config_json_filename, "r", encoding=encoding))

bars_first_bar_x_position: float = bars_plotter_config_dict["bars"]["first bar x position"]
bars_width: float = bars_plotter_config_dict["bars"]["width"]
bars_spacing: float = bars_plotter_config_dict["bars"]["spacing"]
bars_y0: float = bars_plotter_config_dict["bars"]["y0"]
bars_pen_dict: dict = bars_plotter_config_dict["bars"]["pen"]
bars_brush_color: str = bars_plotter_config_dict["bars"]["brush"]["color"]

x_ticks_auto: bool = bars_plotter_config_dict["x ticks"]["auto"]
x_ticks_name: str = bars_plotter_config_dict["x ticks"]["name"]
x_ticks_separator: str = bars_plotter_config_dict["x ticks"]["separator"]
x_ticks_custom: list = bars_plotter_config_dict["x ticks"]["custom"]

y_ticks_use_fixed_range: bool = bars_plotter_config_dict["y ticks"]["use fixed range"]
y_ticks_min: float = bars_plotter_config_dict["y ticks"]["min"]
y_ticks_max: float = bars_plotter_config_dict["y ticks"]["max"]

crucial_line_activated: bool = bars_plotter_config_dict["crucial line"]["activated"]
crucial_line_y_position: float = bars_plotter_config_dict["crucial line"]["y position"]
crucial_line_pen_dict: dict = bars_plotter_config_dict["crucial line"]["pen"]

global_color: str = bars_plotter_config_dict["global color"]
global_font_family: str = bars_plotter_config_dict["global font-family"]
background_color: str = bars_plotter_config_dict["background color"]
axis_width: float = bars_plotter_config_dict["axis width"]
pixel_size: float = bars_plotter_config_dict["pixel size"]
enable_mouse: bool = bars_plotter_config_dict["enable mouse"]
enable_menu: bool = bars_plotter_config_dict["enable menu"]

bottom_label: str = bars_plotter_config_dict["bottom"]["label"]
bottom_units: str = bars_plotter_config_dict["bottom"]["units"]
bottom_unitPrefix: str = bars_plotter_config_dict["bottom"]["unitPrefix"]

left_label: str = bars_plotter_config_dict["left"]["label"]
left_units: str = bars_plotter_config_dict["left"]["units"]
left_unitPrefix: str = bars_plotter_config_dict["left"]["unitPrefix"]

label_dict: dict = bars_plotter_config_dict["label"].copy()
label_dict["font-family"] = global_font_family
label_dict["color"] = global_color

title_name: str = bars_plotter_config_dict["title"]["name"]
title_settings_dict: dict = bars_plotter_config_dict["title"]["settings"].copy()
title_settings_dict["font-family"] = global_font_family
title_settings_dict["color"] = global_color

grid_x: bool = bars_plotter_config_dict["grid"]["x"]
grid_y: bool = bars_plotter_config_dict["grid"]["y"]

additional_things_text: dict = bars_plotter_config_dict["additional things"]["text"]
additional_things_vertical_line: dict = bars_plotter_config_dict["additional things"]["vertical line"]

print("config.widgets: BarsPlotterConfig is imported")