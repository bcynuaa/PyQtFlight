'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-23 00:07:33
 # @ description: config for backend.DataStream
 '''

import re

from src.config.LanguageConfig import *

data_stream_config_json_filename: str = os.path.join(config_path, "backend", "data_stream_config.json")
data_stream_config_dict: dict = json.load(open(data_stream_config_json_filename, "r", encoding=encoding))

latest_data_regular_expression: str = data_stream_config_dict["latest data"]["regular expression"]
latest_data_format: str = data_stream_config_dict["latest data"]["format"]
latest_data_skiprows: int = data_stream_config_dict["latest data"]["skiprows"]
latest_data_delim_whitespace: bool = data_stream_config_dict["latest data"]["delim_whitespace"]
latest_data_header: str = data_stream_config_dict["latest data"]["header"]
latest_data_index_col: str = data_stream_config_dict["latest data"]["index_col"]

time_columns_name: str = data_stream_config_dict["time columns"]["name"]
time_columns_component: dict = data_stream_config_dict["time columns"]["component"]
time_columns_component_index_list: list = [time_columns_component[item]["number"] - 1 for item in time_columns_component] 
time_columns_component_name_list: list = [time_columns_component[item]["name"] for item in time_columns_component]
time_columns_component_conversion_list: list = [time_columns_component[item]["conversion"] for item in time_columns_component]

sensor_columns_first_column_index: int = data_stream_config_dict["sensor columns"]["first column number"] - 1
sensor_columns_name: str = data_stream_config_dict["sensor columns"]["name"]

parameter_columns: dict = data_stream_config_dict["parameter columns"]
parameter_columns_index_list: list = [parameter_columns[item]["number"] - 1 for item in parameter_columns]
parameter_columns_name_list: list = [parameter_columns[item]["name"] for item in parameter_columns]
parameter_columns_units_list: list = [parameter_columns[item]["units"] for item in parameter_columns]

parameters_with_units_activated: bool = data_stream_config_dict["parameter with units"]["activated"]
parameter_with_units_separator: str = data_stream_config_dict["parameter with units"]["separator"]
parameters_with_units_before: str = data_stream_config_dict["parameter with units"]["before"]
parameters_with_units_after: str = data_stream_config_dict["parameter with units"]["after"]

markdown_table_parameter_name: str = data_stream_config_dict["markdown table"]["parameter name"]
markdown_table_parameter_align: str = data_stream_config_dict["markdown table"]["parameter align"]
markdown_table_value_name: str = data_stream_config_dict["markdown table"]["value name"]
markdown_table_value_align: str = data_stream_config_dict["markdown table"]["value align"]
markdown_table_separator: str = data_stream_config_dict["markdown table"]["separator"]
markdown_table_column_number: int = data_stream_config_dict["markdown table"]["column number"]
markdown_table_index: int = data_stream_config_dict["markdown table"]["index"]

latest_sensor_data_curves_nrows: int = data_stream_config_dict["latest sensor data"]["curves"]["n rows"]
latest_sensor_data_grids_nrows: int = data_stream_config_dict["latest sensor data"]["grids"]["n rows"]
latest_sensor_data_bars_nrows: int = data_stream_config_dict["latest sensor data"]["bars"]["n rows"]

save_activated: bool = data_stream_config_dict["save"]["activated"]
save_path: str = data_stream_config_dict["save"]["path"]
save_name: str = data_stream_config_dict["save"]["name"]
save_separator: str = data_stream_config_dict["save"]["separator"]
save_time_format: str = data_stream_config_dict["save"]["time format"]
save_format: str = data_stream_config_dict["save"]["format"]
save_sep: str = data_stream_config_dict["save"]["sep"]
save_header: bool = data_stream_config_dict["save"]["header"]
save_index: bool = data_stream_config_dict["save"]["index"]

latest_data_regular_expression_pattern: re.Pattern = re.compile(latest_data_regular_expression + latest_data_format)

if parameters_with_units_activated == True:
    for i_parameter in range(len(parameter_columns_name_list)):
        parameter_columns_name_list[i_parameter] += parameter_with_units_separator
        parameter_columns_name_list[i_parameter] += parameters_with_units_before
        parameter_columns_name_list[i_parameter] += parameter_columns_units_list[i_parameter]
        parameter_columns_name_list[i_parameter] += parameters_with_units_after
        pass
    pass
else:
    pass

markdown_table_name_list: list = list()
markdown_table_align_list: list = list()
# for i in range(markdown_table_column_number):
#     markdown_table_name_list.append(markdown_table_parameter_name + markdown_table_separator + str(i + 1))
#     markdown_table_name_list.append(markdown_table_value_name + markdown_table_separator + str(i + 1))
#     markdown_table_align_list.append(markdown_table_parameter_align)
#     markdown_table_align_list.append(markdown_table_value_align)
#     pass
if markdown_table_column_number == 1:
    markdown_table_name_list.append(markdown_table_parameter_name)
    markdown_table_name_list.append(markdown_table_value_name)
    markdown_table_align_list.append(markdown_table_parameter_align)
    markdown_table_align_list.append(markdown_table_value_align)
    pass
else:
    for i_column in range(markdown_table_column_number):
        markdown_table_name_list.append(markdown_table_parameter_name + markdown_table_separator + str(i_column + 1))
        markdown_table_name_list.append(markdown_table_value_name + markdown_table_separator + str(i_column + 1))
        markdown_table_align_list.append(markdown_table_parameter_align)
        markdown_table_align_list.append(markdown_table_value_align)
        pass
    pass

print("config.backend: DataStreamConfig.py is imported")