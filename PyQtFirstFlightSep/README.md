[toc]

---

# PyQtFirstFlightSep

A repository for first flight's QT-UI in September using `PySide2`.

---

# Author and Copyright

The code's original author is Chenyu Bao, a member of Prof Tongqing Guo's research group in the Nanjing University of Aero. and Astro. The code services for the first flight of some aircraft in September, 2023. The code is written in `Python 3.8.5`, with GUI frame by `PySide2`. The code is licensed under the `Mozilla Public License 2.0`.

For this flight project is leaded by 601, copyright belongs to this organization.

---

# Package and Installation

## Package

Below is a list of packages required to run the program. Moreover, a python's minimum required version is `3.8.5`.

| Package | minimum version | usage |
| - | - | - |
| `numpy` | 1.19.2 | for array like data structure |
| `pandas` | 1.1.3 | for data flow storage |
| `fsspec` | 0.8.4 | for `csv` file save |
| `tabulate` | 0.8.7 | for pretty `csv` file save |
| `PySide2` | 5.15.1 | for GUI framework |
| `pyvista` | 0.27.3 | for 3D visualization |
| `pyvistaqt` | 0.5.0 | for interactive 3D visualization in QT |
| `imageio` | 2.9.0 | for image read and write, especially for `gif` |
| `imageio-ffmpeg` | 0.4.3 | for `ffmpeg` support in `imageio` |
| `pyqtgraph` | 0.11.0 | for fast updating 2D plot |
| `pglive` | 0.0.1 | for thread-safe 2D plot based on `pyqtgraph` |
| `watchdog` | 0.10.3 | for file system monitoring in updating |

What's more, `json` is used here to read `config` files and `hashlib` is used to generate encrypted username and password. These two packages are built-in in python.

## Installation

The installation of program is supported by `pyinstaller`. I provide 2 versions of `spec` files for debug and release. The debug version is used for development and the release version is used for deployment. The debug version is not recommended to be used in deployment. The most important difference between these two versions is the `console` option. The debug version has `console` option while the release version does not. The `console` option is used to show the `stdout` and `stderr` in the console. The release version is recommended to be used in deployment.

Below is the command to install debug version.

```shell
pyinstaller install_debug.spec
```

Below is the command to install release version.

```shell
pyinstaller install_release.spec
```

---

# Usage

## Run the Program

## Config Files

---

# Warnings

## Platform

The program is developed and tested in `Windows 11`. In my personal working process, both `win7`, `win10` and `win11` platform works well in case you choose the right version of `python`, `pyinstaller` and site-packages. However, I do not guarantee the program can work well in other platforms.

For example, I've tested this code on `fedora 38`, but an error occur in `pyvistaqt`. I've tried to solve this problem but failed. So I do not recommend to use this code in `Linux` platform.

For safety issue, 601 may change platform to `Kylinos` or `Deepin` in the future. Although `PySide2` supports both `window` and `Linux` platform, I have no idea on whether the program can still work well in `Kylinos` or `Deepin`.

## Encoding of Config Files

As 601 requires that all characters in the program should be chinese, I have to use `utf-8` encoding in all files. In `win10` or higher, a text file's default encoding is `utf-8`. However, in `win7` or lower, a text file's default encoding is `gbk`. So if you use `win7` or lower, you should make sure that all config files are encoded in `utf-8`.

An alternative way is to change `config//language.json` to ensure all congig files are encoded in `gbk` or `utf-8`. However, this method is not recommended.

To avoid changes on encoding, `vim`, `notepad++` or `vscode` are recommended to be used to edit config files on `win7` or lower.

---
