class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = False;
        for a in range(len(nums)):
            for b in range(len(nums)):
                if a != b:
                    if nums[a]==nums[b]:
                        st = True;

        return st;