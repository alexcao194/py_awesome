from py_awesome import *
from src.configs.assets import Assets

class Box(Entity):
    def __init__(self):
        super().__init__(hitbox=Vector2(32, 32), position=Vector2(582 + 100, 49 + 50), size=Vector2(32, 49), offset=Vector2(0, 17))
        self.texture = Texture(texture=Assets.tt_box_1, entity=self)
        self.is_solid = True
        self.is_active = False
        self.show_hitbox = False

    def change_state(self):
        self.texture = Texture(texture=Assets.tt_box_0, entity=self)
        self.is_active = True
    
