from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets

class Loose(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_loose)

    def __init_state__(self):
        super().__init_state__()
        
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.hero_death = Image(
            src=Assets.tt_hero_death,
            position=Vector2(screenWidth // 2 - 100, 130),
            scale=Vector2(6, 6),
        )
        
        self.title = Text(
            text=S().loose_gameover,
            position=Vector2(screenWidth // 2, 300),
            size=Vector2(30, 30),
            font_size=50
        )
        
        self.play_again = ImageButton(
            position=Vector2(screenWidth // 2 - 120, 350),
            background=Assets.tt_background_button,
            text=S().all_restart,
            callback= self.onClickPlayAgain,
            font_size=28,
            scale=1.5
        )
        
        self.back_to_home = ImageButton(
            position=Vector2(screenWidth // 2 - 120, 450),
            background=Assets.tt_background_button,
            text=S().all_menu,
            callback= self.onClickBackToHome,
            font_size=28,
            scale=1.5
        )

        self.widget_group.add(self.title)
        self.widget_group.add(self.hero_death)
        self.widget_group.add(self.play_again)
        self.widget_group.add(self.back_to_home)
        
    def onClickPlayAgain(self):
        StateMachine.popUntil('Play')
        StateMachine.__current_state__().__init_state__()
    
    def onClickBackToHome(self):
        StateMachine.popUntil('Home')
        StateMachine.__current_state__().__init_state__()

    
            