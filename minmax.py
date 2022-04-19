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

class Minmax:
    def __init__(self,boardarr):
        self.boardarr = boardarr
        self.move_arr = compute_move_arr()

    def boardArr(self):
        print()
        print()
        for i in range(9):
            print(self.boardarr[i][0], " ", self.boardarr[i][1], " ", self.boardarr[i][2], " ",
                  self.boardarr[i][3], " ", self.boardarr[i][4], " ", )
        print("qwe")
        print()

        for i in range(9):
            for j in range(5):
                if self.boardarr[i][j] == 1: #is a green
                    for ii in range(9):
                        for jj in range(5):

                            distInSqr = distanceInSquare1(j,i,jj,ii)
                            ret = isValid16GutiMoveAI(self.move_arr, j, i, jj,ii, distInSqr, self.boardarr,1)
                            if ret == 1:
                                self.boardarr[i][j] = 0
                                self.boardarr[ii][jj] = 1
                                return self.boardarr


