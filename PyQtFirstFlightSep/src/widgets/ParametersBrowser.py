'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-29 14:31:05
 # @ description: widgets for ParametersBrowser
 '''

import numpy as np
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTextBrowser

from src.config.widgets.ParametersBrowserConfig import *

from src.utils.QSSModify import setFontSizeToQss

class ParametersBrowser(QTextBrowser):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.setParametersMarkdownTable("")
        self.__makeSettings()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSettings(self) -> None:
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.setMaximumWidth(size_maximum_width)
        self.setMaximumHeight(size_maximum_height)
        self.setMinimumWidth(size_minimum_width)
        self.setMinimumHeight(size_minimum_height)
        self.setStyleSheet(parameters_browser_config_style)
        pass
    
    # ---------------------------------------------------------------------------------------------

    def setParametersMarkdownTable(self, markdown_table: str) -> None:
        self.markdown_text: str = additional_text_before + markdown_table + additional_text_after
        self.setMarkdown(self.markdown_text)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setFontSize(self, font_size: float) -> None:
        font_size: int = int(np.floor(font_size))
        qss_modified: str = setFontSizeToQss(parameters_browser_config_style, font_size)
        self.setStyleSheet(qss_modified)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("widgets: ParametersBrowser.py is imported.")