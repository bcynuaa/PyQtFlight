# coding = "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to test the MatplotlibWidget

from test_Header import *
import src.MatplotlibWidget as MatplotlibWidget

mw: MatplotlibWidget.MatplotlibCanvasWidget = MatplotlibWidget.MatplotlibCanvasWidget()
mw.canvas.show()

###################################################################################################
# expected results

# workspace directory included
# successfully set the global theme of matplotlib.

# successfully generate basic things in plot.
