'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-30 00:04:44
 # @ description: widgets for CurvesPlotter
 '''

import numpy as np
from PySide2.QtGui import QFont, QPen, QColor
from pglive.sources.live_plot_widget import LivePlotWidget
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.data_connector import DataConnector
from pglive.sources.live_axis import LiveAxis

from src.config.widgets.CurvesPlotterConfig import *

def getPenForCurve(i_curve: int) -> tuple:
    pen_dict: dict = pen_default_dict.copy()
    pen_dict["color"] = pen_color_list[i_curve % len(pen_color_list)]
    return (pen_dict)
    pass

class CurvesPlotter(LivePlotWidget):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.n_curves: int = 0
        self.curves_list: list = []
        self.data_connectors_list: list = []
        self.__makeSettings()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSettings(self) -> None:
        # set
        self.setBackground(background_color)
        self.setMouseEnabled(enable_mouse, enable_mouse)
        self.getPlotItem().setMenuEnabled(enable_menu)
        # set axis
        axis_pen: QPen = QPen(QColor(global_color))
        axis_pen.setWidth(axis_width)
        self.plotItem.getAxis("bottom").setPen(axis_pen)
        self.plotItem.getAxis("left").setPen(axis_pen)
        # set axis items
        left_axis: LiveAxis = LiveAxis("bottom", axisPen=global_color, textPen=global_color)
        bottom_axis: LiveAxis = LiveAxis("left", axisPen=global_color, textPen=global_color)
        self.getPlotItem().setAxisItems({"bottom": left_axis, "left": bottom_axis})
        # set axis font
        font: QFont = QFont()
        font.setPixelSize(pixel_size)
        font.setFamily(global_font_family)
        self.getPlotItem().getAxis("bottom").setTickFont(font)
        self.getPlotItem().getAxis("left").setTickFont(font)
        self.getPlotItem().getAxis("bottom").tickFont = font
        self.getPlotItem().getAxis("left").tickFont = font
        # set axis label
        self.getPlotItem().getAxis("bottom").setLabel( \
            bottom_label, units=bottom_units, unitPrefix=bottom_unitPrefix, **label_dict)
        self.getPlotItem().getAxis("left").setLabel( \
            left_label, units=left_units, unitPrefix=left_unitPrefix, **label_dict)
        # set grid and title
        self.getPlotItem().showGrid(x=grid_x, y=grid_y)
        self.getPlotItem().setTitle(title_name, **title_settings_dict)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setCurvesNumber(self, n_curves: int) -> None:
        for i_curve in range(n_curves):
            curve: LiveLinePlot = LiveLinePlot(pen=getPenForCurve(i_curve))
            data_connector: DataConnector = DataConnector(curve, max_points=max_points)
            self.addItem(curve)
            self.curves_list.append(curve)
            self.data_connectors_list.append(data_connector)
            pass
        self.n_curves = n_curves
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def plot(self, x: np.ndarray, multi_y: np.ndarray) -> None:
        for i_curve in range(self.n_curves):
            self.curves_list[i_curve].clear()
            self.data_connectors_list[i_curve].cb_set_data(multi_y[:, i_curve], x)
            pass
        self.setXRange(x[0], x[-1])
        if y_ticks_limit_activated == True:
            self.setYRange(y_ticks_limit_y_min, y_ticks_limit_y_max)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("widgets: CurvesPlotter is imported")