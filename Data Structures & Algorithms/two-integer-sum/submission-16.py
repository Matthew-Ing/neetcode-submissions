class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)-1,-1, -1):
            new = target-nums[a]
            if new in nums:
                for b in range(len(nums)):
                    if new == nums[b] and a != b:
                        return [b, a]



        return [a, a]