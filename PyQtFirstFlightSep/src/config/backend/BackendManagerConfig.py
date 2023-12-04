'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-29 00:20:37
 # @ description: config for backend.BackendManager
 '''

from src.config.LanguageConfig import *

backend_manager_config_json_filename: str = os.path.join(config_path, "backend", "backend_manager_config.json")
backend_manager_config_dict: dict = json.load(open(backend_manager_config_json_filename, "r", encoding=encoding))

curves_sensor_number_list: list = backend_manager_config_dict["curves"]["sensor number"]
curves_sensor_index_list: list = [item - 1 for item in curves_sensor_number_list]

bars_devide: int = backend_manager_config_dict["bars"]["devide"]
bars_value_limit: float = backend_manager_config_dict["bars"]["value limit"]
bars_sensor_number_except_activated: bool = backend_manager_config_dict["bars"]["sensor number"]["except"]["activated"]
bars_sensor_number_except_index_list: list = [item - 1 for item in backend_manager_config_dict["bars"]["sensor number"]["except"]["number"]]
bars_sensor_number_reorder_activated: bool = backend_manager_config_dict["bars"]["sensor number"]["reorder"]["activated"]
bars_sensor_number_reorder_index_list: list = [item - 1 for item in backend_manager_config_dict["bars"]["sensor number"]["reorder"]["number"]]

grids_sleep_time: float = backend_manager_config_dict["grids"]["sleep time"]

print("config.backend: BackendManagerConfig.py is imported")