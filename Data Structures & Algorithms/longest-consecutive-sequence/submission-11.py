class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largestSeq = 0
        currentSeq = 1
        a = sorted(set(nums))

        if len(nums) ==  0:
            return 0

        
        for b in a:
            
            if (b + 1) in a:
                currentSeq += 1
            else:
                currentSeq = 1
            if currentSeq> largestSeq:
                largestSeq = currentSeq

        return largestSeq
                