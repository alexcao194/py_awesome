from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets
from src.states.play import *
import random

class Win(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_loose)

    def __init_state__(self):
        super().__init_state__()
        
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.win_message_1 = Text(
            position=Vector2(screenWidth//2, 100),
            size=Vector2(30, 30),
            text=S().win_message_1, 
            font_size=75,
        )

        self.win_message_2 = Text(
            position=Vector2(screenWidth//2, 200),
            size=Vector2(30, 30),
            text=S().win_message_2, 
            font_size=45,
        )
        self.hero_attack = Image(
            src=Assets.tt_hero_attack,
            position=Vector2(screenWidth // 2 - 100, 300),
            scale=Vector2(7, 7),
        )
        self.play_again = ImageButton(
            position=Vector2(screenWidth // 2 - 120, 500),
            background=Assets.tt_background_button,
            text=S().all_restart,
            callback= self.onClickPlayAgain,
            font_size=28,
            scale=1.5
        )
        
        self.back_to_home = ImageButton(
            position=Vector2(screenWidth // 2 - 120, 600),
            background=Assets.tt_background_button,
            text=S().all_menu,
            callback= self.onClickBackToHome,
            font_size=28,
            scale=1.5
        )
        self.background_firework_1 = Image(
            src=Assets.tt_background_firework_1,
            position=Vector2(screenWidth // 6 + 25, 300),
            scale=Vector2(0.1, 0.1),
        )
        self.background_firework_2 = Image(
            src=Assets.tt_background_firework_2,
            position=Vector2(screenWidth // 2 + 100, 300),
            scale=Vector2(0.1, 0.1),
        )
        
        self.widget_group.add(self.win_message_1)
        self.widget_group.add(self.win_message_2)
        self.widget_group.add(self.hero_attack)
        self.widget_group.add(self.play_again)
        self.widget_group.add(self.back_to_home)
        self.widget_group.add(self.background_firework_1)
        self.widget_group.add(self.background_firework_2)
        
    def onClickPlayAgain(self):
        StateMachine.popUntil('Play')
        StateMachine.__current_state__().__init_state__()
            
    def onClickBackToHome(self):
        StateMachine.popUntil('Home')
        StateMachine.__current_state__().__init_state__()
        