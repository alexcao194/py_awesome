from ...core.singleton import Singleton
from ...game.state.base_state import FallState

class StateMachine(Singleton):
    '''
    class StateMachine
    states: list - the list of states
    navigate between states
    '''
    __states__ = []        
    def push(state):
        StateMachine.__current_state__().__on_pause__()
        state.__init_state__()
        StateMachine.__states__.append(state)
    def pop():
        if(StateMachine.canPop()):
            StateMachine.__current_state__().__on_exit__()
            StateMachine.__states__.pop()
            StateMachine.__current_state__().__on_resume__()
    def popUntil(name):
        while(StateMachine.__current_state__().__class__.__name__ != name and StateMachine.canPop()):
            StateMachine.pop()
    def canPop():
        return StateMachine.__states__.__len__() > 1
    def __current_state__():
        if len(StateMachine.__states__) == 0:
            return FallState()
        return StateMachine.__states__[-1]
    def __rebuild_stack__():
        for state in StateMachine.__states__:
            state.__init_state__()


    
