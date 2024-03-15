from py_awesome import *
from src.configs.assets import Assets


class CollisionBox(Entity):
    def __init__(self, position: Vector2, value: int):
        super().__init__(hitbox=Vector2(40,40),size=Vector2(5,5),offset=Vector2(0,0), position=position)
        self.show_hitbox=False
        self.is_solid = False
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)
        self.value = value

