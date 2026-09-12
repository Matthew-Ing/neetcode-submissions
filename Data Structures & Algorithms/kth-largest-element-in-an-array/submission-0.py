class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap

        minheap = []
        sol =0

        for a in nums:
            heapq.heappush(minheap, -a)
        
        heapq.heapify(minheap)

        while k>0:
            sol = -heapq.heappop(minheap)
            k-=1
        return sol