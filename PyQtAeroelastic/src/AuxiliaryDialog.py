# coding = "utf-8"
# author： bcynuaa
# date  : 2023/05/09

###################################################################################################
# This file is used to generate auxiliary dialog

import numpy as np
from src.MatplotlibWidget import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# ref:
# https://blog.csdn.net/jia666666/article/details/81534260
# https://blog.csdn.net/zyx4843/article/details/50698133

class CmapChosenDialog(QDialog):
    
    def __init__(self, current_cmap: str = "jet"):
        super().__init__()
        self.current_cmap: str = current_cmap
        self.setWindowTitle(u"Cmap Chose Dialog")
        self.resize(400, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.__initialCmapChosen()
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        pass
    
    def __initialCmapChosen(self):
        self.__initialMatplotlib()
        self.__initialComboBox()
        self.__showCurrentCmap()
        pass
    
    def __initialMatplotlib(self):
        self.matplotlib_canvas_widget = MatplotlibCanvasWidget()
        self.layout.addWidget(self.matplotlib_canvas_widget.toolbar)
        self.layout.addWidget(self.matplotlib_canvas_widget.canvas)
        x: np.ndarray = np.linspace(0, 10, 100)
        y: np.ndarray = x
        X, Y = np.meshgrid(x, y)
        self.cmap_show_data: np.ndarray = X + Y
        pass
    
    def __initialComboBox(self):
        self.cmap_chosen_combo_box = QComboBox()
        self.cmap_chosen_combo_box.addItems(cmap_option_list)
        self.cmap_chosen_combo_box.setCurrentText(self.current_cmap)
        self.cmap_chosen_combo_box.currentIndexChanged.connect(self.__showCurrentCmap)
        self.layout.addWidget(self.cmap_chosen_combo_box)
        pass
    
    def __showCurrentCmap(self):
        self.current_cmap = self.cmap_chosen_combo_box.currentText()
        self.matplotlib_canvas_widget.clearPlot()
        self.matplotlib_canvas_widget.axes.imshow(self.cmap_show_data, cmap=self.current_cmap)
        self.matplotlib_canvas_widget.canvas.draw()
        pass
    
    def accept(self) -> str:
        self.close()
        return self.current_cmap
        pass
    
    pass

###################################################################################################

class SetScalarClimDialog(QDialog):
    
    def __init__(self, current_scalar: str, scalars_clim_dict: dict) -> None:
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle(u"Set Scalar Clim Dialog")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.scalars_clim_dict: dict = scalars_clim_dict
        self.scalars_list: list = list(scalars_clim_dict.keys())
        self.current_scalar: str = current_scalar
        self.__initialComboBox()
        self.__initialTextEdits()
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        pass
    
    def __initialComboBox(self):
        self.layout.addWidget(QLabel("选择云图参数:"))
        self.scalar_chosen_combo_box = QComboBox()
        self.scalar_chosen_combo_box.addItems(self.scalars_list)
        self.layout.addWidget(self.scalar_chosen_combo_box)
        pass
    
    def __initialTextEdits(self):
        self.layout.addWidget(QLabel("设置云图参数最小值:"))
        self.min_text_editor = QLineEdit()
        self.layout.addWidget(self.min_text_editor)
        self.layout.addWidget(QLabel("设置云图参数最大值:"))
        self.max_text_editor = QLineEdit()
        self.layout.addWidget(self.max_text_editor)
        
        self.min_text_editor.setValidator(
            QRegExpValidator(
                QRegExp("^(-?\d+)(\.\d+)?$")
            )
        )
        self.max_text_editor.setValidator(
            QRegExpValidator(
                QRegExp("^(-?\d+)(\.\d+)?$")
            )
        )
        self.scalar_chosen_combo_box.currentIndexChanged.connect(self.__curentScalarChange)
        self.__curentScalarChange()
        pass
    
    def __curentScalarChange(self) -> None:
        self.current_scalar = self.scalar_chosen_combo_box.currentText()
        self.min_text_editor.setText(str(self.scalars_clim_dict[self.current_scalar][0]))
        self.max_text_editor.setText(str(self.scalars_clim_dict[self.current_scalar][1]))
        pass
    
    def accept(self):
        current_scalar_clim: list = list()
        current_scalar_clim.append(
            float(
                eval(self.min_text_editor.text())
            )
        )
        current_scalar_clim.append(
            float(
                eval(self.max_text_editor.text())
            )
        )
        self.close()
        return self.current_scalar, current_scalar_clim
        pass
    
    pass

print("Successfully import auxiliary dialog!")

###################################################################################################