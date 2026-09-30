class Solution:
    def __init__(self):
        self.seen = {}
    def maxCoins(self, nums: List[int]) -> int:
        tup = tuple(nums)
        if tup in self.seen:
            return self.seen[tup]
        nums = [1] + nums + [1]
        res = 0
        for i in range(1,len(nums)-1):
            res = max(res, nums[i - 1] * nums[i] * nums[i + 1] + self.maxCoins(nums[1:i] + nums[i+1:-1]))
        self.seen[tup] = res
        return res