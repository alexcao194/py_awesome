from ...game.entity.entity import Entity
from ...utils.vector2 import Vector2
import pygame

class Texture:
    '''
    Texture is a class that represents a texture of an entity.
    '''
    def __init__(self, texture: str = None, entity = None):
        if(texture == None):
            raise Exception("Texture must have a texture source")
        if(entity == None):
            raise Exception("Texture must have an entity")
        self.texture = texture
        self.entity = entity
        self.__init_image__()
    
    def __init_image__(self):
        self.image = pygame.image.load(self.texture)
        self.image = pygame.transform.scale(self.image, self.entity.size.to_tuple())
        
    def __render__(self, display):
        display.blit(self.image, self.entity.position.to_tuple())
