'''
TestCase For TicTacToeManager
'''
import tempfile
from unittest import TestCase, main

from tictactoe.tictactoe import TicTacToe
from tictactoe.tictactoe_manager import TicTacToeManager

# TODO : setUp temp_directory
# TODO : tearDown temp_directory
class TestTicTacToeManager(TestCase):
    '''Represents TicTacToeManager TestCase'''
    def setUp(self):
        '''Set Up Temp Directory'''
        # TODO : check using platform temp directory is safe
        self.manager = TicTacToeManager(tempfile.gettempdir())

    def tearDown(self):
        '''Distroy Temp Directory'''
        self.manager = None

    def test_tictactoe_manager_default(self):
        '''Test TicTacToeManager default'''
        ttt = TicTacToe()
        name = 'default'
        saved_name = self.manager.save(ttt, name=name)
        self.assertEqual(name, saved_name) # saved name should be same as given

        loaded_ttt = self.manager.load(name)
        self.assertEqual(ttt, loaded_ttt) # loaded ttt should be equal

    def test_tictactoe_manager_name(self):
        '''Test TicTacToeManager default name'''
        ttt = TicTacToe()
        name = self.manager.save(ttt)

        loaded_ttt = self.manager.load(name)
        self.assertEqual(ttt, loaded_ttt) # loaded ttt should be equal


if __name__ == "__main__":
    main()
