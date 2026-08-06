class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 1, 1
        res = nums[0]
        for n in nums:
            tmp = minProd * n
            minProd = min(minProd * n, maxProd * n, n)
            maxProd = max(tmp, maxProd * n, n)
            res = max(res, maxProd)
        return res