class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(candidates, target, subset, res):
            if target == 0:
                res.append(subset.copy())
                return res
            if target < 0:
                return res

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                res = helper(candidates[i+1:], target-candidates[i], subset, res)
                subset.pop()

            return res
        
        return helper(candidates, target, [], [])

