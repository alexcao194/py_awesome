from ...game.widget.widget import Widget
from ...utils.vector2 import Vector2
import pygame

class Image(Widget):
    '''
    Image is a widget that displays an image.
    image: str - the image to display
    '''
    
    def __init__(self, src: str = None, position: Vector2 = None, size: Vector2 = None, scale: Vector2 = Vector2(1, 1)):
        if(src == None):
            raise Exception("Image must have an image")
        if(not scale.is_positive()):
            raise Exception("Scale must be positive")
        self.image = src
        self.scale = scale
        self.__init_image__()
        if(size == None):
            self.size = Vector2(self.image.get_size()[0], self.image.get_size()[1])
        else:
            self.size = size
        super().__init__(position=position, size=self.size)
    
    def __init_image__(self):
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale.x), int(self.image.get_height() * self.scale.y)))
        self.size = Vector2(self.image.get_size()[0], self.image.get_size()[1])
    
    def __render__(self, display):
        display.blit(self.image, (self.position.x + self.size.x / 2 - self.image.get_width() / 2, self.position.y + self.size.y / 2 - self.image.get_height() / 2))
    