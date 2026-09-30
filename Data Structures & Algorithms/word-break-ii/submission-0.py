class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]
            
            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in words:
                    for rest in dfs(j):
                        if rest:
                            res.append(word + " " + rest)
                        else:
                            res.append(word)
                
            memo[i] = res
            return res
        
        return dfs(0)