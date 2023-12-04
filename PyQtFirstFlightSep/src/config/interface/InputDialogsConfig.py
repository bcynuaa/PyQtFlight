'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-13 17:33:30
 # @ description: config for interface.InputDialogsConfig
 '''

from src.config.LanguageConfig import *

input_dialogs_config_json_filename: str = os.path.join(config_path, "interface", "input_dialogs_config.json")
input_dialogs_config_dict: dict = json.load(open(input_dialogs_config_json_filename, "r", encoding=encoding))

replay_start_row_window_title: str = input_dialogs_config_dict["replay start row"]["window title"]
replay_start_row_label_text: str = input_dialogs_config_dict["replay start row"]["label text"]

replay_end_row_window_title: str = input_dialogs_config_dict["replay end row"]["window title"]
replay_end_row_label_text: str = input_dialogs_config_dict["replay end row"]["label text"]

replay_interval_row_window_title: str = input_dialogs_config_dict["replay interval row"]["window title"]
replay_interval_row_label_text: str = input_dialogs_config_dict["replay interval row"]["label text"]

print("config.interface: InputDialogsConfig.py is imported")