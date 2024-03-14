from ...game.widget.widget import Widget
from ...utils.vector2 import Vector2
from ...utils.media_query import MediaQuery
import pygame

class Text(Widget):
    '''
    Text is a widget that displays text.
    text: str - the text to display
    font: str - the path to the font file
    font_size: int - the size of the font
    color: tuple - the color of the text
    '''
    
    def __init__(self, text: str = None, position: Vector2 = None, size: Vector2 = None, font: str = MediaQuery.font_family, font_size: int = MediaQuery.font_size, color: tuple = (255, 255, 255)):
        if(text == None):
            raise Exception("Text must have a text")
        if(font_size < 0):
            raise Exception("Font size must be greater than 0")
        super().__init__(position=position, size=size)
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.color = color
    
    def set_text(self, text):
        self.text = text
        return self
    def __render__(self, display):
        lines = self.text.splitlines() 
        if(len(lines) > 1):
            y_offset = 0
            for i, line in enumerate(lines):
                text = self.font.render(line, True, self.color)
                display.blit(text, (self.position.x//3, self.position.y + y_offset))
                y_offset += (self.font.get_height() + 10)
        else:
            text = self.font.render(self.text, True, self.color)
            display.blit(text, (self.position.x + self.size.x / 2 - text.get_width() / 2, self.position.y + self.size.y / 2 - text.get_height() / 2))
