class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for a in nums:
            s.add(a)
        if len(nums) == len(s):
                return False
        return True