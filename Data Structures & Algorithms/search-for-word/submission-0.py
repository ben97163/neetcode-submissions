class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, count, board):
            if count == len(word):
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            
            if word[count] != board[i][j]:
                return False
            

            board[i][j] = "#"
            valid = dfs(i, j+1, count + 1, board) or \
                    dfs(i, j-1, count + 1, board) or \
                    dfs(i+1, j, count + 1, board) or \
                    dfs(i-1, j, count + 1, board)
            
            board[i][j] = word[count]
            
            return valid
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, board):
                    return True
        
        return False