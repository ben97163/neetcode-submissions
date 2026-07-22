class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, target in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            if i > 0 and target == nums[i - 1]:
                continue
            while left < right:
                if nums[left] + nums[right] + target > 0:
                    # print(nums[left] + nums[right] + target)
                    right -= 1
                elif nums[left] + nums[right] + target < 0:
                    left += 1
                else:
                    ans.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return ans
                