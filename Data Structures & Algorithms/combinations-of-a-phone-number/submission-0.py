class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dct = {
            '2': ["a","b","c"],
            '3': ["d","e","f"],
            '4': ["g","h","i"],
            '5': ["j","k","l"],
            '6': ["m","n","o"],
            '7': ["p","q","r","s"],
            '8': ["t","u","v"],
            '9': ["w","x","y","z"]
        }

        ans = []
        cur = []
        
        def dfs(i):
            if i == len(digits):
                string = "".join(cur)
                if string != "":
                    ans.append(string)
                return
            
            for l in dct[digits[i]]:
                cur.append(l)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return ans

    