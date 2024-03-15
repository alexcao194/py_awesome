import pygame
from ...utils.clock import Clock

class Animation:
    '''
    Base class for all animations.
    src - path to the folder containing the frames
    frame_count - number of frames in the animation
    entity - the entity that the animation is attached to
    delay - delay between frames
    '''
    frame_count = 0
    def __init__(self, src: str = None, frame_count: int = None, entity = None, delay: int = 0):
        if(self.__class__.__name__ == 'Animation'):
            raise Exception("Animation cannot be instantiated")
        if(src == None):
            raise Exception("Animation must have a source")
        if(frame_count == None):
            raise Exception("Animation must have a frame count")
        self.src = src
        self.frame_count = frame_count
        self.current_frame = 0
        self.images = [[], []]
        self.entity = entity
        self.delay = delay
        self.delay_count = 0
        self.__init_source__()

    def __init_source__(self):
        for i in range(self.frame_count):
            image = pygame.image.load(self.src + str(i) + '.png')
            image = pygame.transform.scale(image, self.entity.size.to_tuple())            
            self.images[0].append(image)
            image = pygame.transform.flip(image, True, False)
            self.images[1].append(image)
    
    def __next_frame__(self):
        if self.delay_count < self.delay:
            self.delay_count += Clock.delta_time * 1000
        else:
            self.delay_count = 0
            self.current_frame += 1
            if(self.current_frame >= self.frame_count):
                self.current_frame = 0
        return self.images[self.entity.fliped][self.current_frame]

    def __reset__(self):
        self.current_frame = 0
        self.delay_count = 0
    
    def __render__(self, display):
        display.blit(self.__next_frame__(), self.entity.position.to_tuple())



class ActionAnimation(Animation):
    '''
    Animation that plays once and stops.
    '''
    def __init__(self, src: str = None, frame_count: int = None, entity = None, delay: int = 0):
        super().__init__(src=src, frame_count=frame_count, entity=entity, delay=delay)
        
    def __reset__(self):
        self.isStart = True
        super().__reset__()

    def __next_frame__(self):
        __next_frame__ = super().__next_frame__()
        if(self.current_frame == self.frame_count - 1):
            self.isStart = False
        return __next_frame__

    def __render__(self, display):
        super().__render__(display)



class RepeatAnimation(Animation):
    '''
    Animation that plays repeatedly.
    '''
    def __init__(self, src: str, frame_count: int, entity, delay: int = 0):
        super().__init__(src=src, frame_count=frame_count, entity=entity, delay=delay)

        


    