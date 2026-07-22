class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        arr = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            dct[n] += 1
        for key, v in dct.items():
            arr[v].append(key)
        
        ans = []
        for i in range(len(nums), -1, -1):
            for j in arr[i]:
                ans.append(j)
                k -= 1
                if k == 0:
                    return ans
        
        
            
