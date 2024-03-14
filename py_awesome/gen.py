from pathlib import Path
import json

def gen():
    folder_path = 'strings/'

    folder = Path(folder_path)

    def create_property(key, value, script):
        script.write(f'''
        @property
        def {key}(self):
            return Localization.strings[Localization.language]['{key}']
        ''')

    script = open('py_awesome/core/localization.py', 'w', encoding='utf-8')
    script.write('''from py_awesome.core.singleton import Singleton
    class Localization(Singleton):
        language = 'en'
        languages = set()
        strings = dict()
    ''')

    if folder.exists() and folder.is_dir():
        files = list(folder.glob('*'))
        dic = dict()
        languages = set()
        for file in files:
            local = file.name.split('.')[0]
            data = json.load(file.open(encoding='utf-8'))
            dic[local] = data
            languages.add(local)
    else:
        print(f"Folder does not exist or is not a directory: {folder}")

    script.write('''    languages = ''' + str(languages) + '\n')
    script.write('''    strings = ''' + str(dic) + '\n')

    for key, value in dic['en'].items():
            create_property(key, value, script)

    script.close()
    print("Generated localization.py successfully!!!")

    # Gen assests

    def create_ani_assets(name, path, script):
        script.write(f'''   ani_{name.lower()} = '{path.as_posix()}/'
    ''')
        
    def create_texture_assets(name, path, script):
        script.write(f'''   tt_{name.lower()} = '{path.as_posix()}'
    ''')
        
    def create_sound_assets(name, path, script):
        script.write(f'''   sd_{name.lower()} = '{path.as_posix()}'
    ''')
        
    def genAniPath(path: Path, script):
        isEnd = True
        for file in path.glob('*'):
            if file.is_dir():
                isEnd = False
                genAniPath(file, script)   
        if isEnd:
            create_ani_assets(path.name, path, script)
        
    def genTexturePath(path: Path, script):
        for file in path.glob('*'):
            if file.is_dir():
                genTexturePath(file, script)   
            else:
                name = file.name.split('.')[0]
                create_texture_assets(name, file, script)
                
    def genSoundPath(path: Path, script):
        for file in path.glob('*'):
            if file.is_dir():
                genSoundPath(file, script)   
            else:
                name = file.name.split('.')[0]
                create_sound_assets(name, file, script)
        
    folder_path = 'assets/'
    folder = Path(folder_path)

    script = open('src/configs/assets.py', 'w', encoding='utf-8')
    script.write('''from framework.framework import *

    class Assets(Singleton):
    ''')    
            
    if folder.exists() and folder.is_dir():
        script.write('    # Animations\n')
        ani_folder = list(folder.glob('animations'))
        genAniPath(ani_folder[0], script)
        
        script.write('\n# Textures\n')
        textures_folder = list(folder.glob('textures'))
        genTexturePath(textures_folder[0], script)
        
        script.write('\n# Sounds\n')
        sounds_folder = list(folder.glob('sounds'))
        genSoundPath(sounds_folder[0], script)
        
    else:
        print(f"Folder does not exist or is not a directory: {folder}")
        
    script.close()
    print("Generated assets.py successfully!!!")