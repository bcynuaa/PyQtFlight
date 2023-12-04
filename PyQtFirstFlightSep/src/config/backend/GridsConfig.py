'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: config for backend.Grids
 '''

import re

from src.config.LanguageConfig import *

grids_config_json_filename: str = os.path.join(config_path, "backend", "grids_config.json")
grids_config_dict: dict = json.load(open(grids_config_json_filename, "r", encoding=encoding))

standard_mode_response_file_regular_expression: str = grids_config_dict["standard mode response"]["regular expression"]
standard_mode_response_file_format: str = grids_config_dict["standard mode response"]["format"]
standard_mode_response_file_skiprows: int = grids_config_dict["standard mode response"]["skiprows"]
standard_mode_response_file_max_rows: int = grids_config_dict["standard mode response"]["max rows"]

basic_magnification: float = grids_config_dict["basic magnification"]

compared_sensor_index: int = grids_config_dict["compared sensor number"] - 1

standard_mode_response_file_regular_expression_pattern: re.Pattern = re.compile(standard_mode_response_file_regular_expression + standard_mode_response_file_format)

print("config.backend: GridsConfig.py is imported")