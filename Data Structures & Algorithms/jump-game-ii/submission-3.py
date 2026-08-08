class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(nums) - 1:
                return 0
            
            if nums[i] == 0:
                return 1e9
            
            dp[i] = 1e9
            for j in range(1, nums[i] + 1):
                dp[i] = min(dp[i], 1+dfs(i+j))
        
            return dp[i]
        
        return dfs(0)
