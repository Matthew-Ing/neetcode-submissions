class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        csum = 0

        for a in nums:
            if csum < 0:
                csum = 0
            
            csum +=a
            maxSub = max(maxSub, csum)
        return maxSub