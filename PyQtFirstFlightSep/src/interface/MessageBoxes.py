'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 00:09:33
 # @ description: interface for MessageBoxes
 '''

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QMessageBox

from src.config.interface.MessageBoxesConfig import *

# -------------------------------------------------------------------------------------------------

def loadJsonFileSucceededQMessageBox(parent: QObject, n_modes: int, n_sensors: int) -> QMessageBox:
    return QMessageBox.information(parent, \
        load_json_file_succeeded_window_title, \
        load_json_file_succeeded_message % (n_modes, n_sensors))
    pass

def loadJsonFileFailedQMessageBox(parent: QObject) -> QMessageBox:
    return QMessageBox.warning(parent, \
        load_json_file_failed_window_title, load_json_file_failed_message)
    pass

# -------------------------------------------------------------------------------------------------

def saveDataStreamQMessageBox(parent: QObject, data_stream_filename: str) -> QMessageBox:
    return QMessageBox.information(parent, \
        save_data_stream_window_title, save_data_stream_message % data_stream_filename)
    pass

def clearDataStreamQMessageBox(parent: QObject) -> QMessageBox:
    return QMessageBox.information(parent, \
        clear_data_stream_window_title, clear_data_stream_message)
    pass

# -------------------------------------------------------------------------------------------------

def startMonitoringQMessageBox(parent: QObject, monitor_path: str) -> QMessageBox:
    return QMessageBox.information(parent, \
        start_monitoring_window_title, start_monitoring_message % monitor_path)
    pass

def alreadyMonitoringQMessageBox(parent: QObject, monitor_path: str) -> QMessageBox:
    return QMessageBox.information(parent, \
        already_monitoring_window_title, already_monitoring_message % monitor_path)
    pass

def endMonitoringQMessageBox(parent: QObject, monitor_path: str) -> QMessageBox:
    return QMessageBox.information(parent, \
        end_monitoring_window_title, end_monitoring_message % monitor_path)
    pass

def replayFinishedQMessageBox(parent: QObject) -> QMessageBox:
    return QMessageBox.information(parent, \
        replay_finished_window_title, replay_finished_message)
    pass

# -------------------------------------------------------------------------------------------------

print("interface: MessageBoxes.py is imported")