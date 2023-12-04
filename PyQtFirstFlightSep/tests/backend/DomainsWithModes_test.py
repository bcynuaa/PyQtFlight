'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: test for backend.DomainsWithModes
 '''

from src.backend.DomainsWithModes import DomainsWithModes

data_path: str = "data//domains_data//"

domains_with_modes: DomainsWithModes = DomainsWithModes()
domains_with_modes.loadDomainFilesFromPath(data_path)

print(domains_with_modes)
print("mode shape array shape %s" % str(domains_with_modes.getModeShape([1, 2, 3]).shape))

domains_with_modes.addModeResponseToGrid(domains_with_modes.unstructured_grid, [1, 2, 3], 1)

domains_with_modes.unstructured_grid.plot()

# expect results:

# config: PyvistaConfig.py is imported.
# config: DomainsWithModesConfig.py is imported
# backend: DomainsWithModes is imported.
# domains loaded: True
# data path: data//domains_data//
# number of domains: 6
# number of points: 9750
# number of cells: 9216
# number of modes: 3
# active scalar: az
# active scalar index: 2
# all active scalars: ['ax', 'ay', 'az']
# mode shape array shape (9750, 3)