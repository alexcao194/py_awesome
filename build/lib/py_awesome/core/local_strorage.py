from ..core.singleton import Singleton
import json
import os
import pathlib
class LocalStorage(Singleton):
    # path to the local storage file, default is local.json
    # file_path = '../../local_storage/local.json'
    file_path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'local_storage', 'local.json')

    with open(file_path, 'r') as file:
        data = json.load(file)
        
    def get_value(key, dafault_value):
        if key in LocalStorage.data:
            return LocalStorage.data[key]
        else:
            return dafault_value

    def put_value(key, value):
        LocalStorage.data[key] = value
        with open(LocalStorage.file_path, 'w') as file:
            json.dump(LocalStorage.data, file)
    