class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # if len(nums)== 1:
        #     return False

        # for a in range(len(nums)):
        #     if nums[a-1] == nums[a]:
        #         return True
        # return False 

        # using a set

        seen = set()
        for a in nums:
            if a in seen:
                return True
            else:
                seen.add(a)
        return False