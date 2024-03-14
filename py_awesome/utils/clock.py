from ..core.singleton import Singleton
import pygame

class Clock(Singleton):
    time = 0
    delta_time = 0

    def __update__(event):
        Clock.delta_time = (pygame.time.get_ticks() - Clock.time) / 1000
        Clock.time = pygame.time.get_ticks()
