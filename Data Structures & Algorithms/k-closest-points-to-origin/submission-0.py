class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dist = (x**2 + y**2)
            res.append([dist, x, y])
        
        heapq.heapify(res)
        sol = []

        while k>0:
            dist, x, y = heapq.heappop(res)
            sol.append([x, y])
            k-=1
        return sol