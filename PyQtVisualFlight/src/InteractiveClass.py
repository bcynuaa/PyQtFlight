# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to contain the interactive class

from pyvistaqt import BackgroundPlotter, QtInteractor

from config.Base import *
from config.PyvistaSettings import *
from config.MatplotlibSettings import *

from utils.FileObserver import WatchDog

from src.MeshClass import MeshByGenDis
from src.MatplotlibClass import TimeDomainCanvas, FrequencyDomainCanvas

class Interactive:
    
    #------------------------------------------------------------------------------------
    
    def __init__(self, flag: str = DEFAULT_RHS_NAME) -> None:
        # * the flag is used to determine which data to be loaded
        self.flag: str = flag
        # * whether show edges
        self.whether_show_edges: bool = True
        # * whether domains loaded
        self.whether_domains_loaded: bool = False
        self.whether_watchdog_defined: bool = False
        # * whether in updating
        self.whether_in_updating: bool = False
        # * whether finished updating
        self.whether_finished_updating: bool = False
        self.__initializePyvista()
        self.__initializeMatplotlib()
        pass
    
    def __initializePyvista(self) -> None:
        """initialize pyvista
        """
        self.plotter_interactor: QtInteractor = QtInteractor()
        self.plotter_interactor.add_mesh(pyvista.Sphere(), show_edges=self.whether_show_edges)
        self.plotter_interactor.add_axes()
        self.plotter_interactor.add_bounding_box()
        pass
    
    def __initializeMatplotlib(self):
        self.time_domain_canvas: TimeDomainCanvas = TimeDomainCanvas()
        self.frequency_domain_canvas: FrequencyDomainCanvas = FrequencyDomainCanvas()
        pass
    
    #------------------------------------------------------------------------------------
    
    def loadDomainFiles(self, data_path: str) -> None:
        self.mesh: MeshByGenDis = MeshByGenDis(data_path, self.flag)
        self.whether_domains_loaded = True
        self.__updatePyvsitaWhenDomainLoaded()
        pass
    
    def __updatePyvsitaWhenDomainLoaded(self) -> None:
        self.plotter_interactor.clear_slider_widgets()
        self.plotter_interactor.clear()
        self.plotter_interactor.add_mesh(
            self.mesh.unstructured_grid,
            scalars=self.mesh.active_scalar,
            show_edges=self.whether_show_edges,
            cmap=pyvista.global_theme.cmap,
            opacity=pyvista.global_theme.opacity,
        )
        self.plotter_interactor.add_axes()
        self.plotter_interactor.add_bounding_box()
        self.plotter_interactor.show_grid()
        pass
    
    #------------------------------------------------------------------------------------
    
    def setStepByLimitTime(self, time_limit: float) -> None:
        if self.mesh.getCurrentTime() <= time_limit:
            self.mesh.setStepByLimitTime(time_limit)
            self.time_domain_canvas.plot(
                self.mesh.t[0: self.mesh.current_step],
                self.mesh.gen_dis_response[:, 0: self.mesh.current_step],
            )
            print(self.flag, " current step: ", self.mesh.current_step)
            print(self.flag, " total time: ", self.mesh.total_time)
            # * self.frequency_domain_canvas...
            pass
        pass
    
    # test file: ./draft//callback_test.ipynb
    # ! it's the most cofusing part in my code
    def defineWatchDog(self, gen_dis_file_path: str, getTimeLimitFunction) -> None:
        self.mesh.connectToGenDisFilePath(gen_dis_file_path)
        def callbackFunctionInUpdateForWatchDog() -> None:
            while self.whether_in_updating == True:
                try:
                    self.mesh.updateGenDisFile()
                    time_limit: float = getTimeLimitFunction()
                    self.setStepByLimitTime(time_limit)
                    pass
                except:
                    pass
                pass
            pass
        self.callbackFunctionInUpdateForWatchDog = callbackFunctionInUpdateForWatchDog
        self.watchdog: WatchDog = WatchDog(
            self.mesh.gen_dis_file_path,
            callback_on_modified=self.callbackFunctionInUpdateForWatchDog,
        )
        self.whether_watchdog_defined = True
        pass
    
    #------------------------------------------------------------------------------------
    
    pass

print("Successfully import Interactive.py")

###################################################################################################