# coding = "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to define a class named MatplotlibWidget, which is used to show in the GUI

# ref: https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html

import numpy as np

from config.MatplotlibSettings import *
from config.ThingsInMatplotlib import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class MatplotlibCanvasWidget:
    
    def __init__(self) -> None:
        """initialize the matplotlib canvas widget
        
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
        self.test_x: np.ndarray = np.linspace(0, 10, 100)
        self.test_y: np.ndarray = np.sin(self.test_x)
        self.initializePlot()
        pass
    
    def initializePlot(self) -> None:
        self.plot(self.test_x, self.test_y)
        pass
    
    def plot(self, x: np.array, y: np.array) -> None:
        pass
    
    def clearPlot(self) -> None:
        """clear the plot in the matplotlib canvas widget
        """
        self.axes.clear()
        self.canvas.draw()
        pass
    
    def setXLim(self, xlim: tuple) -> None:
        """set the xlim
        
        Args:
            xlim (tuple): xlim
        """
        self.axes.set_xlim(xlim)
        self.canvas.draw()
        pass
    
    pass

###################################################################################################

class TimeDomainCanvas(MatplotlibCanvasWidget):
    
    def __init__(self) -> None:
        """initialize the matplotlib canvas widget for time domain
        
        create:
            self.figure: matplotlib.figure.Figure
            self.canvas: matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg
            self.axes: matplotlib.axes.Axes
            self.toolbar: matplotlib.backends.backend_qt5agg.NavigationToolbar2QT
        """
        super().__init__()
        self.axes.set_xlabel(TIMEDOMAIN_XLABEL)
        self.axes.set_ylabel(TIMEDOMAIN_YLABEL)
        self.axes.set_title(TIMEDOMAIN_TITLE)
        self.initializePlot()
        pass
    
    def plot(self, t_array: np.ndarray, q_array: np.ndarray) -> None:
        """plot the figure
        
        Args:
            t_array (np.ndarray): t data
            q_array (np.ndarray): q data
        """
        self.axes.clear()
        if q_array.ndim == 1:
            self.axes.plot(t_array, q_array, label=getTimeDomainYlabel(-1))
            pass
        else:
            for k in range(len(q_array)):
                self.axes.plot(t_array, q_array[k], label=getTimeDomainYlabel(k))
                pass
            pass
        self.axes.set_xlabel(TIMEDOMAIN_XLABEL)
        self.axes.set_ylabel(TIMEDOMAIN_YLABEL)
        self.axes.set_title(TIMEDOMAIN_TITLE)
        self.axes.legend()
        self.canvas.draw()
        pass
    
    pass

class FrequencyDomainCanvas(MatplotlibCanvasWidget):
    
    def __init__(self) -> None:
        """initialize the matplotlib canvas widget for frequency domain
        
        create:
            self.figure: matplotlib.figure.Figure
            self.canvas: matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg
            self.axes: matplotlib.axes.Axes
            self.toolbar: matplotlib.backends.backend_qt5agg.NavigationToolbar2QT
        """
        super().__init__()
        self.axes.set_xlabel(FREQUENCYDOMAIN_XLABEL)
        self.axes.set_ylabel(FREQUENCYDOMAIN_YLABEL)
        self.axes.set_title(FREQUENCYDOMAIN_TITLE)
        self.initializePlot()
        pass
    
    def plot(self, f_array: np.ndarray, q_array: np.ndarray) -> None:
        """plot the figure
        
        Args:
            f_array (np.ndarray): f data
            q_array (np.ndarray): q data
        """
        self.axes.clear()
        if q_array.ndim == 1:
            self.axes.plot(f_array, q_array, label=getFrequencyDomainYlabel(-1))
            pass
        else:
            for k in range(len(q_array)):
                self.axes.plot(f_array, q_array[k], label=getFrequencyDomainYlabel(k))
                pass
            pass
        self.axes.legend()
        self.axes.set_xlabel(FREQUENCYDOMAIN_XLABEL)
        self.axes.set_ylabel(FREQUENCYDOMAIN_YLABEL)
        self.axes.set_title(FREQUENCYDOMAIN_TITLE)
        self.canvas.draw()
        pass
    
    pass

print("Successfully import MatplotlibClass.py")

###################################################################################################