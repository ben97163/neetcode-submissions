class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, res = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] - buy > res:
                res = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
        
        return res
            