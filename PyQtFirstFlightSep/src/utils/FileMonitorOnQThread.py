'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-04 19:56:47
 # @ description: util for FileMonitorOnQThread
 '''

from PySide2.QtCore import QThread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileModifiedEvent, FileCreatedEvent, FileDeletedEvent, FileMovedEvent

def doNothing(*args, **kwargs) -> None:
    pass

class Handler(FileSystemEventHandler):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.modified_callback: 'function' = doNothing
        self.created_callback: 'function' = doNothing
        self.deleted_callback: 'function' = doNothing
        self.moved_callback: 'function' = doNothing
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setModifiedCallback(self, modified_callback: 'function') -> None:
        self.modified_callback: 'function' = modified_callback
        pass
    
    def setCreatedCallback(self, created_callback: 'function') -> None:
        self.created_callback: 'function' = created_callback
        pass
    
    def setDeletedCallback(self, deleted_callback: 'function') -> None:
        self.deleted_callback: 'function' = deleted_callback
        pass
    
    def setMovedCallback(self, moved_callback: 'function') -> None:
        self.moved_callback: 'function' = moved_callback
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def on_modified(self, event: FileModifiedEvent) -> None:
        if not event.is_directory:
            self.modified_callback(event.src_path)
            pass
        pass
    
    def on_created(self, event: FileCreatedEvent) -> None:
        if not event.is_directory:
            self.created_callback(event.src_path)
            pass
        pass
    
    def on_deleted(self, event: FileDeletedEvent) -> None:
        if not event.is_directory:
            self.deleted_callback(event.src_path)
            pass
        pass
    
    def on_moved(self, event: FileMovedEvent) -> None:
        if not event.is_directory:
            self.moved_callback(event.src_path)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

class FileMonitorOnQThread(QThread):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.handler: Handler = Handler()
        self.observer: Observer = Observer()
        self.monitor_path: str = ""
        self.stop_flag: bool = True
        self.recursive: bool = True
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setMonitorPath(self, monitor_path: str) -> None:
        self.monitor_path: str = monitor_path
        self.observer.schedule(self.handler, self.monitor_path, recursive=self.recursive)
        pass
    
    def setModifiedCallback(self, modified_callback: 'function') -> None:
        self.handler.setModifiedCallback(modified_callback)
        pass
    
    def setCreatedCallback(self, created_callback: 'function') -> None:
        self.handler.setCreatedCallback(created_callback)
        pass
    
    def setDeletedCallback(self, deleted_callback: 'function') -> None:
        self.handler.setDeletedCallback(deleted_callback)
        pass
    
    def setMovedCallback(self, moved_callback: 'function') -> None:
        self.handler.setMovedCallback(moved_callback)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def run(self) -> None:
        self.stop_flag = False
        self.observer.start()
        pass
    
    def stop(self) -> None:
        self.stop_flag = True
        self.observer.stop()
        self.quit()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("utils: FileMonitorOnQThread.py is imported")