class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for a in nums:
            d[a] = d.get(a,0) + 1
            

        # sort the data:
        res = []
        for b, c in d.items():
            res.append([c,b])
        res.sort()

        sol = []
        while len(sol)<k:
            sol.append(res.pop()[1])
        return sol
