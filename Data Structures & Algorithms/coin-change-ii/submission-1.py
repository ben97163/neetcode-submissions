class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        coins.sort()
        def dfs(i, target):
            if target == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, target) in dp:
                return dp[(i, target)]
        
            dp[(i, target)] = dfs(i, target-coins[i]) + dfs(i+1, target) if target >= coins[i] else 0
            return dp[(i, target)]
        dfs(0, amount)
        return dfs(0, amount)