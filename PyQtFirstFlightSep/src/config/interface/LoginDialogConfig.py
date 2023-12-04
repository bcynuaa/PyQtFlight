'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-09 01:46:49
 # @ description: config for interface.LoginDialog
 '''

from src.config.LanguageConfig import *

login_dialog_config_json_filename: str = os.path.join(config_path, "interface", "login_dialog_config.json")
login_dialog_config_dict: dict = json.load(open(login_dialog_config_json_filename, "r", encoding=encoding))

size: list = login_dialog_config_dict["size"]

dialog_title: str = login_dialog_config_dict["dialog title"]
dialog_icon: str = login_dialog_config_dict["dialog icon"]

username_label: str = login_dialog_config_dict["username"]["label"]
username_line_edit: str = login_dialog_config_dict["username"]["line edit"]

password_label: str = login_dialog_config_dict["password"]["label"]
password_line_edit: str = login_dialog_config_dict["password"]["line edit"]

login_button: str = login_dialog_config_dict["login button"]

login_dialog_config_qss_filename: str = os.path.join(config_path, "interface", "login_dialog_config.qss")
login_dialog_config_style: str = open(login_dialog_config_qss_filename, "r", encoding=qss_encoding).read()

print("config: interface.LoginDialog is imported.")