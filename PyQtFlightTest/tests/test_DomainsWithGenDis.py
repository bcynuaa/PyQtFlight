'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 19:16:10
 # @ license: Mozilla Public License 2.0
 # @ description: the file is used to test DomainsWithGenDis
 '''
 
from src.DomainsWithGenDisClass import DomainsWithGenDis

domain_files_path: str = "..//..//TestData//ProjectFlightTest2//Domains//"
domains_with_gen_dis: DomainsWithGenDis = DomainsWithGenDis()
domains_with_gen_dis.loadDomainFilesFromPath(domain_files_path)
print(domains_with_gen_dis)

ug = domains_with_gen_dis.getUnstructuredGrid([1,2,3,4,5], 0.2)
ug.plot(show_edges=True, show_grid=True, notebook=False)
domains_with_gen_dis.addGenDisToUnstructuredGrid(ug, [-1,-2,-3,-4,-5], 0.2)
ug.plot(show_edges=True, show_grid=True, notebook=False)


# result:

# config: Name.py is imported.
# config: Pyvista settings have been finished.
# utils: RegularExpression.py is imported.
# src: DomainsWithGenDisClass.py is imported.
# --------------------------------------------------
# DomainsWithGenDis
# data path: ..//..//TestData//ProjectFlightTest2//Domains//
# number of domains: 48
# number of points: 11462
# number of cells: 9996
# number of general displacement: 5
# --------------------------------------------------