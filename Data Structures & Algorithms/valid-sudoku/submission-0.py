class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for row in board:
            dct = [1] * 10
            for element in row:
                if element.isdigit():
                    dct[int(element)] -= 1
                    if dct[int(element)] < 0:
                        return False
        # check vertical
        for i in range(9):
            dct = [1] * 10
            for j in range(9):
                if board[j][i].isdigit():
                    dct[int(board[j][i])] -= 1
                    if dct[int(board[j][i])] < 0:
                        return False
        
        # check boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dct = [1] * 10
                for k in range(3):
                    for l in range(3):
                        if board[i + l][j + k].isdigit():
                            dct[int(board[i + l][j + k])] -= 1
                            if dct[int(board[i + l][j + k])] < 0:
                                return False

        return True