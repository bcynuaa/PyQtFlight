# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/21

###################################################################################################
# This file is used to contain the thread for watchdog

# ref:
# https://blog.csdn.net/lly1122334/article/details/110475197
# https://blog.csdn.net/jia666666/article/details/81674427

from PySide2.QtCore import QThread

from utils.FileObserver import callback_none

DEFAULT_MAX_ITERATIONS = 100000000

class Thread(QThread):     
	
    def __init__(self, callbackFunction) -> None:
        """__init__ for Thread

        Args:
            callbackFunction (_type_): _description_
        """
        super(Thread, self).__init__()
        self.callbackFunction = callbackFunction
        self.working: bool = True
        pass
    
    def __del__(self) -> None:
        """__del__ for Thread
        """
        self.working = False
        pass
			
    def run(self) -> None:
        """run for Thread
        """
        for i in range(DEFAULT_MAX_ITERATIONS):
            if self.working == True:
                try:
                    self.callbackFunction()
                    pass
                except:
                    pass
                pass
            else:
                break
                pass
            pass
        pass
    
    def kill(self) -> None:
        """kill for Thread
        """
        self.working = False
        self.callbackFunction = callback_none
        pass
    
    pass

print("Thread for watchdog has been loaded.")

###################################################################################################