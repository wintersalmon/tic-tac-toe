'''
TIC-TAC-TOE
WinterSalmon
'''
import os
import pickle
from datetime import datetime


class TicTacToeManager():
    '''
    class to play TicTacToe
    '''
    def __init__(self, save_dir=None):
        # TODO : Check save_dir is valid
        # TODO : Check save_dir is writeable
        if save_dir is None:
            save_dir = 'save_files'
        os.chdir(save_dir)
        self.save_dir = os.getcwd()
        # TODO : FIX ISSUE
        #  When TicTacToeManager() is called more then once
        #  it causes issues

    def load(self, file_name):
        '''Returns TicTacToe Game Data'''
        with open(file_name, 'rb') as file:
            tictactoe = pickle.load(file)
            return tictactoe

    def save(self, tictactoe, *, name=None):
        '''Save TicTacToe Game Data to save_dir with name and time'''
        if name is None:
            date = datetime.now()
            file_name = date.strftime('%Y%m%d')
        else:
            file_name = name
        with open(file_name, 'wb') as file:
            pickle.dump(tictactoe, file)
        return file_name
