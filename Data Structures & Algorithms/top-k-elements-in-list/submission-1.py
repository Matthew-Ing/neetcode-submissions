class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for a in nums:
            count[a] = count.get(a,0)+1
        
        b = heapq.nlargest(k, count, key=count.get)
        return b

