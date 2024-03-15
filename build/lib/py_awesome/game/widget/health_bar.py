import pygame
from ...game.widget.widget import Widget
from ...utils.vector2 import Vector2
from ...game.entity.entity import Entity

class HealthBar(Widget):
    def __init__(self, size: Vector2 = None, entity: Entity = None, offset: Vector2 = None):
        if(entity == None):
            raise Exception("HealthBar must have an entity")
        if(offset == None):
            raise Exception("HealthBar must have an offset")
        super().__init__(position=entity.position + offset, size=size)
        self.entity = entity
        self.max = self.entity.max_hp
        self.current = self.entity.hp
        self.offset = offset

    def __update__(self, event):
        super().__update__(event=event)
        self.current = self.entity.hp
        self.position = self.entity.position + self.offset
    
    def __render__(self, display):
        if(self.entity.alive == False):
            return
        super().__render__(display=display)
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(self.position.to_tuple(), self.size.to_tuple()))
        pygame.draw.rect(display, (0, 255, 0), pygame.Rect(self.position.to_tuple(), (self.size.x * (self.current / self.max), self.size.y)))
