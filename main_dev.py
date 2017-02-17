'''
TIC-TAC-TOE
WinterSalmon
'''
from tictactoe.tictactoe import TicTacToe
from tictactoe.board import Position
from tictactoe.events.placement_event import PlacementEvent
from tictactoe.events.gamestart_event import GameStartEvent
from tictactoe.tictactoe_manager import TicTacToeManager


def show(game, *, print_all_events=False):
    '''print game to command line'''
    # print game status and players
    game_status_fmt = 'Stauts({}), Players({}) Events({})'
    print(game_status_fmt.format(game.status, game.num_of_players, len(game.events)))

    if print_all_events:
        for event in game.events:
            print(repr(event))

    # print board
    board = game.board
    for row in range(board.max_row):
        for col in range(board.max_col):
            value = board.get_value_at(row, col)
            if value is None:
                value = '.'
            print(value, end='\t')
        print('')

    print('')


def handle(game, event):
    '''handle game event'''
    game.push(event)


def rungame():
    '''run game simulation'''
    events = load_events_first_player_win()
    game = TicTacToe()
    for event in events:
        handle(game, event)
        show(game)

    manager = TicTacToeManager()
    name = manager.save(game)
    game = manager.load(name)
    show(game, print_all_events=True)

def load_events_first_player_win():
    '''load player one win events'''
    events = []
    events.append(GameStartEvent())
    events.append(PlacementEvent(0, Position(1, 1)))
    events.append(PlacementEvent(1, Position(1, 2)))

    events.append(PlacementEvent(0, Position(0, 0)))
    events.append(PlacementEvent(1, Position(2, 1)))

    events.append(PlacementEvent(0, Position(0, 1)))
    events.append(PlacementEvent(1, Position(1, 0)))

    events.append(PlacementEvent(0, Position(2, 2)))

    return events


if __name__ == "__main__":
    rungame()
