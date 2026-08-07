class Solution:
    import sys

    # Increase the recursion depth limit
    sys.setrecursionlimit(100000)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[-1] * COL for _ in range(ROW)]
        def dfs(i, j, val):
            if i >= ROW or j >= COL or i < 0 or j < 0:
                return 0
            if matrix[i][j] <= val:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = 1 + max(
                dfs(i, j+1, matrix[i][j]),
                dfs(i, j-1, matrix[i][j]),
                dfs(i+1, j, matrix[i][j]),
                dfs(i-1, j, matrix[i][j]),
            )
            return dp[i][j]

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, -1)
        return max([item for row in dp for item in row])