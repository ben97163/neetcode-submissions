class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return 
            
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for di, dj in direction:
                dfs(i+di, j+dj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
