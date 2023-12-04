'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-07 02:37:53
 # @ description: decorator for noError
 '''

def noError(func: 'function') -> 'function':
    def func_wrapper(*args, **kwargs) -> any:
        try:
            result: any = func(*args, **kwargs)
            return result
            pass
        except:
            print("an error occur in function: %s, abort `noError` for debugging." % func.__name__)
            return None
            pass
        pass
    return func_wrapper
    pass

print("decorator: NoError.py is imported.")