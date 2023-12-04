'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-09 03:22:40
 # @ description: utils for KeyExaminer
 '''

import os
import json
import hashlib

encoding: str = "utf-8"
encrypted_keys_json_filename: str = ".//resources//keys//encrypted_keys.json"

if os.path.exists(encrypted_keys_json_filename):
    encrypted_keys_json: dict = json.load( \
        open(encrypted_keys_json_filename, "r", encoding=encoding))
    pass
else:
    encrypted_keys_json = {}
    pass

class KeyExaminer:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setUsername(self, username: str) -> None:
        self.username: str = username
        self.encrypted_username: str = hashlib.sha224(self.username.encode(encoding)).hexdigest()
        pass
    
    def setPassword(self, password: str) -> None:
        self.password: str = password
        self.encrypted_password: str = hashlib.sha256(self.password.encode(encoding)).hexdigest()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def check(self) -> bool:
        if self.encrypted_username in encrypted_keys_json:
            if self.encrypted_password == encrypted_keys_json[self.encrypted_username]:
                return True
                pass
            else:
                return False
                pass
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("utils: KeyExaminer is imported")