# coding = "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to define a class named MatplotlibWidget, which is used to show in the GUI

# ref: https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html

import numpy as np
from src.MatplotlibSettings import *
from src.ThingsInPlot import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class MatplotlibCanvasWidget:
    
    def __init__(self) -> None:
        """initial the matplotlib canvas widget
        
        create:
            self.figure: matplotlib.figure.Figure
            self.canvas: matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg
            self.axes: matplotlib.axes.Axes
            self.toolbar: matplotlib.backends.backend_qt5agg.NavigationToolbar2QT
        """
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas.parent())
        self.__testPlot()
        pass
    
    def __testPlot(self) -> None:
        """test the matplotlib canvas widget
        
        add test data of: y = sin(x)
        """
        test_data_x: np.ndarray = np.linspace(0, 10, 101)
        test_data_y: np.ndarray = np.sin(test_data_x)
        self.axes.plot(test_data_x, test_data_y, label=DEFAULT_YLABEL)
        self.axes.set_xlabel(DEFAULT_XLABEL)
        self.axes.set_ylabel(DEFAULT_YLABEL)
        self.axes.set_title(DEFAULT_TITLE)
        self.axes.legend()
        self.canvas.draw()
        pass
    
    def clearPlot(self) -> None:
        """clear the plot in the matplotlib canvas widget
        """
        self.axes.clear()
        self.canvas.draw()
        pass
    
    pass

###################################################################################################