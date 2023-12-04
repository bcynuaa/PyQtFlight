# coding = "utf-8"
# author: bcynuaa
# date  : 2023/05/04

###################################################################################################
# This file is used to define timer class

from PySide2.QtCore import QTimer

class AutoDisplayTimer:
    
    def __init__(
        self,
        callbackIndexFunction,
        skip_step: int = 1,
        start_step: int = 0,
        end_step: int = 100
    ) -> None:
        self.callbackIndexFunction: function = callbackIndexFunction
        self.skip_step: int = skip_step
        self.start_step: int = start_step
        self.end_step: int = end_step
        self.current_step: int = start_step
        self.timer: QTimer = QTimer()
        self.timer.timeout.connect(self.slot_timer)
        pass
    
    def start(self) -> None:
        self.current_step = self.start_step
        self.timer.start()
        pass
    
    def slot_timer(self) -> None:
        if self.current_step >= self.end_step:
            self.timer.stop()
            pass
        else:
            self.callbackIndexFunction(self.current_step)
            self.current_step += self.skip_step
            self.timer.start()
            pass
        pass
    
    pass

####################################################################################################