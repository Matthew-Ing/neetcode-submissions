class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)== 1:
            return False

        for a in range(len(nums)):
            if nums[a-1] == nums[a]:
                return True
        return False 