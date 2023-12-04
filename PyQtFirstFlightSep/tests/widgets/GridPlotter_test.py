'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-01 00:19:14
 # @ description: test for widgets.GridPlotter
 '''
 
import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from src.widgets.GridPlotter import GridPlotter
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
        self.grid_plotter: GridPlotter = GridPlotter()
        self.setCentralWidget(self.grid_plotter)
        self.grid_plotter.connectWithGrid(backend_manager.getFlightTestGrid())
        pass
    
    pass

if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    # backend_manager.updateGrids()
    # make a thread to do updateGrids()
    import threading
    thread: threading.Thread = threading.Thread(target=backend_manager.updateGrids)
    thread.start()
    # thread.join()
    sys.exit(app.exec_())
    pass

# expected output:

# config: LanguageConfig.py is imported
# language: chinese, encoding: utf-8
# config path: .//config\chinese
# config.libs: PyvistaConfig.py is imported.
# config.widgets: GridPlotterConfig.py is imported.
# widgets: GridPlotter.py is imported.
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
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0260012149810791 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009808540344238281 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001071929931640625 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0018968582153320312 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001003265380859375 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.002001523971557617 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001964569091796875 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0008924007415771484 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010042190551757812 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.000957489013671875 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.002000570297241211 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010633468627929688 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0008828639984130859 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010204315185546875 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0008649826049804688 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001039743423461914 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010097026824951172 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009989738464355469 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010037422180175781 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009274482727050781 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009922981262207031 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009963512420654297 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009827613830566406 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0018913745880126953 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010089874267578125 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0018839836120605469 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009989738464355469 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0008792877197265625 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0009760856628417969 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001051187515258789 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.001867055892944336 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.0010457038879394531 seconds.
# ----------------------------------------------------------------------
# Function updateGrids costs 0.5531275272369385 seconds.
# ----------------------------------------------------------------------