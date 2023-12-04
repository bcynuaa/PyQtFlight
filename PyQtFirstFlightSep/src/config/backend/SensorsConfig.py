'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: config for backend.Sensors
 '''

import re

from src.config.LanguageConfig import *

sensors_config_json_filename: str = os.path.join(config_path, "backend", "sensors_config.json")
sensor_config_dict: dict = json.load(open(sensors_config_json_filename, "r", encoding=encoding))

map_matrix_regular_expression: str = sensor_config_dict["map matrix"]["regular expression"]
map_matrix_regular_expression_format: str = sensor_config_dict["map matrix"]["format"]
skiprows: int = sensor_config_dict["map matrix"]["skiprows"]

map_matrix_regular_expression_pattern: re.Pattern = re.compile(map_matrix_regular_expression + map_matrix_regular_expression_format)

print("config.backend: SensorsConfig.py is imported")