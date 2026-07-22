class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = defaultdict(lambda: False)
        for n in nums:
            if dictionary[n] is True:
                return True
            else:
                dictionary[n] = True
        
        return False
