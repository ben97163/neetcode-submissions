class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        seen = defaultdict(int)
        for i in range(len(s)):
            seen[s[i]] = i
        
        count = 0
        end = 0
        for i in range(len(s)):
            count += 1
            end = max(end, seen[s[i]])

            if i == end:
                res.append(count)
                count = 0
        
        return res
            