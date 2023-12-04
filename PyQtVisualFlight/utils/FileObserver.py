# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to observe the file changes in the directory, and then call the function to do

# ref:
# https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/
# https://www.cnblogs.com/root-123/p/16720860.html
# ! https://blog.csdn.net/lly1122334/article/details/110475197
# ! on windows platform, modified action will not be triggered

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def callback_none() -> None:
    pass

class customizeHandler(FileSystemEventHandler):
    
    """customize the handler
    """
    
    def __init__(
        self,
        callback_on_created=callback_none,
        callback_on_deleted=callback_none,
        callback_on_modified=callback_none,
        callback_on_moved=callback_none,
    ) -> None:
        """customize the handler

        Args:
            callback_on_created (_type_, optional): _description_. Defaults to callback_none.
            callback_on_deleted (_type_, optional): _description_. Defaults to callback_none.
            callback_on_modified (_type_, optional): _description_. Defaults to callback_none.
            callback_on_moved (_type_, optional): _description_. Defaults to callback_none.
        """
        FileSystemEventHandler.__init__(self)
        self.callback_on_created = callback_on_created
        self.callback_on_deleted = callback_on_deleted
        self.callback_on_modified = callback_on_modified
        self.callback_on_moved = callback_on_moved
        pass

    def on_created(self, event) -> None:
        """when the file is created, call the callback function

        Args:
            event (_type_): _description_
        """
        self.callback_on_created()
        pass
    
    def on_deleted(self, event) -> None:
        """when the file is deleted, call the callback function

        Args:
            event (_type_): _description_
        """
        self.callback_on_deleted()
        pass
    
    def on_modified(self, event) -> None:
        """when the file is modified, call the callback function

        Args:
            event (_type_): _description_
        """
        self.callback_on_modified()
        pass
    
    def on_moved(self, event) -> None:
        """when the file is moved, call the callback function

        Args:
            event (_type_): _description_
        """
        self.callback_on_moved()
        pass
    
    pass

class WatchDog:
    
    def __init__(
        self,
        path: str,
        sleep_time: float = 0.5,
        callback_on_created=callback_none,
        callback_on_deleted=callback_none,
        callback_on_modified=callback_none,
        callback_on_moved=callback_none,
    ) -> None:
        """initialize the WatchDog

        Args:
            path (str): _description_
            sleep_time (float, optional): _description_. Defaults to 0.5.
            callback_on_created (_type_, optional): _description_. Defaults to callback_none.
            callback_on_deleted (_type_, optional): _description_. Defaults to callback_none.
            callback_on_modified (_type_, optional): _description_. Defaults to callback_none.
            callback_on_moved (_type_, optional): _description_. Defaults to callback_none.
        """
        # * eyesore: a person or thing that is very ugly or unpleasant to look at
        # * 眼中钉
        self.eyesore_path: str = path
        # * sleep_time: the time interval between two observations
        self.sleep_time: float = sleep_time
        self.event_handler: customizeHandler = customizeHandler(
            callback_on_created=callback_on_created,
            callback_on_deleted=callback_on_deleted,
            callback_on_modified=callback_on_modified,
            callback_on_moved=callback_on_moved
        )
        self.observer: Observer = Observer()
        self.observer.schedule(self.event_handler, self.eyesore_path, recursive=True)
        self.working: bool = True
        pass
    
    def setSleepTime(self, sleep_time: float) -> None:
        """set the sleep time

        Args:
            sleep_time (float): the time interval between two observations
        """
        self.sleep_time = sleep_time
        pass
    
    def start(self) -> None:
        """start the observer
        """
        self.observer.start()
        try:
            while self.working == True:
                time.sleep(self.sleep_time)
                pass
            pass
        except KeyboardInterrupt:
            self.observer.stop()
            pass
        self.observer.join()
        pass
    
    def end(self) -> None:
        """end the observer
        """
        self.working = False
        self.observer.stop()
        self.observer.join()
        pass
    
    pass

print("WatchDog has been loaded.")

###################################################################################################