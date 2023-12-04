'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 00:20:47
 # @ description: utils for CallbackOnQThread
 '''

from PySide2.QtCore import QThread, Signal, Slot

def doNothing(*args, **kwargs) -> None:
    pass

class CallbackOnQThread(QThread):
    
    finished_signal = Signal()
    
    # -------------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.callback: 'function' = doNothing
        self.finished_callback: 'function' = doNothing
        pass
    
    # -------------------------------------------------------------------------------------------------
    
    def setCallback(self, callback: 'function') -> None:
        self.callback: 'function' = callback
        pass
    
    def setFinishedCallback(self, finished_callback: 'function') -> None:
        self.finished_callback: 'function' = finished_callback
        pass
    
    # -------------------------------------------------------------------------------------------------
    
    @Slot()
    def finishedCallback(self) -> None:
        self.finished_callback()
        self.deleteLater()
        pass
    
    # -------------------------------------------------------------------------------------------------
    
    def run(self) -> None:
        self.finished_signal.connect(self.finishedCallback)
        self.callback()
        self.finished_signal.emit()
        pass
    
    # -------------------------------------------------------------------------------------------------
    
    def __del__(self) -> None:
        print("%s.%s is finished" % (self.__class__.__name__, self.callback.__name__))
        pass
    
    # -------------------------------------------------------------------------------------------------
    
    pass

print("utils: CallbackOnQThread.py is imported")