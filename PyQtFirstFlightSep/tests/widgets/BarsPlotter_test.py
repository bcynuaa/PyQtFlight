'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-31 16:41:11
 # @ description: test for widgets.BarsPlotter
 '''

import sys
import time
from PySide2.QtWidgets import QApplication, QMainWindow

from src.widgets.BarsPlotter import BarsPlotter
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
        self.bars_plotter: BarsPlotter = BarsPlotter()
        self.setCentralWidget(self.bars_plotter)
        pass
    
    pass

if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    window.bars_plotter.setBarsNumber(backend_manager.getBarsNumber())
    start_time: float = time.time()
    backend_manager.readLatestData(latest_data_filename)
    backend_manager.getLatestTimeDataForCurves()
    backend_manager.getLatestFlightTestSensorDataForCurves()
    backend_manager.getLatestSimulationSensorDataForCurves()
    backend_manager.getLatestParametersMarkdownTable()
    window.bars_plotter.plot(backend_manager.getLatestSensorDataForBars())
    end_time: float = time.time()
    print("time cost for one loop in backend_manager + bars plotter: %f" % (end_time - start_time))
    sys.exit(app.exec_())
    pass

# expected output:

# config: LanguageConfig.py is imported
# language: chinese, encoding: utf-8
# config path: .//config\chinese
# config.widgets: BarsPlotterConfig is imported
# widgets: BarsPlotter is imported
# config.libs: PyvistaConfig.py is imported.
# config.backend: BackendManagerConfig.py is imported
# decorator: Clock.py is imported.
# config.backend: GridsConfig.py imported
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
# time cost for one loop in backend_manager + bars plotter: 0.027882