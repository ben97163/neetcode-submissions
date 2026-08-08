class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            # 記憶化檢查
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Base Case 1: Pattern 走完了，字串 s 也必須走完才算匹配成功
            if j == len(p):
                return i == len(s)

            # 檢查當前字元是否匹配 (需確保 s 還沒走完)
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # 情況 A: 下一個字元是 '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # 選擇 1: 跳過 '*' (當作 0 次，例如 "a*" 匹配 "") -> dfs(i, j + 2)
                # 選擇 2: 當前匹配，繼續用 '*' 匹配下一個 s[i] -> dfs(i + 1, j)
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]

            # 情況 B: 下一個字元不是 '*'
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return dfs(0, 0)