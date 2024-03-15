from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets

class Setting(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background_loose)
    
    def __init_state__(self):
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        self.title = Text(
            position=Vector2(screenWidth//2, 50),
            size=Vector2(30, 30),
            text=S().all_settings,
            font_size=80, 
        )
        
        self.chooseLanguageTitle = Text(
            position=Vector2(900, 200),
            size=Vector2(30, 30),
            text= S().setting_language,
            font_size=50,
        )
        
        self.viOption = ImageButtonWithIcon(
            position=Vector2(700, 250),
            size=Vector2(200, 60),
            background=Assets.tt_background_button,
            icon=Assets.tt_flag_vi,
            text=S().setting_language_vi,
            callback= lambda:self.change_language('vi'),
            font_size=22
        )
        
        self.enOption = ImageButtonWithIcon(
            position=Vector2(950, 250),
            size=Vector2(200, 60),
            background=Assets.tt_background_button,
            icon=Assets.tt_flag_uk,
            text=S().setting_language_en,
            callback= lambda:self.change_language('en'),
            font_size=22
        )
        
        self.backButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 600),
            background=Assets.tt_background_button,
            text=S().all_back,
            callback= self.onClickBack,
            font_size=28,
            scale=1.5
        )
        
        self.toggleMusicTitle = Text(
            position=Vector2(screenWidth//5, screenHeight//4),
            size=Vector2(30, 30),
            text= S().setting_music_toggle,
            font_size=40,
        )
        
        self.toggleAudioTitle = Text(
            position=Vector2(screenWidth//5, screenHeight//4 + 100),
            size=Vector2(30, 30),
            text= S().setting_audio_toggle,
            font_size=40,
        )
        
        self.toggleMusicButton = CheckBox(
            position=Vector2(screenWidth//5 + 120, screenHeight//4 - 10),
            size=Vector2(50, 50),
            selected_src=Assets.tt_background_setting_toggle_music_off,
            unselected_src=Assets.tt_background_setting_toggle_music_on,
            selected= not AudioManager.is_background_music_on,
            callback= self.onToggleMusic
        )
        
        self.toggleAudioButton = CheckBox(
            position=Vector2(screenWidth//5 + 220, screenHeight//4 + 85),
            size=Vector2(50, 50),
            selected_src=Assets.tt_background_setting_toggle_audio_off,
            unselected_src=Assets.tt_background_setting_toggle_audio_on,
            selected= not AudioManager.is_sound_effects_on,
            callback= self.onToggleAudio
        )
        
        self.widget_group.add(self.title)
        self.widget_group.add(self.chooseLanguageTitle)
        self.widget_group.add(self.toggleMusicTitle)
        self.widget_group.add(self.toggleAudioTitle)
        self.widget_group.add(self.viOption)   
        self.widget_group.add(self.enOption)
        self.widget_group.add(self.backButton)
        self.widget_group.add(self.toggleMusicButton)
        self.widget_group.add(self.toggleAudioButton)
        
    
    def change_language(self, langueCode):
        S.language = langueCode
    
    def onClickBack(self):
        StateMachine.pop()
        
    def onToggleMusic(self, isOff: bool):
        if isOff:
            AudioManager.turn_off_music()
        else: 
            AudioManager.turn_on_music()
        
    def onToggleAudio(self, isOff: bool):
        if isOff:
            AudioManager.turn_off_effects()
        else:
            AudioManager.turn_on_effects()
