# coding = "utf-8"
# author: bcynuaa
# date: 2023/04/27

###################################################################################################
# This file is used to read the data files and plot the data

# ref: 
# - example: https://docs.pyvista.org/version/stable/examples/index.html
# - multiblock: https://docs.pyvista.org/version/stable/api/core/_autosummary/pyvista.MultiBlock.html
# - unstructured grid: https://docs.pyvista.org/version/stable/api/core/_autosummary/pyvista.UnstructuredGrid.html#pyvista-unstructuredgrid
# - plotter: https://docs.pyvista.org/version/stable/api/plotting/_autosummary/pyvista.Plotter.html
# - unstructured 

import os
import numpy as np
# from tqdm import tqdm
from src.PyvistaSettings import *

class MultiBlocksByGenDis:
    
    """the class for the multi-blocks data struct defined by generalized displacement data struct for Prof. Guo
    
    :data_path: the given data path contains the data files
    :active_scalar: the active scalar
    :disp_magnification: the displacement magnification in the plot
    :scalars_clim_dict: the scalar clim's dictionary
    :current_step: the current time step
    :n_blocks: the number of blocks
    :gen_dis_file: the generalized displacement file
    :pressure_file: the pressure file
    :data_file_list: the data file list
    :t: the simulation time array
    :n_steps: the simulation total time step
    :total_time: the simulation total time
    :q: the generalized displacement response matrix, a (n_steps, n_blocks * 6) matrix
    :n_q: the number of generalized displacement response
    :unstructured_grid: the unstructured grid
    :n_points: the number of points
    :n_cells: the number of cells
    :basic_position: the basic position of the unstructured grid
    :n_q_to_display: the number of generalized displacement response to plot
    :phi_3Darray: the generalized displacement response 3D array, a (n_steps, n_points, 3) array
    """
    
    def __init__(self, data_path: str, get_clim: bool = True) -> None:
        """initialize the class

        Args:
            data_path (str): the given data path contains the data files
            get_clim (bool, optional): whether to get the scalars' span. Defaults to True.
        """
        # * data file's directory
        self.data_path: str = data_path
        # * the current time step
        self.current_step: int = 0
        # * the active scalar
        self.active_scalar: str = "Pressure"
        # * the displacement magnification in the plot
        self.displacement_magnification: float = 5000.0
        # * the scalar clim's dictionary
        self.scalars_clim_dict: dict = dict()
        self.scalars_clim_dict["dX"] = None
        self.scalars_clim_dict["dY"] = None
        self.scalars_clim_dict["dZ"] = None
        self.scalars_clim_dict["Pressure"] = None
        self.__filtrateDataFileList()
        self.__findGenDisFile()
        self.__processMultiBlocks()
        if get_clim == True:
            self.__getClim()
            pass
        pass
    
    def __str__(self) -> str:
        """str: return the string of the object

        Returns:
            str: information on console
        """
        s: str = "Multibloks type defined by generalized displacement data struct for Prof. Guo\n"
        s += "data path: " + self.data_path + "\n"
        s += "generalized displacement file: " + self.gen_dis_file + "\n"
        s += "pressure file: " + self.pressure_file + "\n"
        s += "number of blocks: " + str(self.n_blocks) + "\n"
        s += "number of steps: " + str(self.n_steps) + "\n"
        s += "total simulation time: " + str(self.total_time) + "\n"
        s += "current step: " + str(self.current_step) + "\n"
        s += "current active scalar: " + self.active_scalar + "\n"
        s += "displacement magnification: " + str(self.displacement_magnification) + "\n"
        s += "scalar span: " + str(self.scalars_clim_dict) + "\n"
        s += "unstructured grid information: " + str(self.unstructured_grid) + "\n"
        return s
        pass
    
    def __repr__(self) -> str:
        """__repr__: return the string of the object
        """
        return self.__str__()
        pass
    
    def __filtrateDataFileList(self) -> None:
        """delete the file which is not the data file
        """
        data_file_list: list = list()
        cur_file_list: list = os.listdir(self.data_path)
        for item in cur_file_list:
            if item.endswith(".dat"):
                data_file_list.append(item)
                pass
            else:
                pass
            pass
        # * the data file list for all
        self.data_file_list: list = data_file_list
        self.n_blocks: int = len(self.data_file_list) - 2 # ! subtract two files of "Pressure.dat" and "mxxx.dat"
        pass
    
    def __findGenDisFile(self) -> None:
        """__findGenDisFile: find the generalized displacement file and pressure file and add some information
        """
        # * initialize generalized displacement file
        self.gen_dis_file: str = "not_geiven"
        # * initialize pressure file
        self.pressure_file: str = "not_geiven"
        for item in self.data_file_list:
            if item.startswith("m"):
                self.gen_dis_file = item
                pass
            elif item.startswith("P") or item.startswith("p"):
                self.pressure_file = item
                pass
            else:
                pass
            pass
        if self.gen_dis_file in self.data_file_list:
            self.data_file_list.remove(self.gen_dis_file)
            pass
        if self.pressure_file in self.data_file_list:
            self.data_file_list.remove(self.pressure_file)
            pass
        # * generalized displacement file
        self.gen_dis_file: str = os.path.join(self.data_path, self.gen_dis_file)
        # * pressure file
        self.pressure_file: str = os.path.join(self.data_path, self.pressure_file)
        # connect the path before the file name
        self.data_file_list: list = [os.path.join(self.data_path, item) for item in self.data_file_list]
        data: np.ndarray = np.loadtxt(self.gen_dis_file, dtype=np.float64).T
        # * the simulation time array
        self.t: np.ndarray = data[0]
        # * the simulation total time step
        self.n_steps: int = len(self.t)
        # * the simulation total time
        self.total_time: float = self.t[-1]
        # * generalized displacement response matrix, a self.q * self.n_steps matrix
        self.q: np.ndarray = data[1:]
        # * the number of generalized displacement
        self.n_q: int = self.q.shape[0]
        pass
    
    def __processMultiBlocks(self) -> None:
        """__processMultiBlocks: process the multi-blocks data
        """
        multi_blocks: pyvista.core.composite.MultiBlock = pyvista.MultiBlock()
        for item in self.data_file_list:
            multi_blocks.append(
                pyvista.get_reader(item).read()
            )
            pass
        # * the unstructured grid
        self.unstructured_grid: pyvista.UnstructuredGrid = multi_blocks.combine()
        # * the number of points
        self.n_points: int = self.unstructured_grid.n_points
        # * the number of cells
        self.n_cells: int = self.unstructured_grid.n_cells
        # * the basic position of the unstructured grid
        self.basic_position: np.ndarray = np.array(self.unstructured_grid.points, dtype=np.float64)
        param = self.unstructured_grid.point_data.keys()
        param.sort()
        # * the number of generalized displacement response to display
        self.n_q_to_display: int = len(param) // 3
        # ! the list of generalized displacement mdoel, modified on 2023/05/18
        phi_list: list = list()
        for j in range(self.n_q_to_display):
            phi_j: np.ndarray = np.zeros([self.n_points, 3], dtype=np.float64)
            for i in range(3):
                phi_j.T[i] = np.array(
                    self.unstructured_grid.point_data[
                        param[i*self.n_q_to_display + j]
                    ],
                    dtype=np.float64
                )
                pass
            phi_list.append(phi_j)
            pass
        self.phi_3Darray: np.ndarray = np.array(phi_list, dtype=np.float64)
        self.unstructured_grid.clear_point_data() # ! clear the point data to save memory
        self.unstructured_grid.clear_cell_data() # ! clear the cell data to save memory
        self.setStepByIndex(0)
        pass
    
    def __getClim(self) -> None:
        """__getClim: get the clim data stored in dictionary
        """
        self.__getClimDisplacement()
        self.__getClimPressure()
        pass
    
    def __getClimDisplacement(self) -> None:
        """___getClimDisplacement: get the clim data of displacement
        """
        dis_min: np.ndarray = np.zeros([self.n_steps, 3], dtype=np.float64)
        dis_max: np.ndarray = np.zeros([self.n_steps, 3], dtype=np.float64)
        for step in range(self.n_steps):
            self.current_step = step
            displacemnt: np.ndarray = self.__getDisplacementAtCurrentStep()
            dis_min[step] = displacemnt.min(axis=0)
            dis_max[step] = displacemnt.max(axis=0)
            pass
        dis_min = dis_min.min(axis=0)
        dis_max = dis_max.max(axis=0)
        self.scalars_clim_dict["dX"] = [dis_min[0], dis_max[0]]
        self.scalars_clim_dict["dY"] = [dis_min[1], dis_max[1]]
        self.scalars_clim_dict["dZ"] = [dis_min[2], dis_max[2]]
        self.current_step = 0
        pass
    
    def __getClimPressure(self) -> None:
        """__getClimPressure: get the clim data of pressure
        """
        pressure_max: float = np.loadtxt(self.pressure_file, dtype=np.float64).max()
        pressure_min: float = np.loadtxt(self.pressure_file, dtype=np.float64).min()
        self.scalars_clim_dict["Pressure"] = [pressure_min, pressure_max]
        pass
    
    def __limitCurrentStep(self) -> None:
        """__limitCurrentStep: limit the time step
        """
        self.current_step: int = int(np.around(self.current_step))
        if self.current_step < 0:
            self.current_step = 0
            pass
        elif self.current_step > self.n_steps - 1:
            self.current_step = self.n_steps - 1
            pass
        pass
    
    def __timeToStep(self, t: float) -> int:
        """convert the time to step

        Args:
            t (float): given time

        Returns:
            int: the step
        """
        return np.argmin(np.abs(t - self.t))
        pass
    
    def __getDisplacementAtCurrentStep(self) -> np.ndarray:
        """get the displacement at current step

        Returns:
            np.ndarray: current step's displacement
        """
        # displacement: np.ndarray = np.zeros([self.n_points, 3], dtype=np.float64)
        # for i in range(self.n_q_to_display):
        #     displacement += self.q[i][self.current_step] * phi_list[i]
        #     pass
        displacement: np.ndarray = (self.phi_3Darray.T@self.q[0: self.n_q_to_display, self.current_step]).T
        return displacement
        pass
    
    def __getPressureAtCurrentStep(self) -> np.ndarray:
        """get the pressure at current step

        Returns:
            np.ndarray: current step's pressure
        """
        return np.loadtxt(
            self.pressure_file,
            dtype=np.float64,
            skiprows=self.current_step,
            max_rows=1
        )
        pass
    
    def setStepByIndex(self, step: int) -> None:
        self.current_step = step
        self.__limitCurrentStep()
        displacement: np.ndarray = self.__getDisplacementAtCurrentStep()
        pressure: np.ndarray = self.__getPressureAtCurrentStep()
        self.unstructured_grid.points = self.basic_position + displacement * self.displacement_magnification
        self.unstructured_grid.point_data["dX"] = displacement.T[0]
        self.unstructured_grid.point_data["dY"] = displacement.T[1]
        self.unstructured_grid.point_data["dZ"] = displacement.T[2]
        self.unstructured_grid.cell_data["Pressure"] = pressure
        self.unstructured_grid.set_active_scalars(self.active_scalar)
        pass
    
    def setStepByTime(self, t: float) -> None:
        """set the step by time

        Args:
            t (float): given time
        """
        self.setStepByIndex(self.__timeToStep(t))
        return self.unstructured_grid
        pass
    
    def setActivatedScalar(self, scalar: str) -> None:
        """set the activated scalar

        Args:
            scalar (str): the activated scalar
        """
        self.active_scalar = scalar
        self.unstructured_grid.set_active_scalars(self.active_scalar)
        pass
    
    def setDisplacementMagnification(self, magnification: float) -> None:
        """set the displacement magnification

        Args:
            magnification (float): the displacement magnification
        """
        if magnification <= 0.:
            magnification = 1.
            pass
        self.displacement_magnification = magnification
        pass
    
    def setScalarClim(self, scalar_name: str, clim: list) -> None:
        """set the scalar clim

        Args:
            scalar_name (str): the name of scalar
            clim (list): the clim
        """
        self.scalars_clim_dict[scalar_name] = clim
        pass
    
    # ! aborted on 2023/05/09
    def exportGIF(
        self,
        gif_name: str,
        skip_step: int = 1,
        loop: int = 0,
        fps: int = 60,
        whether_show_edges: bool = False,
    ) -> None:
        """export the mp4 file

        Args:
            gif_name (str): the gif_name
            skip_step (int, optional): the skip step. Defaults to 1.
            loop (int, optional): the loop. Defaults to 0.
            fps (int, optional): the fps. Defaults to 60.
            whether_show_edges (bool, optional): whether show edges. Defaults to False.
        """
        skip_step = int(np.around(skip_step))
        if skip_step <= 0:
            skip_step = 1
            pass
        fps = int(np.around(fps))
        if fps <= 0:
            fps = 1
            pass
        if loop < 0:
            loop = 0
            pass
        plotter: pyvista.Plotter = pyvista.Plotter(
            notebook=False,
            off_screen=True,
        )
        plotter.open_gif(gif_name, fps=fps, loop=loop)
        plotter.add_mesh(
            self.unstructured_grid,
            scalars=self.active_scalar,
            clim=self.scalars_clim_dict[self.active_scalar],
            show_edges=whether_show_edges,
            cmap=pyvista.global_theme.cmap
        )
        plotter.add_axes()
        plotter.add_bounding_box()
        plotter.show_grid()
        plotter.write_frame()
        # for j in tqdm( range(0, self.n_steps, skip_step) ):
        for j in range(0, self.n_steps, skip_step):
            self.setStepByIndex(j)
            plotter.write_frame()
            plotter.add_axes()
            plotter.add_bounding_box()
            plotter.show_grid()
            pass
        plotter.close()
        print("successfully export the gif file as " + gif_name)
        pass
    
    # ! aborted on 2023/05/09
    def exportMP4(
        self,
        mp4_name: str,
        skip_step: int = 1,
        framerate: int = 60,
        quality: int = 6,
        whether_show_edges: bool = False,
    ) -> None:
        """export the mp4 file
        
        Args:
            mp4_name (str): the mp4_name
            skip_step (int, optional): the skip step. Defaults to 1.
            framerate (int, optional): the framerate. Defaults to 60.
            quality (int, optional): the quality. Defaults to 6.
            whether_show_edges (bool, optional): whether show edges. Defaults to False.
        """
        skip_step = int(np.around(skip_step))
        if skip_step <= 0:
            skip_step = 1
            pass
        framerate = int(np.around(framerate))
        if framerate <= 0:
            framerate = 1
            pass
        quality = int(np.around(quality))
        if quality <= 0 or quality > 10:
            quality = 6
            pass
        plotter: pyvista.Plotter = pyvista.Plotter(
            notebook=False,
            off_screen=True
        )
        plotter.open_movie(mp4_name, framerate=framerate, quality=quality)
        plotter.add_mesh(
            self.unstructured_grid,
            scalars=self.active_scalar,
            clim=self.scalars_clim_dict[self.active_scalar],
            show_edges=whether_show_edges,
            cmap=pyvista.global_theme.cmap
        )
        plotter.add_axes()
        plotter.add_bounding_box()
        plotter.show_grid()
        plotter.write_frame()
        # for j in tqdm( range(0, self.n_steps, skip_step) ):
        for j in range(0, self.n_steps, skip_step):
            self.setStepByIndex(j)
            plotter.write_frame()
            plotter.add_axes()
            plotter.add_bounding_box()
            plotter.show_grid()
            pass
        plotter.close()
        print("successfully export the mp4 file as " + mp4_name)
        pass
    
    pass

###################################################################################################