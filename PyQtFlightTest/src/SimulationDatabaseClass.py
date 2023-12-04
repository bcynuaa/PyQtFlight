'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 19:40:40
 # @ license: Mozilla Public License 2.0
 # @ description: the class of simulation database
 '''

import os
import numpy as np

from config.Name import kData_File_Format, kDefault_Simulation_Name, kSplit_Line

from utils.RegularExpression import getHAndMaFromDatabaseFile
from utils.SubDict import *

kSkip_Rows: int = 1

class SimulationDatabase:
    
    """the class of simulation database
    - `database_path: str` -> the path of the database
    - `database_files_list: list` -> the list of the database files
    - `database_files_dict: dict` -> the dict of the database files
    - `database_dict: dict` -> the dict of the database, which is a sub-dict like `database_dict[height][mach] = data`
    """
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        info: str = kSplit_Line + "\n<SimulationDatabase>\n"
        info += "database path: " + self.database_path + "\n"
        info += "number of database files: " + str(len(self.database_files_list)) + "\n"
        info += "database files:\n" + str(self.database_files_list) + "\n"
        info += "current database has value at (height, mach):\n" \
            + str(self.getDatabaseDictKeys()) + "\n"
        info += kSplit_Line + "\n"
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    def getInfo(self) -> str:
        info: str = kSplit_Line + "\n<SimulationDatabase>\n"
        info += "database path: " + self.database_path + "\n"
        info += "number of database files: " + str(len(self.database_files_list)) + "\n"
        info += "current database has value at (height, mach):\n" \
            + str(self.getDatabaseDictKeys()) + "\n"
        info += kSplit_Line + "\n"
        return info
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDatabaseFromPath(self, database_path: str) -> None:
        self.database_path: str = database_path
        self.__findDatabaseFilesFromPath()
        self.__buildDatabase()
        pass
    
    def __findDatabaseFilesFromPath(self) -> None:
        database_files_list: list = os.listdir(self.database_path)
        self.database_files_list: list = []
        for database_file in database_files_list:
            # check the file format
            if database_file.startswith(kDefault_Simulation_Name) and \
                database_file.endswith(kData_File_Format):
                self.database_files_list.append(database_file)
                pass
            pass
        # join the path
        self.database_files_list = [os.path.join(self.database_path, database_file) \
            for database_file in self.database_files_list]
        # sort the file list
        self.database_files_list.sort()
        pass
    
    def __buildDatabase(self) -> None:
        # build the database as a dict
        # while the dict should look like: self.database_dict[height][mach] = data
        # what's more, the data should be a numpy array
        # at the same time, a database_files_dict should be built
        self.database_files_dict = dict()
        self.database_dict: dict = dict()
        self.updateDatabaseFromMultipleFiles(self.database_files_list)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def updateDatabaseFromSingularFile(self, database_file: str) -> None:
        # get the height and mach from the database_file
        height, mach = getHAndMaFromDatabaseFile(database_file)
        # insert the database file to the database_files_dict
        insertToSubDict(self.database_files_dict, height, mach, database_file)
        # insert the data to the database_dict
        insertToSubDict(self.database_dict, height, mach, \
            np.loadtxt(database_file, dtype=np.float64, skiprows=kSkip_Rows))
        if database_file not in self.database_files_list:
            self.database_files_list.append(database_file)
            pass
        pass
    
    def updateDatabaseFromMultipleFiles(self, database_files_list: list) -> None:
        for database_file in database_files_list:
            self.updateDatabaseFromSingularFile(database_file)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getDatabaseDictKeys(self) -> list:
        # this function is to get the database_dict's keys like: [(height1, mach1), ...]
        return getSubDictKeys(self.database_dict)
        pass
    
    def getCloestDatabaseDictKeys(self, height_in: np.float64, mach_in: np.float64) -> tuple:
        # for height_in and mach_in may not actually in the database_dict's keys
        # thus we need to find the cloest keys of height(H) and mach(Ma)
        return getCloestSubDictKeys(self.database_dict, height_in, mach_in)
        pass
    
    def getDatabaseDictData(self, height_in: np.float64, mach_in: np.float64) -> tuple:
        # this function is to get the data from database_dict
        # the return value should look like: (database, height, mach)
        height, mach = self.getCloestDatabaseDictKeys(height_in, mach_in)
        return (self.database_dict[height][mach], height, mach)
        pass
    
    def getDatabaseFileDictData(self, height_in: np.float64, mach_in: np.float64) -> tuple:
        # this function is to get the data from database_files_dict
        # the return value should look like: (database_file, height, mach)
        height, mach = self.getCloestDatabaseDictKeys(height_in, mach_in)
        return (self.database_files_dict[height][mach], height, mach)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: SimulationDatabaseClass.py is imported.")