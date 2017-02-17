'''
TestCase For TicTacToe
'''
from unittest import TestCase, main
from tictactoe.tictactoe import TicTacToe


class TestTicTacToe(TestCase):
    '''Represents TicTacToe TestCase'''
    def test_create(self):
        '''Test TestTicTacToe Creation'''
        TicTacToe()
        TicTacToe(num_of_players=3)
        TicTacToe(board_size=5)
        TicTacToe(num_of_players=3, board_size=7)


if __name__ == "__main__":
    main()
