'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 02:17:41
 # @ description: config for interface.MessageBoxes
 '''

from src.config.LanguageConfig import *

message_boxes_config_json_filename: str = os.path.join(config_path, "interface", "message_boxes_config.json")
message_boxes_config_dict: dict = json.load(open(message_boxes_config_json_filename, "r", encoding=encoding))

load_json_file_succeeded_window_title: str = message_boxes_config_dict["load json file succeeded"]["window title"]
load_json_file_succeeded_message: str = message_boxes_config_dict["load json file succeeded"]["message"]

load_json_file_failed_window_title: str = message_boxes_config_dict["load json file failed"]["window title"]
load_json_file_failed_message: str = message_boxes_config_dict["load json file failed"]["message"]

save_data_stream_window_title: str = message_boxes_config_dict["save data stream"]["window title"]
save_data_stream_message: str = message_boxes_config_dict["save data stream"]["message"]

clear_data_stream_window_title: str = message_boxes_config_dict["clear data stream"]["window title"]
clear_data_stream_message: str = message_boxes_config_dict["clear data stream"]["message"]

start_monitoring_window_title: str = message_boxes_config_dict["start monitoring"]["window title"]
start_monitoring_message: str = message_boxes_config_dict["start monitoring"]["message"]
already_monitoring_window_title: str = message_boxes_config_dict["already monitoring"]["window title"]
already_monitoring_message: str = message_boxes_config_dict["already monitoring"]["message"]
end_monitoring_window_title: str = message_boxes_config_dict["end monitoring"]["window title"]
end_monitoring_message: str = message_boxes_config_dict["end monitoring"]["message"]
replay_finished_window_title: str = message_boxes_config_dict["replay finished"]["window title"]
replay_finished_message: str = message_boxes_config_dict["replay finished"]["message"]

print("config.interface: MessageBoxesConfig.py is imported")