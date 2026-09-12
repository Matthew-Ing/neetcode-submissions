class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for a in range(0, len(nums)-1):
            if nums[a] == nums[a+1]:
                return True
        return False
