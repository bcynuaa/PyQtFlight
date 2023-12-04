# coding = "utf-8"
# author: bcynuaa
# date  : 2023/05/04

####################################################################################################
# This file is used to make a interactive layer between the logic and the backend.

import time
from pyvistaqt import QtInteractor, BackgroundPlotter

from src.ReadFile import *
from src.MatplotlibWidget import *
from src.TimerClass import *

class Interactive:
    
    def __init__(self) -> None:
        """initial the interactive layer
        """
        self.whether_show_edges: bool = True
        self.__initialPyvista()
        self.__initialMatplotlib()
        pass
    
    def __initialPyvista(self) -> None:
        self.plotter_interactor: QtInteractor = QtInteractor()
        self.plotter_interactor.add_mesh(pyvista.Sphere(), show_edges=self.whether_show_edges)
        self.plotter_interactor.add_axes()
        self.plotter_interactor.add_bounding_box()
        pass
    
    def __initialMatplotlib(self):
        self.matplotlib_canvas_widget: MatplotlibCanvasWidget = MatplotlibCanvasWidget()
        pass
    
    def loadData(self, data_path: str) -> None:
        """load data from data_path
        """
        self.multi_blocks: MultiBlocksByGenDis = MultiBlocksByGenDis(data_path)
        self.multi_blocks.setActivatedScalar("dZ") # ? todo: set activated scalar
        self.__loadDataMatplotlib()
        self.__loadDataPyvista()
        pass
    
    def __callbackFunctionForUpdateStepWithinTime(self, t: float) -> None:
        self.multi_blocks.setStepByTime(t)
        self.plotter_interactor.add_mesh(
            self.multi_blocks.unstructured_grid,
            scalars=self.multi_blocks.active_scalar,
            clim=self.multi_blocks.scalars_clim_dict[self.multi_blocks.active_scalar],
            show_edges=self.whether_show_edges,
            cmap=pyvista.global_theme.cmap,
            opacity=pyvista.global_theme.opacity,
        )
        self.matplotlib_canvas_widget.axes.set_xlim(self.multi_blocks.t[0], t)
        self.matplotlib_canvas_widget.canvas.draw()
        pass
    
    def __loadDataPyvista(self) -> None:
        """load data and initialize pyvista
        """
        self.plotter_interactor.clear_slider_widgets()
        self.plotter_interactor.clear()
        self.plotter_interactor.add_axes()
        self.plotter_interactor.add_bounding_box()
        self.plotter_interactor.show_grid()
        self.slider = self.plotter_interactor.add_slider_widget(
            self.__callbackFunctionForUpdateStepWithinTime,
            rng = [self.multi_blocks.t[0], self.multi_blocks.t[-1]],
            value=self.multi_blocks.t[0],
            interaction_event="always",
            title="Time (s)",
        )
        self.plotter_interactor.update()
        pass
    
    def __loadDataMatplotlib(self) -> None:
        """load data and initialize matplotlib
        """
        self.matplotlib_canvas_widget.clearPlot()
        for i in range(self.multi_blocks.n_q_to_display):
            self.matplotlib_canvas_widget.axes.plot(
                self.multi_blocks.t,
                self.multi_blocks.q[i],
                label=getYLable(i)
            )
            pass
        self.matplotlib_canvas_widget.axes.legend()
        self.matplotlib_canvas_widget.axes.set_xlabel(DEFAULT_XLABEL)
        self.matplotlib_canvas_widget.axes.set_ylabel(DEFAULT_YLABEL)
        self.matplotlib_canvas_widget.axes.set_title(DEFAULT_YLABEL)
        self.matplotlib_canvas_widget.canvas.draw()
        pass
    
    def newPyvistaWindow(self) -> None:
        background_plotter: BackgroundPlotter = BackgroundPlotter()
        background_plotter.add_mesh(
            self.multi_blocks.unstructured_grid,
            scalars=self.multi_blocks.active_scalar,
            clim=self.multi_blocks.scalars_clim_dict[self.multi_blocks.active_scalar],
            show_edges=self.whether_show_edges
        )
        background_plotter.add_menu_bar()
        background_plotter.add_toolbars()
        background_plotter.show()
        pass
    
    def newMatplotlibOneCurve(self, index: int) -> None:
        ylabel: str = getYLable(index)
        fig = plt.figure()
        axes = fig.add_subplot(111)
        axes.plot(self.multi_blocks.t, self.multi_blocks.q[index], label=ylabel)
        axes.set_xlabel(DEFAULT_XLABEL)
        axes.set_ylabel(ylabel)
        axes.set_title(DEFAULT_XLABEL + "-" + ylabel)
        axes.legend()
        fig.show()
        pass
    
    def newMatplotlibMultiCurvesAllInOne(self, index_list: list) -> None:
        fig = plt.figure()
        axes = fig.add_subplot(111)
        for i in index_list:
            ylabel: str = getYLable(i)
            axes.plot(self.multi_blocks.t, self.multi_blocks.q[i], label=ylabel)
            pass
        axes.set_xlabel(DEFAULT_XLABEL)
        axes.set_ylabel(DEFAULT_YLABEL)
        axes.set_title(DEFAULT_XLABEL + "-" + DEFAULT_YLABEL)
        axes.legend()
        fig.show()
        pass
    
    def newMatplotlibMultiCurvesSplit(self, index_list: list) -> None:
        N: int = len(index_list)
        ncols: int = int( np.floor(np.sqrt(N)) )
        nrows: int = int( np.ceil(N/ncols) )
        fig = plt.figure()
        for j in range(N):
            i = index_list[j]
            ylabel: str = getYLable(i)
            axes = fig.add_subplot(nrows, ncols, j+1)
            axes.plot(self.multi_blocks.t, self.multi_blocks.q[i], label=ylabel)
            axes.set_xlabel(DEFAULT_XLABEL)
            axes.set_ylabel(ylabel)
            axes.set_title(ylabel)
            pass
        fig.show()
        pass
    
    def refresh(self) -> None:
        self.__loadDataMatplotlib()
        self.__loadDataPyvista()
        pass
    
    def autoDisplay(self, skip_step: int = 10, fps: float = 60) -> None:
        sleep_time: float = 1.0 / fps
        def callbackIndexFunction(step: int) -> None:
            t: float = self.multi_blocks.t[step]
            self.slider.GetSliderRepresentation().SetValue(t)
            self.__callbackFunctionForUpdateStepWithinTime(t)
            time.sleep(sleep_time)
            pass
        self.auto_display_timer: AutoDisplayTimer = AutoDisplayTimer(
            callbackIndexFunction,
            skip_step,
            0,
            self.multi_blocks.n_steps
        )
        self.auto_display_timer.start()
        pass
    
    pass

####################################################################################################