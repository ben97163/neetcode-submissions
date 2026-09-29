class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, subset, res):
            if not nums:
                res.append(subset.copy())
                return res
            
            for i in range(len(nums)):
                subset.append(nums[i])
                res = helper(nums[:i] + nums[i+1:], subset, res)
                subset.pop()

            return res
        
        return helper(nums, [], [])