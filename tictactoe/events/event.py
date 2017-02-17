'''
TIC-TAC-TOE
WinterSalmon
'''
from common.equality_mixin import EqualityMixin
from common.auto_number_enum import AutoNumberEnum


class EVENT(AutoNumberEnum):
    '''
    Event Code used to identify event
    '''
    GAMESTART = ()
    PLACEMENT = ()
    GAMEOVER = ()


class Event(EqualityMixin):
    '''
    Event class for TicTacToe
    '''
    def __init__(self, code, name):
        if not isinstance(code, EVENT):
            raise ValueError("Event argument 'code' MUST BE 'EVENT' TYPE")
        self._code = code
        self._name = name
        self._args = dict()

    @property
    def code(self):
        '''
        returns event code
        '''
        return self._code

    @property
    def name(self):
        '''
        returns event name
        '''
        return self._name

    def _add_arg(self, key, value):
        '''
        set argument with (key,value)
        '''
        self._args[key] = value
