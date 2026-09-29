class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, cur):
            if i > n:
                if len(cur) == k:
                    res.append(cur.copy())
                return

            cur.append(i)
            helper(i+1, cur)
            cur.pop()
            helper(i+1, cur)
        
        
        helper(1, [])
        return res