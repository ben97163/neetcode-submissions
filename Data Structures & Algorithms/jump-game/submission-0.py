class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if reachable < i:
                return False
            reachable = max(nums[i] + i, reachable) 
        
        return True