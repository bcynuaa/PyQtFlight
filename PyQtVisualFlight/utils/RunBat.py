# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/19

###################################################################################################
# This file is used to run bat from any path

import os
import subprocess

def runBatFromAbsPath(bat_file_abspath: str) -> None:
    """Run bat from absolute path

    Args:
        bat_file_abspath (str): bat file absolute path
    """
    bat_file_absdir: str = os.path.dirname(bat_file_abspath)
    subprocess.call([bat_file_abspath], cwd=bat_file_absdir)
    pass

print("Run bat has been loaded.")

###################################################################################################