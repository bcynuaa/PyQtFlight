'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 03:35:31
 # @ description: interface for FileDialogs
 '''

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QFileDialog

from src.config.interface.FileDialogsConfig import *

def loadJsonFileQFileDialog(parent: QObject) -> QFileDialog:
    return QFileDialog.getOpenFileName(parent, load_json_file_window_title, \
        load_json_file_default_path, load_json_file_filter)
    pass

def saveDataStreamQFileDialog(parent: QObject) -> QFileDialog:
    return QFileDialog.getSaveFileName(parent, save_data_stream_window_title, \
        save_data_stream_default_filename, save_data_stream_filter)
    pass

print("interface: FileDialogs.py is imported")