# -*- mode: python ; coding: utf-8 -*-


import os
import sys
sys.setrecursionlimit(100000)


block_cipher = None


a = Analysis(
    [
        './PyQtAeroelastic.py',
        './/ui//Ui_MainWindow.py',
        './/src//__init__.py',
        './/src//AuxiliaryDialog.py',
        './/src//Interactive.py',
        './/src//Logic_MainWindow.py',
        './/src//MatplotlibSettings.py',
        './/src//MatplotlibWidget.py',
        './/src//PyvistaSettings.py',
        './/src//ReadFile.py',
        './/src//ThingsInMainWindow.py',
        './/src//ThingsInPlot.py',
        './/src//TimerClass.py'
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
        'tqdm'
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
    name='PyQtAeroelastic',
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
    icon='./data/icon/paper_plane.png',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyQtAeroelastic',
)