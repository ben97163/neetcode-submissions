class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(start, target, subset, res):
            if target == 0:
                res.append(subset.copy())
                return res
            if target < 0:
                return res
            
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                res = helper(i, target-nums[i], subset, res)
                subset.pop()

            return res
        
        return helper(0, target, [], [])