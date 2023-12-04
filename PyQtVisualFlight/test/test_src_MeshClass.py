# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to test the utils.PatternMatch

from test_Header import *
from src.MeshClass import *

data_path: str = "..//..//TestData//ProjectFlightTest//Domain"
mesh: MeshByGenDis = MeshByGenDis(data_path)

print(mesh)
mesh.unstructured_grid.plot()

###################################################################################################
# results should be:

# workspace directory included
# Successfully set the global theme of pyvista.

# Basic things have been loaded loaded.
# Pattern match has been loaded.
# ====================================================================================================

# Mesh data class defined by generalized displacement data structure for Prof. Guo
# Mesh flag: simulation
# data path: ..//..//TestData//ProjectFlightTest//Domain
# generalized displacement file: not given
# number of blocks: 48
# number of steps: 1
# total simulation time: 0
# current step: 0
# current active scalar: dZ
# displacement magnification: 5000.0
# scalar span: {'dX': array([0., 0.]), 'dY': array([0., 0.]), 'dZ': array([0., 0.])}
# unstructured grid information: UnstructuredGrid (0x1a6cc923160)
#   N Cells:    9996
#   N Points:   11462
#   X Bounds:   1.300e+01, 1.776e+01
#   Y Bounds:   8.200e-01, 3.620e+00
#   Z Bounds:   -1.629e+00, -1.336e+00
#   N Arrays:   0

# ====================================================================================================