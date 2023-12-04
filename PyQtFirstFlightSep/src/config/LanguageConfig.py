'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-01 15:35:50
 # @ description: config for Language
 '''

import os
import json

language_config_json_filename: str = "config//language_config.json"
language_config_dict: dict = json.load(open(language_config_json_filename, "r", encoding="utf-8"))

language: str = language_config_dict["language"]
encoding: str = language_config_dict["encoding"][language]
qss_encoding: str = language_config_dict["qss encoding"]

config_path: str = os.path.join(".//config", language)

print("config: LanguageConfig.py is imported")
print("language: %s, encoding: %s" % (language, encoding))
print("config path: %s" % config_path)