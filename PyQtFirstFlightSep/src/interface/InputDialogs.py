'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-13 17:22:29
 # @ description: interface for InputDialogs
 '''

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QInputDialog

from src.config.interface.InputDialogsConfig import *

def replayStartRowQInputDialog(parent: QObject, \
    default_int: int, min_int: int, max_int: int) -> QInputDialog:
    return QInputDialog.getInt(parent, \
        replay_start_row_window_title, replay_start_row_label_text, \
            default_int, min_int, max_int, 1)
    pass

def replayEndRowQInputDialog(parent: QObject, \
    default_int: int, min_int: int, max_int: int) -> QInputDialog:
    return QInputDialog.getInt(parent, \
        replay_end_row_window_title, replay_end_row_label_text, \
            default_int, min_int, max_int, 1)
    pass

def replayIntervalRowQInputDialog(parent: QObject, \
    default_int: int, min_int: int, max_int: int) -> QInputDialog:
    return QInputDialog.getInt(parent, \
        replay_interval_row_window_title, replay_interval_row_label_text, \
            default_int, min_int, max_int, 1)
    pass

print("interface: InputDialogs.py is imported")