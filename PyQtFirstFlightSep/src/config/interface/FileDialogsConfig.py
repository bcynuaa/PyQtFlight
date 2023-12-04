'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 03:50:34
 # @ description: config for interface.FileDialogs
 '''

from src.config.LanguageConfig import *

file_dialogs_config_json_filename: str = os.path.join(config_path, "interface", "file_dialogs_config.json")
file_dialogs_config_dict: dict = json.load(open(file_dialogs_config_json_filename, "r", encoding=encoding))

load_json_file_default_path: str = file_dialogs_config_dict["load json file"]["default path"]
load_json_file_window_title: str = file_dialogs_config_dict["load json file"]["window title"]
load_json_file_filter: str = file_dialogs_config_dict["load json file"]["filter"]

save_data_stream_default_filename: str = file_dialogs_config_dict["save data stream"]["default filename"]
save_data_stream_window_title: str = file_dialogs_config_dict["save data stream"]["window title"]
save_data_stream_filter: str = file_dialogs_config_dict["save data stream"]["filter"]

print("config.interface: FileDialogsConfig.py is imported")