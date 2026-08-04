class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = defaultdict(lambda: -1)
        for c in coins:
            dp[c] = 1
        
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                minimum = float("inf")
                for c in coins:
                    if c < i and dp[i - c] != -1:
                        minimum = min(minimum, 1 + dp[i - c])
                
                if minimum != float("inf"):
                    dp[i] = minimum
        print(dp)

        
        return dp[amount]