'''
TIC-TAC-TOE
WinterSalmon
'''


class TurnCounter():
    '''Keep Track Of (Turn Count) and (Turn Player)'''
    def __init__(self, *, num_of_players, turn_count):
        if num_of_players <= 0:
            raise ValueError("TurnTracker argument 'num_of_players' MUST BE GREATER THEN ZERO")
        if turn_count < 0:
            raise ValueError("TurnTracker argument 'turn_count' MUST BE POSITIVE Value")
        self._num_of_players = num_of_players
        self._turn_count = turn_count

    @property
    def num_of_players(self):
        '''returns number of players'''
        return self._num_of_players

    @property
    def turn_count(self):
        '''returns current turn count'''
        return self._turn_count

    def next_turn(self):
        '''increase turn count'''
        self._turn_count += 1

    def current_turn_player_number(self):
        '''returns current turn player number'''
        return self.seek_turn_player_number(0)

    def seek_turn_player_number(self, seek_turn):
        '''returns seek turn player number'''
        seek_turn_count = self.turn_count + seek_turn
        seek_turn_player_number = seek_turn_count % self.num_of_players
        return seek_turn_player_number
