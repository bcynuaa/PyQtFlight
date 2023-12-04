# coding: "utf-8"
# author: bcynuaa
# date: 2035/05/18

###################################################################################################
# This file is used to read the domains from the data

import os
import numpy as np

from config.PyvistaSettings import *
from config.Base import *
from utils.PatternMatch import *

class MeshByGenDis:
    
    """the class for the mesh data class defined by generalized displacement data structure for Prof. Guo
    
    :flag: str -> the flag of the data
    :data_path: str -> the path of the data
    :current_step: int -> the current step
    :active_scalar: str -> the active scalar
    :displacement_magnification: float -> the magnification of the displacement
    :scalars_clim_dict: dict -> the clim of the scalars, including "dX", "dY", "dZ"
    :scalars_list: list -> the list of the scalars, including "dX", "dY", "dZ"
    
    :domain_files_list: list -> the list of the domain data file
    :n_domains: int -> the number of the domains
    :unstructured_grid: pyvista.UnstructuredGrid -> the unstructured grid
    :n_points: int -> the number of points
    :n_cells: int -> the number of cells
    :basic_position: np.ndarray -> the basic position of the unstructured grid
    :n_gen_dis: int -> the number of generalized displacement response
    :phi_3Darray: np.ndarray -> the generalized displacement response
    
    :gen_dis_file_path: str -> the file path of the generalized displacement
    :gen_dis_file: str -> the file of the generalized displacement
    :t: np.ndarray -> the time of the data
    :n_steps: int -> the number of the steps
    :total_time: float -> the total time of the simulation
    :gen_dis_response: np.ndarray -> the generalized displacement response
    """
    
    #------------------------------------------------------------------------------------
    
    def __init__(self, data_path: str, flag :str = DEFAULT_RHS_NAME) -> None:
        """__init__: initialize the MeshByGenDis class

        Args:
            data_path (str): _description_
        """
        self.__initializeDefaultValue(data_path, flag)
        self.__filtrateDataFileList()
        self.__processDomains()
        self.__initializeDefaultValueOfGenDis()
        pass
    
    def __str__(self) -> str:
        """__str__: return the string of the class

        Returns:
            str: return information of the class
        """
        s: str = "====================================================================================================\n\n"
        s += "Mesh data class defined by generalized displacement data structure for Prof. Guo\n"
        s += "Mesh flag: " + self.flag + "\n"
        s += "data path: " + self.data_path + "\n"
        s += "generalized displacement file: " + self.gen_dis_file + "\n"
        s += "number of blocks: " + str(self.n_domains) + "\n"
        s += "number of steps: " + str(self.n_steps) + "\n"
        s += "total simulation time: " + str(self.total_time) + "\n"
        s += "current step: " + str(self.current_step) + "\n"
        s += "current active scalar: " + self.active_scalar + "\n"
        s += "displacement magnification: " + str(self.displacement_magnification) + "\n"
        s += "scalar span: " + str(self.scalars_clim_dict) + "\n"
        s += "unstructured grid information: " + str(self.unstructured_grid) + "\n"
        s += "===================================================================================================="
        return s
        pass
    
    def __repr__(self) -> str:
        """__repr__: return the string of the class

        Returns:
            str: return information of the class
        """
        return self.__str__()
        pass
    
    def __initializeDefaultValue(self, data_path: str, flag: str) -> None:
        """__initializeDefaultValue: initialize the default value

        Args:
            data_path (str): _description_
        """
        # * the flag of the data
        self.flag: str = flag
        # * the path of the data
        self.data_path: str = data_path
        # * the list of the data file
        self.current_step: int = 0
        # * the list of the data file
        self.active_scalar: str = "dZ"
        # * the magnification of the displacement
        self.displacement_magnification: float = 0.01
        # * # the clim of the scalars
        self.scalars_clim_dict: dict = dict()
        self.scalars_clim_dict["dX"] = np.array([0., 0.])
        self.scalars_clim_dict["dY"] = np.array([0., 0.])
        self.scalars_clim_dict["dZ"] = np.array([0., 0.])
        # * the list of scalars
        self.scalars_list: list = list(self.scalars_clim_dict.keys())
        pass
    
    def __filtrateDataFileList(self) -> None:
        """delete the file which is not the data file
        """
        cur_file_list: list = os.listdir(self.data_path)
        # * the list of the domain data file
        self.domain_files_list: list = getDomainFilesList(cur_file_list)
        for i in range(len(self.domain_files_list)):
            self.domain_files_list[i] = os.path.join(self.data_path, self.domain_files_list[i])
            pass
        # * the number of the domains
        self.n_domains: int = len(self.domain_files_list)
        pass
    
    def __processDomains(self) -> None:
        multi_blocks: pyvista.core.composite.MultiBlock = pyvista.MultiBlock()
        for item in self.domain_files_list:
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
        # * the number of generalized displacement response
        self.n_gen_dis: int = len(param) // 3
        phi_list: list = list()
        for j in range(self.n_gen_dis):
            phi_j: np.ndarray = np.zeros([self.n_points, 3], dtype=np.float64)
            for i in range(3):
                phi_j.T[i] = np.array(
                    self.unstructured_grid.point_data[
                        param[i*self.n_gen_dis + j]
                    ],
                    dtype=np.float64
                )
                pass
            phi_list.append(phi_j)
            pass
        # * the generalized displacement response
        self.phi_3Darray: np.ndarray = np.array(phi_list, dtype=np.float64)
        self.unstructured_grid.clear_point_data() # ! clear the point data to save memory
        self.unstructured_grid.clear_cell_data() # ! clear the cell data to save memory
        for i in range(len(self.scalars_list)):
            self.unstructured_grid.point_data[self.scalars_list[i]] = np.zeros(self.n_points, dtype=np.float64)
            pass
        self.unstructured_grid.set_active_scalars(self.active_scalar)
        pass
    
    def __initializeDefaultValueOfGenDis(self) -> None:
        """initialize the default value of gen_dis_response file
        """
        self.gen_dis_file_path: str = "not given"
        # * the generalized displacement response file
        self.gen_dis_file: str = "not given"
        # * the time array
        self.t: np.ndarray = np.array([0])
        # * the number of steps
        self.n_steps: int = 1
        # * the total time
        self.total_time: float = self.t[-1]
        # * the gneralized displacement responses' array
        self.gen_dis_response: np.ndarray = np.zeros([self.n_gen_dis, 1])
        pass
    
    #------------------------------------------------------------------------------------
    
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
        for i in range(len(self.scalars_list)):
            self.scalars_clim_dict[self.scalars_list[i]] = np.array([dis_min[i], dis_max[i]])
            pass
        self.current_step = 0
        pass
    
    def __getDisplacementAtCurrentStep(self) -> np.ndarray:
        """get the displacement at current step

        Returns:
            np.ndarray: current step's displacement
        """
        displacement: np.ndarray = (self.phi_3Darray.T @ self.gen_dis_response[0: self.n_gen_dis, self.current_step]).T
        return displacement
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
    
    def getCurrentTime(self) -> float:
        """get the current time

        Returns:
            float: current time
        """
        return self.t[self.current_step]
        pass
    
    #------------------------------------------------------------------------------------
    
    def setStepByIndex(self, step: int) -> np.ndarray:
        """set the step by index

        Args:
            step (int): given step

        Returns:
            np.ndarray: the displacement range
        """
        self.current_step = step
        displacement: np.ndarray = self.__getDisplacementAtCurrentStep()
        self.unstructured_grid.points = self.basic_position + displacement * self.displacement_magnification
        for i in range(len(self.scalars_list)):
            self.unstructured_grid.point_data[self.scalars_list[i]] = displacement.T[i]
            pass
        return displacement
        pass
    
    def setStepByTime(self, t: float) -> np.ndarray:
        """set the step by time

        Args:
            t (float): given time

        Returns:
            np.ndarray: the displacement range
        """
        return self.setStepByIndex(self.__timeToStep(t))
        pass
    
    def setStepByLimitTime(self, t_limit: float) -> None:
        """update the current step by the limit time

        Args:
            t (float): the limit time
        """
        displacement: np.ndarray = self.setStepByTime(t_limit)
        for i in range(len(self.scalars_list)):
            self.unstructured_grid.point_data[self.scalars_list[i]] = displacement.T[i]
            pass
        pass
    
    #------------------------------------------------------------------------------------
    
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
    
    def setScalarClim(self, scalar_name: str, clim: np.ndarray) -> None:
        """set the scalar clim

        Args:
            scalar_name (str): the name of scalar
            clim (np.ndarray): the clim
        """
        self.scalars_clim_dict[scalar_name] = clim
        pass
    
    #------------------------------------------------------------------------------------
    
    def connectToGenDisFilePath(self, gen_dis_file_path: str) -> None:
        self.gen_dis_file_path = gen_dis_file_path
        self.gen_dis_file = os.path.join(gen_dis_file_path, observeFileName(self.flag))
        pass
    
    def updateGenDisFile(self) -> float:
        """update the gen_dis_file

        Returns:
            float: return the current total time
        """
        data: np.array = np.loadtxt(self.gen_dis_file, dtype=np.float64, ndmin=2).T # ! ndmin=2 is a must!
        self.t = data[0]
        self.gen_dis_response = data[1:]
        self.total_time = self.t[-1]
        self.n_steps = len(self.t)
        return self.total_time
        pass
    
    #------------------------------------------------------------------------------------
    
    pass

print("Successfully import MeshClass.py")

################################################################################################################################################################