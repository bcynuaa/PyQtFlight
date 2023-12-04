'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-05 17:18:03
 # @ license: Mozilla Public License 2.0
 # @ description: the class of domains with general displacement
 # ! gen_dis means general displacement
 '''
 
import os
import numpy as np

from config.Name import kScalarsList, kDefault_Scalar, kSplit_Line

from config.PyvistaSettings import *

from utils.RegularExpression import getDomainFilesList

class DomainsWithGenDis:
    
    """this class of domains with general displacement
    - `data_path: str` -> the path of the data
    - `domain_files_list: list` -> the list of the domain files
    - `n_domains: int` -> the number of the domains
    - `unstructured_grid: pyvista.UnstructuredGrid` -> the unstructured grid of the domains
    - `n_points: int` -> the number of the points
    - `n_cells: int` -> the number of the cells
    - `basic_position: np.ndarray` -> the basic position of the points
    - `n_gen_dis: int` -> the number of the general displacement
    - `phi_3Darray: np.ndarray` -> the 3D array of the general displacement
    """
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> None:
        info: str = kSplit_Line + "\n<DomainsWithGenDis>\n"
        info += "data path: " + self.data_path + "\n"
        info += "number of domains: " + str(self.n_domains) + "\n"
        info += "number of points: " + str(self.n_points) + "\n"
        info += "number of cells: " + str(self.n_cells) + "\n"
        info += "number of general displacement: " + str(self.n_gen_dis) + "\n"
        info += kSplit_Line + "\n"
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    def getInfo(self) -> str:
        return self.__str__()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDomainFilesFromPath(self, data_path: str) -> None:
        self.data_path: str = data_path
        self.__findDomainFiles()
        self.__processDomainFiles()
        pass
    
    def __findDomainFiles(self) -> None:
        # find the domain files from the data path
        self.domain_files_list: list = getDomainFilesList(os.listdir(self.data_path))
        # join domain files path with data path
        self.domain_files_list = [os.path.join(self.data_path, domain_file) \
            for domain_file in self.domain_files_list]
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
        param: list = list( self.unstructured_grid.point_data.keys() )
        param.sort()
        self.n_gen_dis: int = len(param) // 3
        phi_list: list = []
        for j in range(self.n_gen_dis):
            phi_j: np.ndarray = np.zeros([self.n_points, 3], dtype=np.float64)
            for i in range(3):
                phi_j.T[i] = np.array( \
                    self.unstructured_grid.point_data[param[i*self.n_gen_dis + j]], dtype=np.float64)
                pass
            phi_list.append(phi_j)
            pass
        self.phi_3Darray: np.ndarray = np.array(phi_list, dtype=np.float64)
        self.unstructured_grid.point_data.clear()
        self.unstructured_grid.cell_data.clear()
        for scalar in kScalarsList:
            self.unstructured_grid.point_data[scalar] = np.zeros(self.n_points, dtype=np.float64)
            pass
        # self.unstructured_grid.active_scalars_name should be set as kDefault_Scalar
        self.unstructured_grid.set_active_scalars(kDefault_Scalar)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getGenDis(self, gen_dis_response: np.ndarray) -> np.ndarray:
        return (self.phi_3Darray.T @ gen_dis_response).T
        pass
    
    def getUnstructuredGrid(self, \
        gen_dis_response: np.ndarray, magnification: float = 0.01) -> pyvista.UnstructuredGrid:
        gen_dis: np.ndarray = self.getGenDis(gen_dis_response)
        unstructured_grid: pyvista.UnstructuredGrid = self.unstructured_grid.copy()
        unstructured_grid.points += gen_dis * magnification
        for i in range(len(kScalarsList)):
            unstructured_grid.point_data[kScalarsList[i]] = gen_dis.T[i]
            pass
        return unstructured_grid
        pass
    
    def addGenDisToUnstructuredGrid(self, unstructured_grid: pyvista.UnstructuredGrid, \
        gen_dis_response: np.ndarray, magnification: float = 0.01) -> None:
        gen_dis: np.ndarray = self.getGenDis(gen_dis_response)
        unstructured_grid.points = self.basic_position + gen_dis * magnification
        for i in range(len(kScalarsList)):
            unstructured_grid.point_data[kScalarsList[i]] = gen_dis.T[i]
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: DomainsWithGenDisClass.py is imported.")