class AnimationManager:
    '''
    When you want to use animation, you must create a AnimationManager object.
    AnimationManager has two dictionaries: action_animation and repeat_animation.
    action_animation is a dictionary that contains ActionAnimation objects.
    repeat_animation is a dictionary that contains RepeatAnimation objects.

    You can use play_action() to play an action animation.
    You can use change_animation() to change a repeat animation.
    '''
    def __init__(self, action_animation: dict = None, repeat_animation: dict = None, current_animation: str = None):
        if(action_animation == None):
            raise Exception("AnimationManager must have action_animation")
        if(repeat_animation == None):
            raise Exception("AnimationManager must have repeat_animation")
        if(current_animation == None):
            raise Exception("AnimationManager must have current_animation")
        self.action_animation = action_animation
        self.repeat_animation = repeat_animation
        self.current_repeat_animation = None
        self.current_action_animation = None
        self.current_repeat_animation = current_animation
        if(current_animation not in repeat_animation.keys()):
            raise Exception("current_animation must be in repeat_animation")

    def __render__(self, display):
        if(self.current_action_animation != None):
            self.action_animation[self.current_action_animation].__render__(display)
        else:
            self.repeat_animation[self.current_repeat_animation].__render__(display)

            
        if(self.current_action_animation != None and self.action_animation[self.current_action_animation].isStart == False):
            self.current_action_animation = None
            self.repeat_animation[self.current_repeat_animation].__reset__()
    
    def play_action(self, animation: str):
        if(self.current_action_animation != None):
            print("Action animation is already playing, skipped", self.current_action_animation)
            return
        if(animation in self.action_animation.keys()):
            self.current_action_animation = animation
            self.action_animation[self.current_action_animation].__reset__()
        else:
            raise Exception("Animation not found")
    
    def change_animation(self, animation: str):
        if(self.current_repeat_animation == animation):
            return
        if(animation in self.repeat_animation.keys()):
            self.current_repeat_animation = animation
            self.repeat_animation[self.current_repeat_animation].__reset__()
        else:
            raise Exception("Animation not found")