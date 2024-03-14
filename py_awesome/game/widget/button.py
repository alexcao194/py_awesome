from ...utils.vector2 import Vector2
from ...game.widget.widget import Widget
from ...utils.media_query import MediaQuery
import pygame


class Button(Widget):
    '''
    Button is a widget that can be clicked.
    callback: callable - the function that is called when the button is clicked
    '''
    def __init__(self, text: str = None, callback: callable = None, size: Vector2 = None, position: Vector2 = Vector2(0, 0), font = MediaQuery.font_family, font_size: int = MediaQuery.font_size, delay_time: int = 1):
        super().__init__(position=position, size=size)
        if(text == None):
            raise Exception("Button must have a text")
        if not callable(callback):
            raise Exception("Callback must be callable")
        if(delay_time < 0):
            raise Exception("Delay time must be greater than 0")
        if(font_size < 0):
            raise Exception("Font size must be greater than 0")
        self.callback = callback
        self.font = pygame.font.Font(font, font_size)
        self.text = text
        self.delay_time = delay_time
        self.interactable = True
        self.interact_time = 2

    def __render__(self, display):
        if self.text:
            text = self.font.render(self.text, True, (255, 255, 255))
            display.blit(text, (self.position.x + self.size.x / 2 - text.get_width() / 2, self.position.y + self.size.y / 2 - text.get_height() / 2))

    def __update__(self, event):
        if not self.interactable:
            self.interact_time -=  1 / 60
            if self.interact_time <= 0:
                self.interactable = True
                self.interact_time = 2
            return
        
        self.__handle_events__(event)
        
    def __handle_events__(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.callback()
                self.interactable = False
    

class ImageButton(Button):
    '''
    ImageButton is a button that has an image as background.
    background: str - the path to the background image
    '''
    def __init__(self, background: str = None, callback: callable = None, size:Vector2 = None, position: Vector2 = None, scale = 1, text = "", font = MediaQuery.font_family, font_size: int = MediaQuery.font_size):
        if(background == None):
            raise Exception("ImageButton must have a background")
        self.image = pygame.image.load(background)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        if(size == None):
            self.size = Vector2(self.image.get_width(), self.image.get_height())
        else:
            self.size = size
        super().__init__(text=text, callback=callback, position=position, size=self.size, font=font, font_size=font_size)
    
    def __render__(self, display):
        display.blit(self.image, self.position.to_tuple())
        super().__render__(display)
        
class ImageButtonWithIcon(Button):
    '''
    ImageButtonWithIcon is a image button that has an image as leading icon.
    background: str - the path to the background image
    icon: str - the path to the icon image
    '''
    def __init__(self, background: str = None, icon: str = None, callback: callable = None, size:Vector2 = None, position: Vector2 = None, scale = 1, text = "", font = MediaQuery.font_family, font_size: int = MediaQuery.font_size):
        if(background == None):
            raise Exception("ImageButtonWithIcon must have a background")
        if(icon == None):
            raise Exception("ImageButtonWithIcon must have an icon")
        self.image = pygame.image.load(background)
        
        
        if(size == None):
            self.size = Vector2(self.image.get_width(), self.image.get_height())
            self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        else:
            self.size = size
            self.image = pygame.transform.scale(self.image, (int(self.size.x * scale), int(self.size.y * scale)))
            
        self.ic = pygame.image.load(icon)
        self.ic = pygame.transform.scale(self.ic, (int(self.ic.get_width() * scale), int(self.ic.get_height() * scale)))
        
        super().__init__(text=text, callback=callback, position=position, size=self.size, font=font, font_size=font_size)
    
    def __render__(self, display):
        display.blit(self.image, self.position.to_tuple())
        display.blit(self.ic, (self.position.x + 10, self.position.y + self.size.y // 2 - self.ic.get_height() // 2))
        text = self.font.render(self.text, True, (255, 255, 255))
        display.blit(text, (self.position.x + 20 + self.ic.get_height(), self.position.y + self.size.y // 2 - text.get_height() // 2))