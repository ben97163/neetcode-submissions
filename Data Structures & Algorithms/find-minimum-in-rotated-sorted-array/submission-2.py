class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            if r - l == 1:
                return min(nums[l], nums[r])

            mid = (l+r) // 2
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid

        return nums[l]