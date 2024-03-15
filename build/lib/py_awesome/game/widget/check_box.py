from ...game.widget.button import Widget
from ...core.assets import Assets
from ...utils.vector2 import Vector2
import pygame

class CheckBox(Widget):
    '''
    CheckBox is a widget that can be clicked and has two states: selected and unselected.
    callback: callable - the function that is called when the button is clicked
    selected_src: str - the path to the image that is displayed when the checkbox is selected
    unselected_src: str - the path to the image that is displayed when the checkbox is unselected
    selected: bool - the initial state of the checkbox

    selected_src and unselected_src are optional. If they are not provided, the default images will be used.
    the function that is called when the checkbox is clicked must accept a boolean parameter.
    exp: def callback(selected: bool):
            pass
    '''
    def __init__(self, position: Vector2 = None, size: Vector2 = None, selected_src: str = None, unselected_src: str = None, selected: bool = False, callback: callable = None):
        super().__init__(position=position, size=size)
        if(selected_src == None):
            self.selected_src = Assets.ic_selected_check_box
        else:
            self.selected_src = selected_src
        if(unselected_src == None):
            self.unselected_src = Assets.ic_blank_check_box
        else:
            self.unselected_src = unselected_src
        if not callable(callback):
            raise Exception("Callback must be callable")
        self.selected = selected
        self.callback = callback
        self.__init_image__()
    
    def __init_image__(self):
        self.selected_image = pygame.image.load(self.selected_src)
        pygame.transform.scale(self.selected_image, (self.size.x, self.size.y))
        self.unselected_image = pygame.image.load(self.unselected_src)
        pygame.transform.scale(self.unselected_image, (self.size.x, self.size.y))
        if(self.selected_image.get_size() != self.unselected_image.get_size()):
            raise Exception("Selected and unselected images must have the same size")

    def __render__(self, display):
        if(self.selected):
            display.blit(self.selected_image, (self.position.x + self.size.x / 2 - self.selected_image.get_width() / 2, self.position.y + self.size.y / 2 - self.selected_image.get_height() / 2))
        else:
            display.blit(self.unselected_image, (self.position.x + self.size.x / 2 - self.unselected_image.get_width() / 2, self.position.y + self.size.y / 2 - self.unselected_image.get_height() / 2))
    
    def __update__(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.selected = not self.selected
                self.callback(self.selected)
                return True
        return False
