'''
TIC-TAC-TOE
WinterSalmon
'''
from common.equality_mixin import EqualityMixin
from common.turn_counter import TurnCounter
from tictactoe.board import Board
from tictactoe.events.event import Event
from tictactoe.status.status import STATUS


class TicTacToe(TurnCounter, EqualityMixin):
    '''
    class to play TicTacToe
    '''
    def __init__(self, *, num_of_players=2, turn_count=0, board_size=3):
        super().__init__(num_of_players=num_of_players, turn_count=turn_count)
        self._board = Board(board_size)
        self._events = list()
        self._status = STATUS.GAMEINIT

    @property
    def board(self):
        '''returns board'''
        return self._board

    @property
    def events(self):
        '''returns evetns'''
        return self._events

    @property
    def status(self):
        '''returns status'''
        return self._status

    @status.setter
    def status(self, status):
        if not isinstance(status, STATUS):
            raise ValueError
        self._status = status

    def push(self, event):
        '''
        handle new event
        '''
        if isinstance(event, Event):
            if event.handle(self):
                self.events.append(event)
                return True
        return False
