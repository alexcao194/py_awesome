from py_awesome import *
from src.configs.assets import Assets


class Block(Entity):
    def __init__(self, texture : str ,hitbox:Vector2, size: Vector2, offset: Vector2, position: Vector2):
        super().__init__(hitbox=hitbox, position=position, size=size, offset=offset)
        self.show_hitbox=False
        self.texture = Texture(texture=texture, entity=self)

