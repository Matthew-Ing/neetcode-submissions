class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))

    def help(self, nums):
        one = 0
        two = 0

        for a in nums:
            temp = max(a+one, two)
            one = two
            two = temp
        return two