'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-29 00:48:54
 # @ description: test for backend.BackendManager
 '''

import time

from src.backend.BackendManager import BackendManager

backend_manager = BackendManager()

data_path: str = "data//domains_data//"
map_matrix_filename: str = "data//grids_data//SensorsMap.dat"
standard_mode_response_filename: str = "data//grids_data//StandardModeResponse.dat"

latest_data_filename: str = "data//update_data//LatestData.dat"

backend_manager.loadDomainsFromPath(data_path)
backend_manager.loadMapMatrix(map_matrix_filename)
backend_manager.loadStandardModeResponse(standard_mode_response_filename)
backend_manager.buildBackend()

start_time: float = time.time()
update_number: int = 1000
for i in range(update_number):
    backend_manager.readLatestData(latest_data_filename)
    pass
end_time: float = time.time()
print("time cost for %d loops in backend_manager: %f" % (update_number, end_time - start_time))

start_time: float = time.time()
backend_manager.readLatestData(latest_data_filename)
print("latest flight test sensors data array shape: ", backend_manager.getLatestFlightTestSensorDataForCurves().shape)
print("latest simulation sensors data array shape: ", backend_manager.getLatestSimulationSensorDataForCurves().shape)
print("latest time data min to max: ", backend_manager.getLatestTimeDataForCurves().min(), " to ", backend_manager.getLatestTimeDataForCurves().max())
print("latest sensor data for bars: ", backend_manager.getLatestSensorDataForBars())
print("latest parameters markdown table:\n", backend_manager.getLatestParametersMarkdownTable())
end_time: float = time.time()
print("time cost for one loop in backend_manager: %f" % (end_time - start_time))

print("main_dataframe info:")
print(backend_manager.data_stream.main_dataframe.info())
print("in real working situation, the main_dataframe will consume %.2f times lager than this." % (3600*5/update_number))

# expected output:

# config.backend: BackendManagerConfig.py is imported
# config.libs: PyvistaConfig.py is imported.
# config.backend: GridsConfig.py imported
# decorator: Clock.py is imported.
# config.backend: DomainsWithModesConfig.py is imported
# backend: DomainsWithModes is imported.
# config.backend: SensorsConfig.py is imported
# backend: Sensors.py is imported
# backend: Grids.py is imported
# config.backend: DataStreamConfig.py is imported
# backend: DataStream is imported
# backend: BackendManager.py is imported
# BackendManager.buildBackend() succeeded
# number of sensors: 4
# number of modes: 3
# time cost for 1000 loops in backend_manager: 8.127382
# latest flight test sensors data array shape:  (10000, 3)
# latest simulation sensors data array shape:  (10000, 3)
# latest time data min to max:  61108.059  to  61108.12
# latest sensor data for bars:  [0.32250769 0.21402237 1.24547909]
# latest parameters markdown table:
#  | parameter 1       |    value 1 |
# |:------------------|-----------:|
# | pressure altitude | 373.747    |
# | CAS               | 990        |
# | mach              |   0.779372 |
# | alpha             |  -1        |
# | phi               |  -4        |
# | beta              |   3        |
# | left flaperon     |   7        |
# | right flaperon    |   0        |
# | left horiz tail   |   3        |
# | right horiz tail  |   7        |
# | left rudder       |   1        |
# | right rudder      |  -6        |
# time cost for one loop in backend_manager: 0.035860
# main_dataframe info:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 32032 entries, 0 to 32031
# Data columns (total 45 columns):
#  #   Column             Non-Null Count  Dtype
# ---  ------             --------------  -----
#  0   hour               32032 non-null  int64
#  1   min                32032 non-null  int64
#  2   sec                32032 non-null  int64
#  3   mssec              32032 non-null  int64
#  4   pressure altitude  32032 non-null  float64
#  5   CAS                32032 non-null  int64
#  6   mach               32032 non-null  float64
#  7   alpha              32032 non-null  int64
#  8   phi                32032 non-null  int64
#  9   beta               32032 non-null  int64
#  10  left flaperon      32032 non-null  int64
#  11  right flaperon     32032 non-null  int64
#  12  left horiz tail    32032 non-null  int64
#  13  right horiz tail   32032 non-null  int64
#  14  left rudder        32032 non-null  int64
#  15  right rudder       32032 non-null  int64
#  16  16                 32032 non-null  float64
#  17  17                 32032 non-null  float64
#  18  18                 32032 non-null  float64
#  19  19                 32032 non-null  float64
#  20  20                 32032 non-null  float64
#  21  21                 32032 non-null  float64
#  22  22                 32032 non-null  float64
#  23  23                 32032 non-null  float64
#  24  24                 32032 non-null  float64
#  25  25                 32032 non-null  float64
#  26  26                 32032 non-null  float64
#  27  27                 32032 non-null  float64
#  28  28                 32032 non-null  float64
#  29  29                 32032 non-null  float64
#  30  30                 32032 non-null  float64
#  31  31                 32032 non-null  float64
#  32  32                 32032 non-null  float64
#  33  33                 32032 non-null  float64
#  34  sensor1            32032 non-null  float64
#  35  sensor2            32032 non-null  float64
#  36  sensor3            32032 non-null  float64
#  37  sensor4            32032 non-null  float64
#  38  38                 32032 non-null  float64
#  39  39                 32032 non-null  float64
#  40  40                 32032 non-null  float64
#  41  41                 32032 non-null  float64
#  42  42                 32032 non-null  float64
#  43  43                 32032 non-null  float64
#  44  time               32032 non-null  float64
# dtypes: float64(31), int64(14)
# memory usage: 11.0 MB
# None
# in real working situation, the main_dataframe will consume 18.00 times lager than this.