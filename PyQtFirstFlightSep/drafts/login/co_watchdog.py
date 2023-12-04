import sys
import time
from PySide2.QtCore import QThread, Signal as pyqtSignal
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class WatchdogThread(QThread):
    file_changed = pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.stop_flag = False

    def run(self):
        event_handler = WatchdogEventHandler(self.file_changed)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while not self.stop_flag:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_flag = True
            self.observer.stop()
        self.observer.join()

    def stop(self):
        self.stop_flag = True
        self.observer.stop()
        self.quit()
        print("Stopping thread...")

class WatchdogEventHandler(FileSystemEventHandler):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            self.signal.emit(f"File created: {event.src_path}")
        elif event.event_type == 'modified':
            self.signal.emit(f"File modified: {event.src_path}")
        elif event.event_type == 'deleted':
            self.signal.emit(f"File deleted: {event.src_path}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Watching...")
        self.button = QPushButton("Stop")
        self.button.clicked.connect(self.stop_thread)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.thread = WatchdogThread('.')
        self.thread.file_changed.connect(self.label.setText)
        self.thread.start()

    def stop_thread(self):
        self.thread.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())