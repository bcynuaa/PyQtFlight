'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-08 19:24:46
 # @ license: Mozilla Public License 2.0
 # @ description: the class of matplotlib canvas
 '''

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from config.Name import *
from config.MatplotlibSettings import *

class MatplotlibCanvas:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas.parent())
        self.test_x: np.ndarray = np.linspace(0, 10, 100)
        self.test_y: np.ndarray = np.sin(self.test_x)
        self.plot(self.test_x, self.test_y)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def plot(self, x: np.ndarray, y: np.ndarray) -> None:
        pass
    
    def clearPlot(self) -> None:
        self.axes.clear()
        self.canvas.draw()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setXLim(self, xlim: tuple) -> None:
        self.axes.set_xlim(xlim)
        self.canvas.draw()
        pass
    
    def setYLim(self, ylim: tuple) -> None:
        self.axes.set_ylim(ylim)
        self.canvas.draw()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

class TimeDomainCanvas(MatplotlibCanvas):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.axes.set_xlabel(kTime_Domain_XLabel)
        self.axes.set_ylabel(kTime_Domain_YLabel)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def plot(self, x: np.ndarray, y: np.ndarray) -> None:
        self.axes.clear()
        if y.ndim == 1:
            self.axes.plot(x, y, label=getYlabel(-1))
            pass
        else:
            for k in range(len(y)):
                self.axes.plot(x, y[k], label=getYlabel(k))
                pass
            pass
        self.axes.grid(True)
        self.axes.set_xlabel(kTime_Domain_XLabel)
        self.axes.set_ylabel(kTime_Domain_YLabel)
        self.axes.legend()
        self.canvas.draw()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

class FrequencyDomainCanvas(MatplotlibCanvas):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.axes.set_xlabel(kFrequency_Domain_XLabel)
        self.axes.set_ylabel(kFrequency_Domain_YLabel)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def plot(self, x: np.ndarray, y: np.ndarray) -> None:
        self.axes.clear()
        if y.ndim == 1:
            self.axes.plot(x, y, label=getYlabel(-1))
            pass
        else:
            for k in range(len(y)):
                self.axes.plot(x, y[k], label=getYlabel(k))
                pass
            pass
        self.axes.grid(True)
        self.axes.set_xlabel(kFrequency_Domain_XLabel)
        self.axes.set_ylabel(kFrequency_Domain_YLabel)
        self.axes.legend()
        self.canvas.draw()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: MatplotlibCanvasClass.py is imported.")