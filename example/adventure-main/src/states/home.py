from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets
from src.states.setting import Setting
from src.states.play import Play
from src.states.about import About
from src.states.win import Win

class Home(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)
    
    def __init_state__(self):
        AudioManager.play_background(Assets.sd_home)
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.continueButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 200),
            background=Assets.tt_background_button,
            text=S().all_start,
            callback= self.start_game,
            font_size=28,
            scale=1.5
        )

        self.restartButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 300),
            background=Assets.tt_background_button,
            text=S().all_continue,
            callback= self.continue_game,
            font_size=28,
            scale=1.5
        )

        self.menuButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 400),
            background=Assets.tt_background_button,
            text=S().all_settings,
            callback= self.open_setting,
            font_size=28,
            scale=1.5
        )


        self.settingButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 500),
            background=Assets.tt_background_button,
            text=S().all_about,
            callback= self.open_about,
            font_size=28,
            scale=1.5
        )

        self.widget_group.add(self.continueButton)
        self.widget_group.add(self.restartButton)
        self.widget_group.add(self.menuButton)
        self.widget_group.add(self.settingButton)

    
    def start_game(self):
        StateMachine.push(Play())     
        pass

    def continue_game(self):
        StateMachine.push(Play())
        pass
    
    def open_setting(self):
        StateMachine.push(Setting())
    
    def open_about(self):
        StateMachine.push(About())
        pass