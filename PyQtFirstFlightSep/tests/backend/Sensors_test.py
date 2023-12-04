'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: test for backend.Sensors
 '''

from src.backend.Sensors import Sensors

map_matrix_filename: str = "data//grids_data//SensorsMap.dat"

sensors: Sensors = Sensors()
sensors.loadMapMatrix(map_matrix_filename)

print(sensors)

print(sensors.modeToSensor([1, 1, 1]))
print(sensors.sensorToMode([1, 1, 1, 1]))

# expected output:

# config: SensorsConfig.py is imported
# backend: Sensors.py is imported
# map matrix loaded: True
# map matrix file name: data//grids_data//SensorsMap.dat
# number of sensors: 4
# number of modes: 3
# [0.00797522 0.00286059 0.00079421 0.01354991]
# [ 369.7046139   -78.71310335 -141.64057929]