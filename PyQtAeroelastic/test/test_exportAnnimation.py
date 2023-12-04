# coding = "utf-8"
# author = "bcynuaa"
# date = "2023/05/05"

###################################################################################################
# This file is used to test the class MultiBlocksByGenDis's annimation function in src.ReadFile.py

from test_Header import *
import src.ReadFile as ReadFile

print("test for src.ReadFile.py's annimation function")
print("test for ReadFile.MultiBlocksByGenDis's annimation function")
print("include gif and mp4 file in for the test data of test_data1 directory")

test_data: str = "data//test_data//test_data1"
mb: ReadFile.MultiBlocksByGenDis = ReadFile.MultiBlocksByGenDis(test_data)

print(mb)

test_scalar: str = "dZ"
magnification: float = 3000.0
mb.setActivatedScalar(test_scalar)
mb.setDisplacementMagnification(magnification)
print(mb)

annimation_path: str = "image//test_image//test_annimation"
gif_file_name: str = "test_annimation.gif"
mp4_file_name: str = "test_annimation.mp4"
fps: int = 60
skip_step: int = 1
loop: int = 0
quality: int = 7

print("start to generate gif file...")
mb.exportGIF(
    os.path.join(annimation_path, gif_file_name),
    skip_step=skip_step,
    fps=fps,
    loop=loop
)

print("start to generate mp4 file...")
mb.exportMP4(
    os.path.join(annimation_path, mp4_file_name),
    skip_step=skip_step,
    framerate=fps,
    quality=7
)

###################################################################################################
# expected results

# workspace directory included
# successfully set the global theme of pyvista.

# test for src.ReadFile.py's annimation function
# test for ReadFile.MultiBlocksByGenDis's annimation function
# include gif and mp4 file in for the test data of test_data1 directory
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
# unstractured grid information: UnstructuredGrid (0x1327a8c28c0)
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
# current step: 0
# current active scalar: dZ
# displacement magnification: 3000.0
# scalar span: {'dX': [0.0, 0.0], 'dY': [0.0, 0.0], 'dZ': [-2.1550726822577413e-05, 1.938558057881892e-05], 'Pressure': [0.92219002, 1.10911417]}
# unstractured grid information: UnstructuredGrid (0x1327a8c28c0)
#   N Cells:    5000
#   N Points:   5716
#   X Bounds:   1.496e+01, 1.830e+01
#   Y Bounds:   1.900e+00, 4.198e+00
#   Z Bounds:   -1.956e-01, -4.198e-02
#   N Cells:    5000
#   N Points:   5716
#   X Bounds:   1.496e+01, 1.830e+01
#   Y Bounds:   1.900e+00, 4.198e+00
#   Z Bounds:   -1.956e-01, -4.198e-02
#   N Arrays:   4


# start to generate gif file...
# 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 360/360 [01:12<00:00,  4.97it/s] 
# successfully export the gif file as image//test_image//test_annimation\test_annimation.gif
# start to generate mp4 file...
# 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 360/360 [01:01<00:00,  5.88it/s] 
# successfully export the mp4 file as image//test_image//test_annimation\test_annimation.mp4