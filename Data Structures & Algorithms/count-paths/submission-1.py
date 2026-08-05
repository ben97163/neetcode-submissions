class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 1
        for i in range(1, m+n-1):
            result *= i
        for i in range(1, n):
            result //= i
        for i in range(1, m):
            result //= i
        
        return int(result)