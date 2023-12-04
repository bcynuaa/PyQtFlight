# -*- mode: python ; coding: utf-8 -*-


import os
import sys
sys.setrecursionlimit(100000)


block_cipher = None


a = Analysis(
    [
        ".//PyQtFirstFlightSep.py",
    ],
    pathex=[],
    binaries=[],
    datas=[
        (".//LICENSE", "."),
        (".//README.md", "."),
        (".//config", ".//config"),
        (".//resources", ".//resources"),
        (".//data", ".//data"),
    ],
    hiddenimports=[
        "hashlib",
        "json",
        "numpy",
        "pandas",
        "fsspec",
        "tabulate",
        "PySide2",
        "pyvista",
        "pyvistaqt",
        "imageio",
        "imageio_ffmpeg",
        "pyqtgraph",
        "pglive",
        "watchdog",
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
    name="PyQtFirstFlightSep",
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
    icon="resources//icons//exe_icon.png",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="release",
)