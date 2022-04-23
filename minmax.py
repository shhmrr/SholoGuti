from copy import deepcopy
from enum import Flag
from tkinter.messagebox import NO
GREEN = 1
RED = 2
def distanceInSquare1(starting_j, starting_i, released_j, released_i):
    # x0,y0,x1,y1
    distInSqr = (starting_j - released_j) * (starting_j - released_j) + (starting_i - released_i) * (
            starting_i - released_i)
    return distInSqr
def isValid16GutiMoveAI(move_arr, starting_j, starting_i, released_j, released_i, distInSqr, board_Arr, currentPlayer):
    # need to varify if a move to (released_i, released_j) is possible

    target = (released_i, released_j)
    # print(target)
    for k in move_arr[starting_i][starting_j]:
        if k == target and board_Arr[target[0]][target[1]] == 0:
            if distInSqr == 1 or distInSqr == 2:
                return 1
            else:
                m1 = int((starting_i + k[0]) / 2)
                m2 = int((starting_j + k[1]) / 2)
                if (board_Arr[m1][m2] == -1):
                    return 1
                if (currentPlayer == 1 and board_Arr[m1][m2] == 2):
                    return 2
                if (currentPlayer == 2 and board_Arr[m1][m2] == 1):
                    return 2
    return 0
# returns possible move arrayList
def compute_move_arr():
    arr = [0] * 9
    for i in range(9):
        arr[i] = [0] * 5
        for j in range(5):
            arr[i][j] = []
    arr[0][0] = [(0, 2), (0, 4), (1, 1), (2, 2)]
    arr[0][2] = [(0, 0), (0, 4), (1, 2), (2, 2)]
    arr[0][4] = [(0, 0), (0, 2), (1, 3)]
    arr[1][1] = [(0, 0), (1, 2), (1, 3), (2, 2), (3, 3)]
    arr[1][2] = [(0, 2), (1, 1), (1, 3), (2, 2), (3, 2)]
    arr[1][3] = [(0, 4), (1, 1), (1, 2), (2, 2), (3, 1)]
    arr[2][0] = [(2, 1), (2, 2), (3, 0), (3, 1), (4, 2), (4, 0)]
    arr[2][1] = [(2, 0), (2, 2), (2, 3), (3, 1), (4, 1)]
    arr[2][2] = [(1, 1), (1, 2), (1, 3), (0, 0), (0, 4), (0, 2), (2, 0), (2, 1), (2, 3), (2, 4),
                 (3, 1), (3, 2), (3, 3), (4, 0), (4, 2), (4, 4)]
    arr[2][3] = [(2, 1), (2, 2), (2, 4), (3, 3), (4, 3)]
    arr[2][4] = [(2, 2), (2, 3), (3, 3), (3, 4), (4, 2), (4, 4)]
    arr[3][0] = [(2, 0), (3, 1), (3, 2), (4, 0), (5, 0)]
    arr[3][1] = [(2, 0), (2, 1), (2, 2), (1, 3), (3, 0), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (5, 1), (5, 3)]
    arr[3][2] = [(1, 2), (2, 2), (3, 0), (3, 1), (3, 3), (3, 4), (4, 2), (5, 2)]
    arr[3][3] = [(1, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4), (5, 1), (5, 3)]
    arr[3][4] = [(2, 4), (3, 2), (3, 3), (4, 4), (5, 4)]
    arr[4][0] = [(2, 0), (3, 0), (5, 0), (6, 0), (2, 2), (3, 1), (5, 1), (6, 2), (4, 1), (4, 2)]
    arr[4][1] = [(4, 0), (4, 2), (4, 3), (2, 1), (3, 1), (5, 1), (6, 1)]
    arr[4][2] = [(2, 0), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 3), (4, 4), (5, 1), (5, 2),
                 (5, 3), (6, 0), (6, 2), (6, 4)]
    arr[4][3] = [(2, 3), (3, 3), (4, 1), (4, 2), (4, 4), (5, 3), (6, 3)]
    arr[4][4] = [(2, 2), (2, 4), (3, 3), (3, 4), (4, 2), (4, 3), (5, 3), (5, 4), (6, 2), (6, 4)]
    # lets loop for the rest
    for i in range(4):
        for j in range(5):
            arr[8 - i][j] = []
            for k in arr[i][j]:
                if k[0] == i:
                    arr[8 - i][j].append((8 - i, k[1]))
                else:
                    arr[8 - i][j].append((8 - k[0], k[1]))

    return arr
def checkWinner(boardArr):
    ##to be used for deciding winner
    redcount = 0
    greencount = 0
    for i in range(9):
        for j in range(5):
            if boardArr[i][j] == 2:  ##counting red/human guti
                redcount += 1
            if boardArr[i][j] == 1:  ##counting green/AI guti
                greencount += 1
    if redcount == 0:
        print("Green Won")
        return 1

    if greencount == 0:
        print("Red Won")
        return 2
    return 0
#pass the board here
def evaluate(boardArr):
    redcount = 0
    greencount = 0
    for i in range(9):
        for j in range(5):
            if boardArr[i][j] == 2:  ##counting red/human guti
                redcount += 1
            if boardArr[i][j] == 1:  ##counting green/AI guti
                greencount += 1
    return greencount - redcount

def get_all_pieces(board,color):
    all_pieces = []
    for i in range(9):
        for j in range(5):
            if board[i][j] == color:  ##counting red/human guti
                  all_pieces.append((i,j))
    return all_pieces

