# coding="utf-8"
# author: bcynuaa
# date: 2023/04/27

###################################################################################################
# This file is used to include the workspace directory

import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

import pyvista
pyvista.set_jupyter_backend("trame")

print("workspace directory included")

###################################################################################################