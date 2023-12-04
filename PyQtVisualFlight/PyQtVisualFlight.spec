# -*- mode: python ; coding: utf-8 -*-


import os
import sys
sys.setrecursionlimit(100000)


block_cipher = None


a = Analysis(
    [
        './/PyQtVisualFlight.py',

        './/ui//Ui_MainWindow.py',

        './/config//__init__.py',
        './/config//Base.py',
        './/config//MatplotlibSettings.py',
        './/config//PyVistaSettings.py',
        './/config//ThingsInMatplotlib.py',
        './/config//ThingsInMainWindow.py',

        './/utils//__init__.py',
        './/utils//FileObserver.py',
        './/utils//PatternMatch.py',
        './/utils//RunBat.py',
        './/utils//ThreadWatchdog.py',

        './/src//__init__.py',
        './/src//InteractiveClass.py',
        './/src//Logic_MainWindow.py',
        './/src//MatplotlibClass.py',
        './/src//MeshClass.py',
    ],
    pathex=[
        os.getcwd(),
    ],
    binaries=[],
    datas=[],
    hiddenimports=[
        'numpy',
        'matplotlib',
        'pyvista',
        'pyvistaqt',
        'PySide2',
        'imageio',
        'imageio_ffmpeg',
        'watchdog'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyQtVisualFlight',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='.//resources//icon//paper_plane.png',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyQtVisualFlight',
)