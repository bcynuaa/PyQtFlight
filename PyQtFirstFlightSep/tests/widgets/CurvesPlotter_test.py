'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-30 01:16:53
 # @ description: test for widgets.CurvesPlotter
 '''

import sys
import time
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow

from src.widgets.CurvesPlotter import CurvesPlotter
from src.backend.BackendManager import BackendManager

backend_manager: BackendManager = BackendManager()
data_path: str = "data//domains_data//"
map_matrix_filename: str = "data//grids_data//SensorsMap.dat"
standard_mode_response_filename: str = "data//grids_data//StandardModeResponse.dat"
latest_data_filename: str = "data//update_data//LatestData.dat"

backend_manager.loadDomainsFromPath(data_path)
backend_manager.loadMapMatrix(map_matrix_filename)
backend_manager.loadStandardModeResponse(standard_mode_response_filename)
backend_manager.buildBackend()

for i in range(100):
    backend_manager.readLatestData(latest_data_filename)
    pass

class MainWindow(QMainWindow):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.curves_plotter: CurvesPlotter = CurvesPlotter()
        self.setCentralWidget(self.curves_plotter)
        self.curves_plotter.setCurvesNumber(backend_manager.getCurvesNumber())
        pass
    
    pass

if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    start_time: float = time.time()
    backend_manager.readLatestData(latest_data_filename)
    latest_time_data: np.ndarray = backend_manager.getLatestTimeDataForCurves()
    backend_manager.getLatestSensorDataForBars()
    window.curves_plotter.plot(latest_time_data, \
        backend_manager.getLatestFlightTestSensorDataForCurves())
    window.curves_plotter.plot(latest_time_data, \
        backend_manager.getLatestSimulationSensorDataForCurves())
    end_time: float = time.time()
    print("time cost for one loop in backend_manager + curves plotter: %f" % (end_time - start_time))
    sys.exit(app.exec_())
    pass

# expected output:

# config.widgets: CurvesPlotterConfig.py is imported.
# widget: CurvesPlotter is imported
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
# time cost for one loop in backend_manager + curves plotter: 0.019092