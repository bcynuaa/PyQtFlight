'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: config for backend.Grids
 '''

import numpy as np
import pandas as pd

from src.backend.Grids import Grids

data_path: str = "data//domains_data"
map_matrix_filename: str = "data//grids_data//SensorsMap.dat"
standard_mode_response_filename: str = "data//grids_data//StandardModeResponse.dat"

grids: Grids = Grids()

grids.loadDomainsFromPath(data_path)
grids.loadMapMatrix(map_matrix_filename)
grids.loadStandardModeResponse(standard_mode_response_filename)

grids.allLoaded()

print("standard mode response: %s" % str(grids.standard_mode_response))
print("standard mode shape's array shape: %s" % str(grids.standard_mode_shape.shape))
print("standard compared sensor response: %.10f" % grids.standard_compared_sensor_response)
print("compared sensor index: %d" % grids.compared_sensor_index)
print("standard sensor response: %s" % str(grids.standard_sensor_response))

# random sensor response
print("----------------------------------random test----------------------------------")
print("random data:\n")
data: np.ndarray = np.random.randn(10000, grids.sensors.n_sensors)
sensor_response: pd.DataFrame = pd.DataFrame(data)
print(sensor_response.info())

print("first 1 row:\n%s" % str(sensor_response.iloc[0, :]))
print("simulation sensor response:\n%s" % str(grids.getSimulationSensorResponse(sensor_response.iloc[0, :].values)))
print("first 5 rows:\n%s" % str(sensor_response.iloc[0:5, :]))
print("simulation sensor responses:\n%s" % str(grids.getSimulationSensorResponses(sensor_response.iloc[0:5, :].values)))

print("update via first row")
grids.updateGrids(sensor_response.iloc[0, :].values)
grids.simulation_grid.plot()

# expected output:

# config: PyvistaConfig.py is imported.
# config: GridsConfig.py imported
# decorator: Clock.py is imported.
# config: DomainsWithModesConfig.py is imported
# backend: DomainsWithModes is imported.
# config: SensorsConfig.py is imported
# backend: Sensors.py is imported
# backend: Grids.py is imported
# standard mode response: [211.08884694  -1.72437235  -1.70903847]
# standard mode shape's array shape: (9750, 3)
# standard compared sensor response: 0.9921515479
# compared sensor index: 0
# standard sensor response: [0.99215155 0.49988537 0.31801484 1.1983033 ]
# ----------------------------------random test----------------------------------
# random data:

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10000 entries, 0 to 9999
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   0       10000 non-null  float64
#  1   1       10000 non-null  float64
#  2   2       10000 non-null  float64
#  3   3       10000 non-null  float64
# dtypes: float64(4)
# memory usage: 312.6 KB
# None
# first 1 row:
# 0   -0.434095
# 1   -0.998505
# 2    0.338675
# 3   -0.773778
# Name: 0, dtype: float64
# simulation sensor response:
# [-0.43409459 -0.2187141  -0.13914056 -0.52429186]
# first 5 rows:
#           0         1         2         3
# 0 -0.434095 -0.998505  0.338675 -0.773778
# 1 -0.907783  0.022394  0.341110  0.048359
# 2 -0.833635  0.697720 -0.222959 -0.742242
# 3 -1.189550 -2.689282  0.252953  0.513880
# 4  0.785787 -0.078057  0.917670  0.553404
# simulation sensor responses:
# [[-0.43409459 -0.2187141  -0.13914056 -0.52429186]
#  [-0.90778298 -0.45737713 -0.29097214 -1.09640442]
#  [-0.83363502 -0.42001845 -0.26720545 -1.00684981]
#  [-1.18954983 -0.59934247 -0.38128701 -1.43671749]
#  [ 0.78578666  0.39591054  0.25186859  0.9490594 ]]
# update via first row
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0020017623901367188 seconds.
# ----------------------------------------------------------------------