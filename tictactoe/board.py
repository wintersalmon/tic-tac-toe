'''
TIC-TAC-TOE
WinterSalmon
'''
from collections import namedtuple

from common.equality_mixin import EqualityMixin


Position = namedtuple('Position', ['row', 'col'])


class Board(EqualityMixin):
    '''Represents TicTacToe Board'''
    def __init__(self, size):
        if size < 3:
            raise ValueError('size for board must be greater or equal then three')
        if size % 2 == 0:
            raise ValueError('size for board must be odd number')
        self._max_size = size
        self._blocks = [list() for _ in range(self._max_size)]
        for row in range(self._max_size):
            self._blocks[row] = [None for _ in range(self._max_size)]

    @property
    def max_row(self):
        '''Return Max Row Size'''
        return self._max_size

    @property
    def max_col(self):
        '''Return Max Column Size'''
        return self._max_size

    def get_value_at(self, row, col):
        '''
        returns value of block at (row, col)
        Throws IndexError Exception if (row, col) is invalid
        '''
        if self.is_position_valid(row, col):
            return self._blocks[row][col]
        else:
            raise IndexError

    def set_value_at(self, row, col, value):
        '''
        set value of the block at (row, col)
        Returns True if set value was complete
        '''
        if self.is_position_valid(row, col):
            self._blocks[row][col] = value
            return True
        else:
            return False

    def is_position_valid(self, row, col):
        '''returns True if (row, col) is valid(On Board)'''
        if row < 0 or row >= self.max_row:
            return False
        if col < 0 or col >= self.max_col:
            return False
        return True

    def has_straight_line(self):
        '''
        returns True if "Straight Line" exsist on Board

        Straight Line : Line that contains same data in a row (horizontally, vertically, diagnolly)
        '''
        if self._has_horizontal_straight_line():
            return True
        if self._has_vertical_straight_line():
            return True
        if self._has_diagnol_straight_line():
            return True
        return False

    def _has_horizontal_straight_line(self):
        values = list()
        for row in range(self.max_row):
            for col in range(self.max_col):
                values.append(self._blocks[row][col])
            if self._is_same_values(values):
                return True
            values.clear()
        return False

    def _has_vertical_straight_line(self):
        values = list()
        for col in range(self.max_col):
            for row in range(self.max_row):
                values.append(self._blocks[row][col])
            if self._is_same_values(values):
                return True
            values.clear()
        return False

    def _has_diagnol_straight_line(self):
        # ! max_row and max_col should be equal (and also odd number)
        max_idx = self.max_row

        # TopLeft To BottomRight
        values = list()
        for idx in range(max_idx):
            row = idx
            col = idx
            values.append(self._blocks[row][col])
        if self._is_same_values(values):
            return True

        # TopRight To BottomLeft
        values.clear()
        for idx in range(max_idx):
            row = idx
            col = max_idx - idx - 1
            values.append(self._blocks[row][col])
        if self._is_same_values(values):
            return True

        return False

    def _is_same_values(self, values):
        '''
        returns True if 'values' contain all same data (and Not None)
        '''
        value_set = set(values)
        if None in value_set:
            return False
        if len(value_set) != 1:
            return False
        if len(values) != self._max_size:
            return False
        return True
