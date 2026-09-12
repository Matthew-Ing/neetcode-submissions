class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        Nset = set(nums)

        for a in nums:
            if (a-1) not in Nset:
                length = 0
                while (a+length) in Nset:
                    length += 1
                longest = max(length, longest)
        return longest