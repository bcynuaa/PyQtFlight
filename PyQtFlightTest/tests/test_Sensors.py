'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 20:08:47
 # @ license: Mozilla Public License 2.0
 # @ description: the file is used to test Sensors
 '''
 
import numpy as np
 
from src.SensorsClass import Sensors

sensors_file: str = "..//..//TestData//ProjectFlightTest2//Sensors//sensor_vbshape.dat"
sensors: Sensors = Sensors()
sensors.loadSensorsModeDisFile(sensors_file)
print(sensors)

print("mode j at sensor i's displacement's matrix [i, j]\n", sensors.mode_dis_matrix)
sensor_response_data: np.ndarray = np.zeros(sensors.n_sensors) + 1
print("sensor response data: ", sensor_response_data)
print("general displacement response: ", sensors.getGenDisResponse(sensor_response_data))

# results:

# config: Name.py is imported.
# src: SensorsToModeClass.py is imported.
# --------------------------------------------------
# Sensors
# sensors mode displacement files: ..//..//TestData//ProjectFlightTest2//Sensors//sensor_vbshape.dat
# number of sensors: 4
# number of general displacement: 5
# --------------------------------------------------

# mode j at sensor i's displacement's matrix [i, j]
#  [[ 5.24621044e-03  4.19315876e-04  4.32177499e-03  3.70759700e-03
#   -1.32514131e-03]
#  [ 2.41022253e-03  2.69759595e-03 -2.16915652e-03 -3.32380445e-03
#   -1.15648163e-04]
#  [ 1.60559939e-03  1.00080312e-03 -1.54050054e-03  3.21911335e-04
#   -2.22998471e-03]
#  [ 6.65424136e-03 -1.85990488e-02  2.09414053e-05 -1.63393921e-02
#    2.47003517e-03]]
# sensor response data:  [1. 1. 1. 1.]
# general displacement response:  [ 241.59024901   31.13881526 -100.77192797  -27.85413233 -194.91899223]