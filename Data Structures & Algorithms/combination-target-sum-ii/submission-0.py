class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, tar):
            # base cases
            if tar == target:
                res.append(list(curr))
                return
            if len(candidates)<=i or tar>=target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, tar + candidates[i])
            curr.pop()

            while i +1 <len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, tar)

        dfs(0, [], 0)
        return res