class Solution:
    def climbStairs(self, n: int) -> int:
        dct = defaultdict(int)
        dct[1], dct[2] = 1, 2
        for i in range(3, n+1):
            dct[i] = dct[i-1] + dct[i-2]
        return dct[n]