'''
TIC-TAC-TOE
WinterSalmon
'''
from tictactoe.events.event import Event, EVENT
from tictactoe.status.status import STATUS


class GameStartEvent(Event):
    '''
    Placement Event class for TicTacToe
    '''
    def __init__(self):
        super().__init__(EVENT.GAMESTART, 'GameStart')

    def handle(self, game):
        '''handle event to game'''
        if game.status == STATUS.GAMEINIT:
            game.status = STATUS.GAMERUNNING
            return True
        else:
            return False
