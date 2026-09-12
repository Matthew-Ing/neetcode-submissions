class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a max heap to keep track of the min element
        maxheap = []

        for a,b in points:
            dist = -((a**2)+(b**2))
            heapq.heappush(maxheap, [dist, a, b])
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        sol = []

        while maxheap:
            dist,x ,y = heapq.heappop(maxheap)
            sol.append([x,y])
        return sol        
