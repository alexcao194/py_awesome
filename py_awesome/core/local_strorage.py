from ..core.singleton import Singleton
import json

class LocalStorage(Singleton):
    file_path = 'py_awesome/local_storage/local.json'
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
    