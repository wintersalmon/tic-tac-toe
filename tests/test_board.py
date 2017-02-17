'''
TestCase For Board
'''
from unittest import TestCase, main
from tictactoe.board import Board


class TestBoardCreate(TestCase):
    '''Represents Board Create TestCases'''
    def test_crete_invalid_size(self):
        '''Test Board Creation with INVLID number'''
        self.assertRaises(ValueError, Board, 1)
        self.assertRaises(ValueError, Board, 2)
        self.assertRaises(ValueError, Board, -3)
        self.assertRaises(ValueError, Board, -2)

    def test_create_even_size(self):
        '''Test Board Creation with EVEN number'''
        self.assertRaises(ValueError, Board, 4)
        self.assertRaises(ValueError, Board, 6)
        self.assertRaises(ValueError, Board, 8)
        self.assertRaises(ValueError, Board, 100)

    def test_create_odd_size(self):
        '''Test Board Creation with ODD number'''
        Board(3)
        Board(5)
        Board(7)
        Board(99)


class TestBoardHasStraightLine(TestCase):
    '''Represents Board Pattern Check TestCases'''
    def setUp(self):
        self.board_size_list = [3, 5, 9]
        self.sample_values = [-9999999, -1, 0, 1, 9999999]

    def tearDown(self):
        self.board_size_list = None

    def test_board_not_straight_line(self):
        '''Test Board not has_straight_line horizontal'''
        for size in self.board_size_list:
            board = Board(size)
            self.assertTrue(not board.has_straight_line())

    def test_board_horizontal_line(self):
        '''Test Board has_straight_line horizontal'''
        for size in self.board_size_list:
            for value in self.sample_values:
                for row in range(size):
                    board = Board(size)
                    self._fill_board_horizontally(board, value=value, row=row)
                    self.assertTrue(board.has_straight_line())

    def test_board_vertical_line(self):
        '''Test Board has_straight_line vertical'''
        for size in self.board_size_list:
            for value in self.sample_values:
                for col in range(size):
                    board = Board(size)
                    self._fill_board_vertically(board, value=value, col=col)
                    self.assertTrue(board.has_straight_line())

    def test_board_diagnal_line(self):
        '''Test Board has_straight_line diagnal'''
        for size in self.board_size_list:
            for value in self.sample_values:
                board = Board(size)
                self._fill_board_diagnally(board, value=value)
                self.assertTrue(board.has_straight_line())

        for size in self.board_size_list:
            for value in self.sample_values:
                board = Board(size)
                self._fill_board_diagnally(board, value=value, direction=1)
                self.assertTrue(board.has_straight_line())

    def _fill_board_horizontally(self, board, *, value, row):
        '''fill board horizontally with value'''
        for col in range(board.max_col):
            board.set_value_at(row, col, value)

    def _fill_board_vertically(self, board, *, value, col):
        '''fill board vertically with value'''
        for row in range(board.max_row):
            board.set_value_at(row, col, value)

    def _fill_board_diagnally(self, board, *, value, direction=0):
        '''fill board diagnally with value'''
        max_idx = board.max_row
        for idx in range(max_idx):
            row = idx
            if direction: # LeftTop to RightBottom
                col = idx
            else: # RightTop to LeftBottom
                col = max_idx - idx - 1
            board.set_value_at(row, col, value)


if __name__ == "__main__":
    main()
