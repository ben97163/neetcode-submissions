class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if len(nums) == 0:
                return [[]]
            
            cur = nums[0]
            potentialSols = helper(nums[1:])
            
            res = []
            for potentialSol in potentialSols:
                res.append(potentialSol)
                res.append([cur] + potentialSol)
            return res
        
        return helper(nums)