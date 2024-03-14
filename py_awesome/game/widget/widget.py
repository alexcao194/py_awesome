from ...utils.vector2 import Vector2
import pygame

class Widget:
    '''
    Widget is the base class for all widgets.
    position: Vector2 - the position of the widget
    size: Vector2 - the size of the widget
    '''
    def __init__(self, position: Vector2, size: Vector2):
        if(self.__class__.__name__ == 'Widget'):
            raise Exception("Widget cannot be instantiated")
        if(position == None):
            raise Exception("Widget must have a position")
        if(size == None):
            raise Exception("Widget must have a size")
        if(not size.is_positive()):
            raise Exception("Size must be positive")
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position.to_tuple(), size.to_tuple())
    
    def __render__(self, display):
        pass

    def __update__(self, event):
        pass