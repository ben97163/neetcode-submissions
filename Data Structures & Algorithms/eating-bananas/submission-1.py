class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            k = (l+r) // 2
            print(k)
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            
            print(count)
            
            if count <= h:
                ans = k
                r = k - 1
                
            
            else:
                l = k + 1
        
        return ans