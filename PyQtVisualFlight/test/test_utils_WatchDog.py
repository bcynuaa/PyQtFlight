# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to test the utils.FileObserber.py

from test_Header import *
from utils.FileObserver import *

wd: WatchDog = WatchDog(
    "./draft",
    sleep_time=1.0,
    callback_on_created=lambda: print("created"),
    callback_on_deleted=lambda: print("deleted"),
    callback_on_modified=lambda: print("modified"),
    callback_on_moved=lambda: print("moved")
)

wd.start()

###################################################################################################
# results should be:

# workspace directory included
# WatchDog has been loaded.
# modified
# modified
# modified
# modified
# modified
# modified
# modified
# modified