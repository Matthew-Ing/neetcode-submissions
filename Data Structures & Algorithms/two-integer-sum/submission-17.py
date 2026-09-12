class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for a, b in enumerate(nums):
            new = target-b
            if new in maps:
                return [maps[new], a]
            maps[b] = a
        return
                