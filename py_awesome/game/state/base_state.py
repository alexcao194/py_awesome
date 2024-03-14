from ...core.logger import log
from ...utils.media_query import *
from ...game.widget.widget_group import WidgetGroup
from ...game.entity.entity_group import EntityGroup
import pygame

class BaseState:
    '''
    class BaseState
    background: str - the path to the background image
    '''
    def __init__(self, background: str = None):
        if(self.__class__.__name__ == 'BaseState'):
            raise Exception("BaseState cannot be instantiated")
        if(background == None):
            raise Exception("BaseState must have a background")
        self.__background_asset__ = background
        self.__background_image__ = None



    def __update__(self, event):
        '''
        Update is called every frame.
        '''
        self.widget_group.__update__(event)
        self.entity_group.__update__(event)

    
    def __render__(self, display):
        '''
        Render is called every frame. 
        '''
        if(self.__background_asset__ != ''):
            display.blit(self.__background_image__, (0, 0))
        self.widget_group.__render__(display)
        self.entity_group.__render__(display)
    
    def __init_state__(self):
        '''
        Init is called when the state is created.
        '''
        self.__background_image__ = pygame.image.load(self.__background_asset__) # 
        width = self.__background_image__.get_width()
        height = self.__background_image__.get_height()
        # transform with original aspect ratio
        if(width < MediaQuery.size.x):
            self.__background_image__ = pygame.transform.scale(self.__background_image__, (MediaQuery.size.x, (MediaQuery.size.x / width) * height))
        if(height < MediaQuery.size.y):
            self.__background_image__ = pygame.transform.scale(self.__background_image__, ((MediaQuery.size.y / height) * width, MediaQuery.size.y))
        self.widget_group = WidgetGroup()
        self.entity_group = EntityGroup()
        
    def __on_pause__(self):
        '''
        OnPause is called when the state is paused.
        '''
        pass

    def __on_resume__(self):
        '''
        OnResume is called when the state is resumed.
        '''
        pass

    def __on_exit__(self):
        '''
        OnExit is called when the state is exited.
        '''
        pass
    
class FallState(BaseState):
    def __init__(self, background=''):
        super().__init__(background)
    
    def __render__(self, display):
        display.fill((255, 0, 0))
        
