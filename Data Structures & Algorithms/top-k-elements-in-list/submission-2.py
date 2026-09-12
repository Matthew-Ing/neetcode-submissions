class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
       

        for a in range(len(nums)):
            count[nums[a]] = 1+count.get(nums[a], 0)
            

      
        largest = dict(heapq.nlargest(k, count.items(), key=lambda item: item[1]))
        print(largest)
        
        return list(largest.keys())