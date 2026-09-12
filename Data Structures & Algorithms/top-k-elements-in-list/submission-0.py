class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap and find the frequency of each sorted

        hm = {}
        for a in nums:
            hm[a]=hm.get(a,0)+1;
        names = heapq.nlargest(k, hm, key=hm.get)
        return names;