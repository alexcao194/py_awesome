from pygame import mixer
from ..core.singleton import Singleton
from ..core.local_strorage import LocalStorage


class AudioManager(Singleton):
    background_music = None
    is_background_music_on = LocalStorage.get_value('isMusicOn', True)
    is_sound_effects_on = LocalStorage.get_value('isSoundEffectOn', True)

    def play_background(src):
        if AudioManager.is_background_music_on:
            if AudioManager.background_music:
                mixer.music.stop()
            mixer.music.load(src)
            mixer.music.play(-1)
        AudioManager.background_music = src
        
    def play_effect(src):
        if AudioManager.is_sound_effects_on:
            sound = mixer.Sound(src)
            sound.play()

    def turn_on_music():
        if AudioManager.background_music:
            mixer.music.load(AudioManager.background_music)
            mixer.music.play(-1)
        AudioManager.is_background_music_on = True
        LocalStorage.put_value('isMusicOn', True)

    def turn_off_music():
        if AudioManager.background_music:
            mixer.music.stop()
        AudioManager.is_background_music_on = False
        LocalStorage.put_value('isMusicOn', False)

    def turn_on_effects():
        AudioManager.is_sound_effects_on = True
        LocalStorage.put_value('isSoundEffectOn', True)

    def turn_off_effects():
        AudioManager.is_sound_effects_on = False
        LocalStorage.put_value('isSoundEffectOn', False)
