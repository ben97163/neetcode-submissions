class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for s in string:
                arr[ord(s) - ord('a')] += 1
        
            dct[tuple(arr)].append(string)
        
        return list(dct.values())