# coding="utf-8"
# author: bcynuaa
# dart: 2023/04/27

###################################################################################################
# This file is used to test the class MultiBlocksByGenDis in src.ReadFile.py

from test_Header import *
import src.ReadFile as ReadFile

print("test for src.ReadFile.py")
print("test for ReadFile.MultiBlocksByGenDis")

test_data: str = "data//test_data//test_data1"
mb: ReadFile.MultiBlocksByGenDis = ReadFile.MultiBlocksByGenDis(test_data)

print(mb)

test_time: float = 0.15
test_scalar: str = "dZ"
magnification: float = 50.0
mb.setStepByTime(test_time)
mb.setActivatedScalar(test_scalar)
mb.setDisplacementMagnification(magnification)
print(mb)

mb.unstructured_grid.plot()

###################################################################################################
# expected results

# workspace directory included
# successfully set the global theme of pyvista.

# test for src.ReadFile.py
# test for ReadFile.MultiBlocksByGenDis
# Multibloks type defined by generalized displacement data struct for Prof. Guo
# data path: data//test_data//test_data1
# generalized displacement file: data//test_data//test_data1\m03n0089.dat
# pressure file: data//test_data//test_data1\Pressure.dat
# number of blocks: 18
# number of steps: 360
# total simulation time: 0.21113
# current step: 0
# current active scalar: Pressure
# displacement magnification: 50.0
# scalar span: {'dX': [0.0, 0.0], 'dY': [0.0, 0.0], 'dZ': [-2.1550726822577413e-05, 1.938558057881892e-05], 'Pressure': [0.92219002, 1.10911417]}
# unstractured grid information: UnstructuredGrid (0x23a3c39f820)
#   N Cells:    5000
#   N Points:   5716
#   X Bounds:   1.496e+01, 1.830e+01
#   Y Bounds:   1.900e+00, 4.198e+00
#   Z Bounds:   -1.956e-01, -4.198e-02
#   N Arrays:   4


# Multibloks type defined by generalized displacement data struct for Prof. Guo
# data path: data//test_data//test_data1
# generalized displacement file: data//test_data//test_data1\m03n0089.dat
# pressure file: data//test_data//test_data1\Pressure.dat
# number of blocks: 18
# number of steps: 360
# total simulation time: 0.21113
# current step: 255
# current active scalar: dZ
# displacement magnification: 50.0
# scalar span: {'dX': [0.0, 0.0], 'dY': [0.0, 0.0], 'dZ': [-2.1550726822577413e-05, 1.938558057881892e-05], 'Pressure': [0.92219002, 1.10911417]}
# unstractured grid information: UnstructuredGrid (0x23a3c39f820)
#   N Cells:    5000
#   N Points:   5716
#   X Bounds:   1.496e+01, 1.830e+01
#   Y Bounds:   1.900e+00, 4.198e+00
#   Z Bounds:   -1.956e-01, -4.196e-02
#   N Arrays:   4