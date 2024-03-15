from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets

class About(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_about)
    
    def __init_state__(self):
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.title = Text(
            position=Vector2(screenWidth//2, 50),
            size=Vector2(30, 30),
            text=S().all_about, 
            font_size=80,
        )
        
        self.backButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 650),
            background=Assets.tt_background_button,
            text=S().all_back,
            callback= self.onClickBack,
            font_size=28,
            scale=1.5
        )
        # thong tin ve tac gia
        self.author = Text(
            position=Vector2(screenWidth // 9, screenHeight // 3),
            size=Vector2(30, 30),
            text=S().all_author,
            font_size=25,
        )
        self.author_name = Text(
            position=Vector2(screenWidth // 9, screenHeight // 3 + 50),
            size=Vector2(30, 30),
            text=S().all_author_name,
            font_size=20,
        )
        self.game = Text(
            position=Vector2(screenWidth // 2 + screenWidth // 12, screenHeight // 6),
            size=Vector2(30, 30),
            text=S().all_game,
            font_size=25,
        )
        self.game_instructions = Text(
            position=Vector2(screenWidth // 2 + screenWidth // 12, screenHeight // 6 + 25),
            size=Vector2(30, 30),
            text=S().all_game_instructions,
            font_size=20,
        )
        self.monster_stand = Image(
            src=Assets.tt_monster_stand,
            position=Vector2(screenWidth *2 //3 - 25, screenHeight *2 //3 ),
            scale=Vector2(4, 4),
        )
        self.hero_attack = Image(
            src = Assets.tt_hero_attack,
            position=Vector2(screenWidth // 20, screenHeight // 12 ),
            scale=Vector2(8, 8),
        )
        self.widget_group.add(self.title)
        self.widget_group.add(self.backButton)
        self.widget_group.add(self.author)
        self.widget_group.add(self.author_name)
        self.widget_group.add(self.game)
        self.widget_group.add(self.game_instructions)
        self.widget_group.add(self.monster_stand)
        self.widget_group.add(self.hero_attack)
         
    def onClickBack(self):
        StateMachine.pop()