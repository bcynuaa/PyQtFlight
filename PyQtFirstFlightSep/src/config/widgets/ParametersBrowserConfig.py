'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-29 16:19:34
 # @ description: config for widgets.ParametersBrowser
 '''

from src.config.LanguageConfig import *

parameters_browser_config_json_filename: str = os.path.join(config_path, "widgets", "parameters_browser_config.json")
parameters_browser_config_dict: dict = json.load(open(parameters_browser_config_json_filename, "r", encoding=encoding))

open_external_links: bool = parameters_browser_config_dict["open external links"]
open_links: bool = parameters_browser_config_dict["open links"]
read_only: bool = parameters_browser_config_dict["read only"]

size_maximum_width: float = parameters_browser_config_dict["size"]["maximum width"]
size_maximum_height: float = parameters_browser_config_dict["size"]["maximum height"]
size_minimum_width: float = parameters_browser_config_dict["size"]["minimum width"]
size_minimum_height: float = parameters_browser_config_dict["size"]["minimum height"]

additional_text_before: str = parameters_browser_config_dict["additional text"]["before"]
additional_text_after: str = parameters_browser_config_dict["additional text"]["after"]

parameters_browser_config_qss_filename: str = os.path.join(config_path, "widgets", "parameters_browser_config.qss")
parameters_browser_config_style: str = open(parameters_browser_config_qss_filename, "r", encoding=qss_encoding).read()

print("config.widgets: ParametersBrowserConfig.py is imported.")