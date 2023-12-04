'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-17 00:02:05
 # @ description: decorator for clock
 '''

import time

def clock(func: 'function') -> 'function':
    def func_wrapper(*args, **kwargs) -> any:
        print("-" * 70)
        start_time: float = time.time()
        result: any = func(*args, **kwargs)
        end_time: float = time.time()
        time_cost: float = end_time - start_time
        print(f"Function {func.__name__} costs {time_cost} seconds.")
        print("-" * 70)
        return result
        pass
    return func_wrapper
    pass

print("decorator: Clock.py is imported.")