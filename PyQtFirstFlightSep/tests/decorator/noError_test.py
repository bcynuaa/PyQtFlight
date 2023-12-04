'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-07 02:46:47
 # @ description: test for decorator.noError
 '''

from time import sleep
from src.decorator.NoError import noError

@noError
def run() -> None:
    print(a)
    pass

for i in range(10):
    run()
    sleep(0.1)
    pass

# expect output:

# decorator: NoError.py is imported.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.
# an error occur in function: run, abort `noError` for debugging.