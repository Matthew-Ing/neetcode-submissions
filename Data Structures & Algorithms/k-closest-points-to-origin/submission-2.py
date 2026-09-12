class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap solution
        minheap = []
        for a, b in points:
            dist = (a**2) + (b**2)
            heapq.heappush(minheap, [dist, a, b])
        
        heapq.heapify(minheap)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res