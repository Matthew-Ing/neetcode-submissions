class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()

        # for a in range(0, len(nums)-1):
        #     if nums[a] == nums[a+1]:
        #         return True
        # return False

        hash = set()

        for a in nums:
            if a in hash:
                return True
            else:
                hash.add(a)
        return False