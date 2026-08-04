class Solution:
    def isHappy(self, n: int) -> bool:
        seen = defaultdict(int)
        while not seen[n]:
            seen[n] = True
            count = 0
            while n > 0:
                count += (n % 10) ** 2
                n //= 10
            if count == 1:
                return True
            n = count

        return False