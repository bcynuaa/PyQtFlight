# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to test the utils.PatternMatch.py

from test_Header import *
from utils.PatternMatch import *

test_data_file_list: list = ["domain001.dat", "DOMAIN02.dat", "Domain3.dat"]
print(getDomainFilesList(test_data_file_list))

###################################################################################################
# results should be:

# workspace directory included
# ['DOMAIN02.dat', 'Domain3.dat', 'domain001.dat']