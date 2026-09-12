class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = 0
        for a in nums:
            b = a ^ b
        return b
