class Solution:
    def check_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        res = []

        for i in range(len(s)):
            cur = s[:i+1]
            if self.check_palindrome(cur):
                valid_partitions = self.partition(s[i+1:])
                if valid_partitions:
                    res.extend([[cur] + valid_partition for valid_partition in valid_partitions])
            
        return res