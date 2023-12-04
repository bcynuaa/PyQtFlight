'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-03 00:12:03
 # @ description: config for interface.MainWindowUI
 '''

from src.config.LanguageConfig import *

main_window_ui_config_json_filename: str = os.path.join(config_path, "interface", "main_window_ui_config.json")
main_window_ui_config_dict: dict = json.load(open(main_window_ui_config_json_filename, "r", encoding=encoding))

window_title: str = main_window_ui_config_dict["window title"]
window_icon: str = main_window_ui_config_dict["window icon"]

menu_bar_files_dict: dict = main_window_ui_config_dict["menu bar"]["files"].copy()
menu_bar_edit_dict: dict = main_window_ui_config_dict["menu bar"]["edit"].copy()
menu_bar_options_dict: dict = main_window_ui_config_dict["menu bar"]["options"].copy()
menu_bar_tools_dict: dict = main_window_ui_config_dict["menu bar"]["tools"].copy()

labels_dict: dict = main_window_ui_config_dict["labels"].copy()

main_window_ui_config_qss_filename: str = os.path.join(config_path, "interface", "main_window_ui_config.qss")
main_window_ui_config_style: str = open(main_window_ui_config_qss_filename, "r", encoding=qss_encoding).read()

print("config.interface: MainWindowUIConfig is imported")