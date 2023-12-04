'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-16 23:21:18
 # @ description: backend for DomainsWithModes
 '''

import os
import numpy as np

from src.config.libs.PyvistaConfig import pyvista
from src.config.backend.DomainsWithModesConfig import *

class DomainsWithModes:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.domains_loaded: bool = False
        pass
    
    def __str__(self) -> str:
        info: str = "domains loaded: %s\n" % str(self.domains_loaded)
        if self.domains_loaded == False:
            pass
        else:
            info += "data path: %s\n" % self.data_path
            info += "number of domains: %d\n" % self.n_domains
            info += "number of points: %d\n" % self.n_points
            info += "number of cells: %d\n" % self.n_cells
            info += "number of modes: %d\n" % self.n_modes
            info += "active scalar: %s\n" % self.active_scalar
            info += "active scalar index: %d\n" % self.active_scalar_index
            info += "all active scalars: %s" % str(scalars_list)
            pass
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDomainFilesFromPath(self, data_path: str) -> None:
        self.data_path: str = data_path
        self.__findDomainFiles()
        self.__processDomainFiles()
        self.__processModes()
        self.domains_loaded = True
        pass
    
    def __findDomainFiles(self) -> None:
        self.domain_files_list: list[str] = list()
        files_list: list[str] = os.listdir(self.data_path)
        for file in files_list:
            is_match: bool = domains_regular_expression_pattern.match(file)
            if is_match == None:
                continue
                pass
            else:
                self.domain_files_list.append(os.path.join(self.data_path, file))
                pass
            pass
        self.domain_files_list.sort()
        self.n_domains: int = len(self.domain_files_list)
        pass
    
    def __processDomainFiles(self) -> None:
        multi_blocks: pyvista.core.composite.MultiBlock = pyvista.MultiBlock()
        for domain_file in self.domain_files_list:
            multi_blocks.append( pyvista.get_reader(domain_file).read() )
            pass
        self.unstructured_grid: pyvista.UnstructuredGrid = multi_blocks.combine()
        self.n_points: int = self.unstructured_grid.n_points
        self.n_cells: int = self.unstructured_grid.n_cells
        self.basic_position: np.ndarray = np.array(self.unstructured_grid.points, dtype=np.float64)
        pass
    
    def __processModes(self) -> None:
        param: list[str] = list( self.unstructured_grid.point_data.keys() )
        param.sort()
        self.n_modes: int = len(param) // dim
        mode_list: list[np.ndarray] = list()
        for i_mode in range(self.n_modes):
            mode: np.ndarray = np.zeros((self.n_points, dim), dtype=np.float64)
            for i_dim in range(dim):
                mode[:, i_dim] = np.array(
                    self.unstructured_grid.point_data[param[i_dim * self.n_modes + i_mode]], \
                        dtype=np.float64)
                pass
            mode_list.append(mode)
            pass
        self.mode_tensor: np.ndarray = np.array(mode_list, dtype=np.float64)
        self.unstructured_grid.point_data.clear()
        self.unstructured_grid.cell_data.clear()
        for scalar in scalars_list:
            self.unstructured_grid.point_data[scalar] = np.zeros(self.n_points, dtype=np.float64)
            pass
        self.setActiveScalar(scalars_default)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setActiveScalar(self, active_scalar: str) -> None:
        self.active_scalar: str = active_scalar
        self.active_scalar_index: int = scalars_list.index(self.active_scalar)
        self.unstructured_grid.set_active_scalars(self.active_scalar)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getModeShape(self, mode_response: np.ndarray) -> np.ndarray:
        return (self.mode_tensor.T @ mode_response).T
        pass
    
    def addModeShapeToGrid(self, unstructured_grid: pyvista.UnstructuredGrid,
        mode_shape: np.ndarray, magnification: float) -> None:
        unstructured_grid.points = self.basic_position + magnification * mode_shape
        unstructured_grid.point_data[self.active_scalar] = \
            mode_shape[:, self.active_scalar_index]
        pass
    
    def addModeResponseToGrid(self, unstructured_grid: pyvista.UnstructuredGrid,
        mode_response: np.ndarray, magnification: float) -> None:
        mode_shape: np.ndarray = self.getModeShape(mode_response)
        self.addModeShapeToGrid(unstructured_grid, mode_shape, magnification)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("backend: DomainsWithModes.py is imported.")