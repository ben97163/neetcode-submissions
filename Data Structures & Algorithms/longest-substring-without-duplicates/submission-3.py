class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        ans = 0
        if len(s) <= 1:
            return len(s)
        dct = defaultdict(bool)
        dct[s[l]] = True
        while r < len(s):
            if dct[s[r]]:
                
                while s[l] != s[r]:
                    dct[s[l]] = False
                    l += 1
                l += 1
            
            dct[s[r]] = True
            r += 1
            ans = max(ans, r - l)
        
        return ans
