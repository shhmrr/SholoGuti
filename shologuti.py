"""Tic Tac Toe."""


from game import Game
import sys


class SholoGuti(Game):
    """Sholo guti game class."""

    def __init__(self):
        """Construct new shologuti game instance."""
        #self.board = ['1', 'x', '1', 'x', '1', 'x', '1', '1', '1','x',  '1', '1', '1', '1', '1',  '1', '1', '1', '1', '1',       '-', '-', '-', '-', '-',    '2', '2', '2', '2', '2',     '2', '2', '2', '2', '2',        'x', '2', '2', '2', 'x',         '2', 'x', '2', 'x', '2']
        self.board = ['X', '-', 'X', '-', 'X', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                      'X', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', 'O', 'O',
                      'O', '-', 'O', '-', 'O', '-', 'O']
        self.player = 'X'
        self.winner = None

    def reset(self):
        """Reset board between games."""
        #self.board = ['1', 'x', '1', 'x', '1', 'x', '1', '1', '1','x',  '1', '1', '1', '1', '1',  '1', '1', '1', '1', '1',       '-', '-', '-', '-', '-',    '2', '2', '2', '2', '2',     '2', '2', '2', '2', '2',        'x', '2', '2', '2', 'x',         '2', 'x', '2', 'x', '2']
        self.board = ['X', '-', 'X', '-', 'X', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                      'X', '-', '-', '-', '-', '-', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '-', 'O', 'O',
                      'O', '-', 'O', '-', 'O', '-', 'O']
        self.player = 'X'
        self.winner = None

    def get_open_moves(self):
        """Returns list of available moves given current states and next states."""
        actions = []
        states = []
        for i, val in enumerate(self.board):
            if val == '-':
                actions.append(i)
                self.board[i] = self.player
                states.append(self.get_state(self.board))
                self.board[i] = '-'
        return states, actions

    def get_state(self, board):
        """Returns board state as String."""
        return ''.join(board)

    def is_win(self):
        # """Check the board for win condition.
        #
        # Possible outputs are X, O, Draw, None.
        # """
        # # Check win condition
        # row_1 = self.board[0] + self.board[1] + self.board[2]
        # row_2 = self.board[3] + self.board[4] + self.board[5]
        # row_3 = self.board[6] + self.board[7] + self.board[8]
        # col_1 = self.board[0] + self.board[3] + self.board[6]
        # col_2 = self.board[1] + self.board[4] + self.board[7]
        # col_3 = self.board[2] + self.board[5] + self.board[8]
        # diag_1 = self.board[0] + self.board[4] + self.board[8]
        # diag_2 = self.board[2] + self.board[4] + self.board[6]
        # triples = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]
        #
        # for triple in triples:
        #     if (triple == 'OOO'):
        #         return 'O'
        #     elif (triple == 'XXX'):
        #         return 'X'
        #
        # # Check draw condition
        # if '-' not in self.board:
        #     return 'Draw'
        #
        # return None

        #############################
        redcount = 0
        greencount = 0
        for i in range(45):

                if self.board[i] == '2':  ##counting red/human guti
                    redcount += 1
                if self.board[i] == '1':  ##counting green/AI guti
                    greencount += 1
        if redcount == 0:
            print("Green Won")
            return 'X'

        if greencount == 0:
            print("Red Won")
            return 'O'

        return None

    def is_valid_move(self, position):
        """Check that potential move is in a valid position.

        Valid means inbounds and not occupied.
        """
        if position >= 0 and position < len(self.board):
            return self.board[position] == '-'
        else:
            return False

    def make_move(self, position):
        """Makes move by setting position to player value.

        Also toggles player and returns is_win result.
        """
        self.board[position] = self.player
        self.player = 'O' if self.player == 'X' else 'X'
        return self.is_win()

    def read_input(self):
        """Define game specific read in function from command line."""
        return int(sys.stdin.readline()[:-1])

    def print_board(self):
        print('{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {} \n{} {} {} {} {}'.format(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4],
                                                                        self.board[5], self.board[6], self.board[7], self.board[8], self.board[9],
                                                                        self.board[10], self.board[11], self.board[12], self.board[13], self.board[14],
                                                                        self.board[15], self.board[16], self.board[17], self.board[18], self.board[19],
                                                                        self.board[20], self.board[21], self.board[22], self.board[23], self.board[24],
                                                                        self.board[25], self.board[26], self.board[27], self.board[28], self.board[29],
                                                                        self.board[30], self.board[31], self.board[32], self.board[33], self.board[34],
                                                                        self.board[35], self.board[36], self.board[37], self.board[38], self.board[39],
                                                                        self.board[40], self.board[41], self.board[42], self.board[43], self.board[44]))


        print('=====')

    def print_instructions(self):
        pass