def convert_to_tuple(board):
    board2 = deepcopy(board)
    for i in range(9):
        board2[i] = tuple(board[i])
    return tuple(board2)

def eating_dfs(now_i, now_j, board, mymap, valid_moves, step, move_arrr, color):
    # vyrevy
    mymap[convert_to_tuple(board)] = True
    # if I can't eat anything then add stuff in valid_moves
    eat_one = False
    for ii in range(9):
        for jj in range(5):
            distInSqr = distanceInSquare1(now_j, now_i, jj, ii)
            ret = isValid16GutiMoveAI(move_arrr, now_j, now_i, jj, ii, distInSqr, board, color)
            if ret == 2:
                skip_i = int((now_i+ii)/2)
                skip_j = int((now_j+jj)/2)
                new_board = deepcopy(board)
                new_board[now_i][now_j]  = 0
                new_board[ii][jj] = color
                new_board[skip_i][skip_j] = 0
                
                # if the new_board is not visited, go there
                if (mymap.get(convert_to_tuple(new_board)) == None):
                    eat_one = True
                    step.append((skip_i, skip_j))
                    eating_dfs(ii, jj, new_board, mymap, valid_moves, step, move_arrr, color)
    
    # can't eat anything ? -> last move in chain, add in valid_moves 
    if eat_one == False:
        valid_moves.append((now_i, now_j, deepcopy(step)))

    step.pop()
    
def get_valid_moves(board, color,piece):
    valid_moves = []
    i = piece[0]
    j = piece[1]
    move_arrr = compute_move_arr()
    for ii in range(9):
        for jj in range(5):
            distInSqr = distanceInSquare1(j, i, jj, ii)
            ret = isValid16GutiMoveAI(move_arrr, j, i, jj, ii, distInSqr, board, color)
            if ret == 1:
                valid_moves.append((ii,jj,[]))
            elif ret == 2:
                step = []
                skip_i = int((i+ii)/2)
                skip_j = int((j+jj)/2)
                step.append((skip_i, skip_j))
                # how to do this
                mymap = {}
                mymap[convert_to_tuple(board)] = True
                new_board = deepcopy(board)
                new_board[i][j]  = 0
                new_board[ii][jj] = color
                new_board[skip_i][skip_j] = 0
                eating_dfs(ii, jj, new_board, mymap, valid_moves, step, move_arrr, color)
                

                """
                while ret == 2:
                    for iii in range(9):
                        for jjj in range(5):
                            distInSqr = distanceInSquare1(jj, ii, jjj, iii)
                            ret = isValid16GutiMoveAI(move_arrr, jj, ii, jjj, iii, distInSqr, board, color)
                            if ret == 2:
                                step.append((int((ii + iii) / 2), int((jj + jjj) / 2)))
                valid_moves.append((ii, jj, step))
                """

    print(valid_moves)
    return valid_moves


def simulate_move(piece, move, board, skip,color):
    board[piece[0]][piece[1]] = 0
    board[move[0]][move[1]] = color
    #if skip:
     #   board[int(skip[0])][int(skip[1])] = 0
    for i in skip:

        print(i)
        row = int(i[0])
        col =  int(i[1])
        board[row][col] = 0

    return board



def get_all_moves(board, color):
    moves = []
    for piece in get_all_pieces(board,color):
        valid_moves = get_valid_moves(board,color,piece)
        print(piece)
        print(valid_moves)
        print()
        for i in valid_moves:
            move = (i[0],i[1])
            skip = i[2]
            print(move)
            temp_board = deepcopy(board)
            print("qqqq")
            print(skip)
            new_board = simulate_move(piece,move,temp_board,skip,color)
            moves.append(new_board)

    return moves




#position is the board object
def minimax(board, depth,max_player):
    if depth == 0 or  checkWinner(board):
        return evaluate(board), board

    if max_player:
        maxEval =float('-inf')
        best_move = None
        for move in get_all_moves(board,GREEN):
            evaluation = minimax(move,depth - 1,False)[0]
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval =float('inf')
        best_move = None
        for move in get_all_moves(board,RED):
            evaluation = minimax(move,depth - 1,True)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

class Minmax:
    def __init__(self,boardarr):
        self.boardarr = boardarr
        self.move_arr = compute_move_arr()




    def boardArr(self):
        print()
        print()
        print("minmaxpy")
        for i in range(9):
            print(self.boardarr[i][0], " ", self.boardarr[i][1], " ", self.boardarr[i][2], " ",
                  self.boardarr[i][3], " ", self.boardarr[i][4], " ", )
        print("qwe")
        print()

        #     for i in range(9):
        #         for j in range(5):
        #             if self.boardarr[i][j] == 1: #is a green
        #                 for ii in range(9):
        #                     for jj in range(5):
        #
        #                         distInSqr = distanceInSquare1(j,i,jj,ii)
        #                         ret = isValid16GutiMoveAI(self.move_arr, j, i, jj,ii, distInSqr, self.boardarr,1)
        #                         if ret == 1:
        #                             self.boardarr[i][j] = 0
        #                             self.boardarr[ii][jj] = 1
        #                             return self.boardarr,ret,i,j,ii,jj
        #                         if ret == 2:
        #                             print("first turn and two")
        #                             self.boardarr[i][j] = 0
        #                             midi = int((i+ii)/2)
        #                             midj = int((j+jj)/2)
        #                             self.boardarr[midi][midj] = 0
        #                             self.boardarr[ii][jj] = 1
        #                             return self.boardarr,ret,i,j,ii,jj
        value, self.boardarr = minimax(self.boardarr,3,True)
        return self.boardarr
