class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = nums[0]
        for a in nums[1:]:
            b = a ^ b
        return b
