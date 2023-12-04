'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-24 01:06:19
 # @ description: test for backend.DataStream
 '''

from src.backend.DataStream import DataStream

data_stream: DataStream = DataStream()

latest_data_filename: str = "data//update_data//LatestData.dat"

print("set sensor number to 4")
data_stream.setSensorNumber(4)
print(data_stream.sensors_index_list)

print("read from file: LatestData.dat for twice")

data_stream.readLatestData(latest_data_filename)
data_stream.readLatestData(latest_data_filename)

print("latest parameters markdown table:")
print(data_stream.getLatestParametersMarkdownTable())

print("head 5 lines of main dataframe:")
print(data_stream.main_dataframe.head(5))

print("tail 5 lines of main dataframe:")
print(data_stream.main_dataframe.tail(5))

print("shape of data for curves")
print(data_stream.getLatestSensorDataForCurves().shape)

print("time span of data for curves")
print(data_stream.getLatestTimeDataForCurves().min(), " to ", data_stream.getLatestTimeDataForCurves().max())

print("shape of data for bars")
print(data_stream.getLatestSensorDataForBars().shape)

print("save main dataframe to csv file at data//update_data//LatestData.csv")
data_stream.main_dataframe.to_csv("data//update_data//LatestData.csv")

# expected output:

# config.backend: DataStreamConfig.py is imported
# backend: DataStream is imported
# set sensor number to 4
# [34, 35, 36, 37]
# read from file: LatestData.dat for twice
# latest parameters markdown table:
# | parameter 1       |    value 1 |
# |:------------------|-----------:|
# | pressure altitude | 290.402    |
# | CAS               | 917        |
# | mach              |   0.895698 |
# | alpha             |   8        |
# | phi               |   5        |
# | beta              |   5        |
# | left flaperon     |  -7        |
# | right flaperon    |  -7        |
# | left horiz tail   |   6        |
# | right horiz tail  |  -3        |
# | left rudder       |   2        |
# | right rudder      |   7        |
# head 5 lines of main dataframe:
#    hour  min  sec  mssec  pressure altitude   CAS      mach  alpha  phi  beta  left flaperon  ...  sensor1  sensor2  sensor3  sensor4       38       39       40       41       42       43       time
# 0    16   58   27    934            250.033   998  0.856526     -6    1     3              9  ... -0.82836 -0.27356 -0.21620 -1.66030 -0.09181  0.31525 -0.15152  0.26936 -0.53199 -0.57383  61107.934        
# 1    16   58   27    936            251.335  1066  0.859683      1    1    -4              6  ... -1.27103 -0.30863 -0.14686 -1.17297 -0.21216  0.23729  0.38047  0.20202 -0.20202  1.54882  61107.936        
# 2    16   58   27    938            252.637   967  0.802801     -4   -3     4              4  ... -1.51838 -0.25953 -0.13870 -1.23330 -0.21216  0.18644  0.18182  0.55556 -0.07407  1.25926  61107.938        
# 3    16   58   27    940            253.939   977  0.801826      6    3    -2              9  ... -1.38862 -0.25151 -0.17133 -0.97859 -0.07940  0.14576 -0.15825  0.71717 -0.37037  0.24497  61107.940        
# 4    16   58   27    942            255.242  1006  0.735881      6   -8    -8             -4  ... -1.26089 -0.22346 -0.18357 -0.34854  0.14268  0.05085  0.42424  0.32323 -0.22896  0.84899  61107.942        

# [5 rows x 45 columns]
# tail 5 lines of main dataframe:
#     hour  min  sec  mssec  pressure altitude   CAS      mach  alpha  phi  beta  left flaperon  ...  sensor1  sensor2  sensor3  sensor4       38       39       40       41       42       43       time
# 59    16   58   27    987            285.193  1035  0.792683      9   -7   -10              1  ...  0.74509  0.48369  0.19640  0.47713  0.31017 -0.05085 -0.00337 -0.11448  0.53872 -0.63758  61107.987       
# 60    16   58   27    989            286.496  1005  0.800088     -8    4    -4             -5  ...  1.05530  0.25728  0.23871  0.45668  0.21340 -0.17288  0.36364 -0.46465  0.44781 -0.03691  61107.989       
# 61    16   58   27    991            287.798   970  0.742648      4    0     4             -1  ...  0.87891  0.07410  0.30921 -0.48595  0.13524 -0.26441  0.93603  0.07744  0.01010 -0.22483  61107.991       
# 62    16   58   27    993            289.100  1077  0.706253     -4   -3     3              4  ...  0.95697  0.25625  0.22460 -0.45243  0.13027  0.02712  1.21141  1.03378 -0.42424 -0.80201  61107.993       
# 63    16   58   27    995            290.402   917  0.895698      8    5     5             -7  ...  1.13640  0.47237  0.09971  0.34422  0.21216  0.25085  1.18121  0.98653 -0.12795 -0.14094  61107.995       

# [5 rows x 45 columns]
# shape of data for curves
# (64, 4)
# time span of data for curves
# 61107.934  to  61107.995
# shape of data for bars
# (64, 4)
# save main dataframe to csv file at data//update_data//LatestData.csv