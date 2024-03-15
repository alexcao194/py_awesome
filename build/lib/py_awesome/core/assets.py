from ..core.singleton import Singleton
import os
import pathlib

class Assets(Singleton):
    # ic_blank_check_box = 'py_awesome/assets/blank_check_box.png'
    # ic_selected_check_box = 'py_awesome/assets/selected_check_box.png'
    # font = 'py_awesome/assets/iciel_pony.ttf'

    ic_blank_check_box = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'assets', 'blank_check_box.png')
    ic_selected_check_box = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'assets', 'selected_check_box.png')
    font = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'assets', 'iciel_pony.ttf')