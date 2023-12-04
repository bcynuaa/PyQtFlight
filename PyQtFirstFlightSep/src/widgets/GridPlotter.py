'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-31 23:58:42
 # @ description: widgets for GridPlotter
 '''

from PySide2.QtCore import Qt
from PySide2.QtGui import QMouseEvent
from pyvistaqt import QtInteractor

from src.config.libs.PyvistaConfig import *
from src.config.widgets.GridPlotterConfig import *

class GridPlotter(QtInteractor):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.connectWithGrid(pyvista.Sphere())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setMouseReleaseEvent(self, mouse_release_callback: 'function') -> None:
        self.mouse_release_callback: 'function' = mouse_release_callback
        pass
    
    def mouseReleaseEvent(self, mouse_event: QMouseEvent) -> None:
        super().mouseReleaseEvent(mouse_event)
        if mouse_event.button() == Qt.MouseButton.RightButton:
            self.reset_camera()
            self.isometric_view_interactive()
            pass
        self.mouse_release_callback()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def connectWithGrid(self, grid: pyvista.UnstructuredGrid) -> None:
        self.clear()
        self.add_mesh(grid, \
            opacity=pyvista.global_theme.opacity, \
                cmap=pyvista.global_theme.cmap, clim=clim)
        self.add_axes()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("widgets: GridPlotter.py is imported.")