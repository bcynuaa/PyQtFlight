[toc]

# PyQtAeroelastic

## Warning

A `PyQt` project for Aeroelasticity using PyVista.

> Warning: This project is used only to read and display professor **Tongqing Guo** and his research group's CFD codes' output file. For this `PyQt` project is not integrated closely with backend's `Fortran` code, it's possible to store the codes in a public repository. The ownership of the code belongs to Tongqing Guo and his research group.

To avoid some research security, I have removed `test_data/` from `data/`, but you may find the exported file in image to see what this project can do.

## Requirement

This project is based on `python` . Here's the list of package used in this project with its version and function it performs.

| package | verion | function |
| - | - | - |
| `numpy` | 1.24.2 | read and store array like data |
| `matplotlib` | 3.7.0 | plot the curve of signals in time domain |
| `pyside2` | 5.15.2.1 | the base of UI design |
| `pyvista` | 0.38.3 | to read and display 3D object |
| `pyvistaqt` | 0.9.1 | interact between pyvista and PyQt |
| `sphinx` | 6.2.0 | generate doc of codes |
| `pyinstaller` | 5.9.0 | convert the python project to exe |
| `pytest` | 7.3.1 | test the python code |
| `trame` | 2.3.2 | plot pyvista inside jupyter=notebook |
| `ipywidgets` | 7.6.5 | widget used in jupyter-notebook |
| `imageio` | 2.9.0 | export image of pyvista |
| `imageio-ffmpeg` | 0.4.5 | export video of pyvista |
| `tqdm` | 4.623 | automatic progress bar |

## Build

You may change the `main.spec` file to your own PC path and run `pyinstaller main.spec` in the root path to attain `exe`.