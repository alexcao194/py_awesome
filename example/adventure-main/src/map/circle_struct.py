from py_awesome import *
from src.configs.assets import Assets

class CircleStruct(Entity):
    def __init__(self):
        super().__init__(hitbox=Vector2(230, 175), position=Vector2(582, 49), size=Vector2(230, 175), offset=Vector2(0, 0))
        self.texture = Texture(texture=Assets.tt_well_0, entity=self)
        self.positions = []
        self.is_solid = False
        self.is_active = False
    
    def __update__(self, event):
        if(not self.is_active and self.check()):
            self.change_state()
        if(len(self.positions) == 4):
            self.positions = []

    def change_state(self):
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)
        self.is_active = True
    
    def check(self):
        check_list = [3, 4, 2, 1]
        if(len(self.positions) != len(check_list)):
            return False
        for i in range(len(self.positions)):
            if(self.positions[i] != check_list[i]):
                return False
        return True
    
