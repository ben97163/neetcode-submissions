class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        ans = 0
        for n in nums:
            if dct[n] != 0:
                continue
            dct[n] = 1 + dct[n-1] + dct[n+1]
            dct[n - dct[n-1]] = dct[n]
            dct[n + dct[n+1]] = dct[n]
            ans = max(ans, dct[n])
        return ans