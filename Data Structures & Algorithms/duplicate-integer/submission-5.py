class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort();
        # for a in range(len(nums)-1):
        #     if nums[a]==nums[a+1]:
        #         return True;
        # return False;
        s = set();
        for n in nums:
            if n in s:
                return True;
            s.add(n)
        return False;
