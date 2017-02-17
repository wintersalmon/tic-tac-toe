'''
TIC-TAC-TOE
WinterSalmon
'''


class Player():
    '''Represents Player class for TicTacToe'''
    def __init__(self, number, name):
        self._number = number
        self._name = name

    @property
    def number(self):
        '''returns number'''
        return self._number

    @property
    def name(self):
        '''returns player name'''
        return self._name
