'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: config for backend.DomainsWithModes
 '''

import re

from src.config.LanguageConfig import *

domains_with_modes_config_json_filename: str = os.path.join(config_path, "backend", "domains_with_modes_config.json")
domains_with_modes_config_dict: dict = json.load(open(domains_with_modes_config_json_filename, "r", encoding=encoding))

domains_regular_expression: str = domains_with_modes_config_dict["domains"]["regular expression"]
domains_format: str = domains_with_modes_config_dict["domains"]["format"]

dim: int = domains_with_modes_config_dict["dim"]

scalars_list: list = domains_with_modes_config_dict["scalars"]["list"]
scalars_default: str = domains_with_modes_config_dict["scalars"]["default"]

domains_regular_expression_pattern: re.Pattern = re.compile(domains_regular_expression + domains_format)

print("config.backend: DomainsWithModesConfig.py is imported")