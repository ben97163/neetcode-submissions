class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, action): # 1 for buy, -1 for sell, 0 for cooldown
            if i >= len(prices):
                return 0
            if (i, action) in dp:
                return dp[(i, action)]
            
            if action == 1:
                dp[(i, action)] = max(dfs(i+1, -1) - prices[i], dfs(i+1, 1)) 
                return dp[(i, action)]
            elif action == -1:
                dp[(i, action)] = max(dfs(i+2, 1) + prices[i], dfs(i+1, -1))
                return dp[(i, action)]
        
        return dfs(0, 1)
