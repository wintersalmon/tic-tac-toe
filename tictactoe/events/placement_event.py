'''
TIC-TAC-TOE
WinterSalmon
'''
from tictactoe.events.event import Event, EVENT
from tictactoe.board import Position
from tictactoe.status.status import STATUS


class PlacementEvent(Event):
    '''Placement Event class for TicTacToe'''
    def __init__(self, value, position):
        super().__init__(EVENT.PLACEMENT, 'Placement')
        if not isinstance(position, Position):
            raise ValueError("PlacementEvent argument 'position' MUST BE TYPE(Position)")
        self._add_arg('value', value)
        self._add_arg('position', position)

    @property
    def value(self):
        '''returns event arg value'''
        return self._args['value']

    @property
    def position(self):
        '''returns event arg position'''
        return self._args['position']

    def handle(self, game):
        '''handle event to game'''
        if not game.status == STATUS.GAMERUNNING:
            return False

        if not game.board.is_position_valid(self.position.row, self.position.col):
            return False

        game.board.set_value_at(self.position.row, self.position.col, self.value)

        if game.board.has_straight_line():
            game.status = STATUS.GAMEOVER
        else:
            game.next_turn()

        return True
