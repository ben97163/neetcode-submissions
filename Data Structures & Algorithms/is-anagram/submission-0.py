class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for i in s:
            seen[i] += 1
        for j in t:
            seen[j] -= 1
        
        for v in seen.values():
            if v != 0:
                return False

        return True 