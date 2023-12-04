'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-31 15:38:55
 # @ description: widgets for BarsPlotter
 '''

import numpy as np
from PySide2.QtGui import QFont, QPen, QBrush, QColor
from pyqtgraph import TextItem
from pglive.sources.live_plot_widget import LivePlotWidget
from pglive.sources.live_plot import LiveVBarPlot, LiveLinePlot
from pglive.sources.data_connector import DataConnector
from pglive.sources.live_axis import LiveAxis

from src.config.widgets.BarsPlotterConfig import *

class BarsPlotter(LivePlotWidget):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
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
        self.left_axis: LiveAxis = LiveAxis("bottom", axisPen=global_color, textPen=global_color)
        self.bottom_axis: LiveAxis = LiveAxis("left", axisPen=global_color, textPen=global_color)
        self.getPlotItem().setAxisItems({"bottom": self.left_axis, "left": self.bottom_axis})
        # set axis font
        self.font: QFont = QFont()
        self.font.setPixelSize(pixel_size)
        self.font.setFamily(global_font_family)
        self.getPlotItem().getAxis("bottom").setTickFont(self.font)
        self.getPlotItem().getAxis("left").setTickFont(self.font)
        self.getPlotItem().getAxis("bottom").tickFont = self.font
        self.getPlotItem().getAxis("left").tickFont = self.font
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
    
    def __makeXTicks(self) -> None:
        self.x_ticks: list = [x_ticks_name + x_ticks_separator + str(i+1) \
            for i in range(self.n_bars)]
        if x_ticks_auto == True:
            pass
        else:
            if len(x_ticks_custom) > self.n_bars:
                self.x_ticks = x_ticks_custom[0: self.n_bars]
                pass
            elif len(x_ticks_custom) < self.n_bars:
                self.x_ticks[0: len(x_ticks_custom)] = x_ticks_custom
                pass
            else:
                self.x_ticks = x_ticks_custom
                pass
            pass
        self.getPlotItem().getAxis("bottom").setTicks( \
            [list(zip(self.bars_x_positions, self.x_ticks))])
        self.x_min: float = self.bars_x_positions.min() - bars_width
        self.x_max: float = self.bars_x_positions.max() + bars_width
        self.setXRange(self.x_min, self.x_max)
        pass
    
    def __makeCrucialLinePlot(self) -> None:
        self.line_plot: LiveLinePlot = LiveLinePlot(max_points=2, pen=(crucial_line_pen_dict))
        self.addItem(self.line_plot)
        self.line_plot_data_connector: DataConnector = DataConnector(self.line_plot, \
            max_points=2)
        self.line_plot_data_connector.cb_set_data( \
            [crucial_line_y_position, crucial_line_y_position], [self.x_min, self.x_max])
        pass
    
    def __makeBarsPlot(self) -> None:
        self.vertical_bar_plot: LiveVBarPlot = LiveVBarPlot(max_points=self.n_bars, \
            bar_width=bars_width, bar_spacing=bars_spacing, y0=bars_y0, \
                pen=(bars_pen_dict), brush=QBrush(QColor(bars_brush_color)))
        self.vertical_bar_data_connector: DataConnector = DataConnector(self.vertical_bar_plot, \
            max_points=self.n_bars)
        self.addItem(self.vertical_bar_plot)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeAdditionalThingsText(self) -> None:
        self.text_item_list: list = []
        self.text_item_font_list: list = []
        for text_item_dict in additional_things_text["values"]:
            font: QFont = QFont()
            font.setPixelSize(text_item_dict["pixel size"])
            font.setFamily(text_item_dict["font-family"])
            text_item: TextItem = TextItem(text_item_dict["text"], color=text_item_dict["color"], \
                border=text_item_dict["border"], fill=text_item_dict["fill"])
            text_item.setFont(font)
            self.text_item_font_list.append(font)
            self.text_item_list.append(text_item)
            self.addItem(text_item)
            text_item.setPos(text_item_dict["pos"][0] - additional_things_text["shared x shift"] \
                , text_item_dict["pos"][1])
            pass
        pass
    
    def __makeAdditionalThingsVerticalLine(self) -> None:
        self.vertical_line_list: list = []
        self.vertical_line_data_connector_list: list = []
        for vertical_line in additional_things_vertical_line["values"]:
            vertical_line_plot: LiveLinePlot = LiveLinePlot(max_points=2, pen=(vertical_line["pen"]))
            vertical_line_data_connector: DataConnector = DataConnector(vertical_line_plot, \
                max_points=2)
            self.vertical_line_list.append(vertical_line_plot)
            self.vertical_line_data_connector_list.append(vertical_line_data_connector)
            self.addItem(vertical_line_plot)
            after_bar_index: int = vertical_line["after bar number"] - 1
            if after_bar_index >= self.n_bars:
                after_bar_index = self.n_bars - 2
                pass
            x_pos: float = (self.bars_x_positions[after_bar_index] \
                + self.bars_x_positions[after_bar_index + 1]) / 2
            vertical_line_data_connector.cb_set_data( \
                [vertical_line["y min"], vertical_line["y max"]], \
                    [x_pos, x_pos])
            pass
        pass
    
    def __makeAdditionalThings(self) -> None:
        if additional_things_text["activated"] == True:
            self.__makeAdditionalThingsText()
            pass
        if additional_things_vertical_line["activated"] == True:
            self.__makeAdditionalThingsVerticalLine()
            pass
        pass
    
    def setBarsNumber(self, n_bars: int) -> None:
        self.bars_x_positions: np.ndarray = np.arange(bars_first_bar_x_position, \
            bars_first_bar_x_position + n_bars * (bars_width + bars_spacing), \
                bars_width + bars_spacing)
        self.n_bars: int = n_bars
        self.__makeBarsPlot()
        self.__makeXTicks()
        if crucial_line_activated == True:
            self.__makeCrucialLinePlot()
            pass
        self.__makeAdditionalThings()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def plot(self, bars_values: np.ndarray) -> None:
        self.vertical_bar_data_connector.cb_set_data(bars_values, self.bars_x_positions)
        self.setXRange(self.x_min, self.x_max)
        if y_ticks_use_fixed_range == True:
            self.setYRange(y_ticks_min, y_ticks_max)
            pass
        else:
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("widgets: BarsPlotter is imported")