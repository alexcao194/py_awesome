from ..core.singleton import Singleton
from ..utils.vector2 import Vector2
from ..core.assets import Assets


class MediaQuery(Singleton):
    '''
    MediaQuery is a singleton class that contains the size of the window and the aspect ratio.
    '''
    size = Vector2(1200, 800)
    aspect_ratio = size.x / size.y
    font_family = Assets.font
    font_size = 32
    